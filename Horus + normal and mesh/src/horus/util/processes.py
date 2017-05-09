import subprocess
import sys
import numpy as np
import os
import multiprocessing

import struct

class NormalEstimation:
    def __init__(self, mesh, **args):
        assert mesh is not None
        self.neighborhood_size = args['neighborhood_size'] if 'neighborhood_size' in args.keys() else 100
        self.planes_count = args['planes_count'] if 'planes_count' in args.keys() else 1000
        self.acc_steps = args['acc_steps'] if 'acc_steps' in args.keys() else 15
        self.rotation_count = args['rotation_count'] if 'rotation_count' in args.keys() else 5
        self.tolerance_angle = args['tolerance_angle'] if 'tolerance_angle' in args.keys() else 79
        self.neighborhood_size_dens_est = args['neighborhood_size_dens_est'] \
                                          if 'neighborhood_size_dens_est' in args.keys() else 5
        self.mesh = mesh
        self.executed = False
        self._prepare()

    def __del__(self):
        try:
            os.remove('input.xyz')
            os.remove('output.xyz')
        except:
            pass

    def _prepare(self):
        with open('input.xyz', 'w') as f:
            for vertex in self.mesh.vertexes:
                f.write('{0} {1} {2}\n'.format(vertex[0], vertex[1], vertex[2]))

    def run_and_wait(self):
        with open('input.xyz', 'r') as stdin:
            with open('output.xyz', 'w') as stdout:
                return_code = subprocess.call(["./Hough_Exec",
                                               "-k {0}".format(self.neighborhood_size),
                                               "-t {0}".format(self.planes_count),
                                               "-p {0}".format(self.acc_steps),
                                               "-r {0}".format(self.rotation_count),
                                               "-a {0}".format(self.tolerance_angle / 100),
                                               "-e {0}".format(self.neighborhood_size_dens_est)],
                                              stdin=stdin,
                                              stdout=stdout,
                                              stderr=sys.stderr)
        if return_code == 0:
            self.executed = True
        else:
            raise RuntimeError('Execution of Hough_Exec was unsuccessful: return code {0}'.format(return_code))

    def get_normals(self):
        assert self.executed
        with open('output.xyz', 'r') as f:
            lines = f.readlines()

        index_of_data = 0
        for i, line in enumerate(lines):
            if line.strip() == 'points':
                index_of_data = i + 1
                break

        return np.array([[float(value) for value in line.split()[3:]] for line in lines[index_of_data:]])


class PoissonReconstruction:
    def __init__(self, mesh, **args):
        assert mesh is not None
        self.boundary_type = args['neighborhood_size'] if 'boundary_type' in args.keys() else 3
        self.octree_depth = args['octree_depth'] if 'octree_depth' in args.keys() else 8
        self.samples_per_node = args['samples_per_node'] if 'samples_per_node' in args.keys() else 1.5
        self.point_weight = args['point_weight'] if 'point_weight' in args.keys() else 4.0
        self.iterations = args['iterations'] if 'iterations' in args.keys() else 8
        self.full_depth = args['full_depth'] if 'full_depth' in args.keys() else 5
        self.density = args['density'] if 'density' in args.keys() else False
        self.linear_fit = args['linear_fit'] if 'linear_fit' in args.keys() else False
        self.polygon_mesh = args['polygon_mesh'] if 'polygon_mesh' in args.keys() else False

        self.mesh = mesh
        self.executed = False

        self.input_name = '__poisson_input.ply'
        self.output_name = '__poisson_output.ply'

        self._prepare()

    def __del__(self):
        try:
            os.remove(self.input_name)
        except:
            pass

    def _prepare(self):
        with open(self.input_name, 'wb') as f:
            self.__save_scene_stream(f, self.mesh)

    def __save_scene_stream(self, stream, m):
        if m is not None:
            pack_type = '<fff'
            frame = "ply\n"
            frame += "format binary_little_endian 1.0\n"
            frame += "element vertex {0}\n".format(m.vertex_count)
            frame += "property float x\n"
            frame += "property float y\n"
            frame += "property float z\n"
            if m.has_colors:
                frame += "property uchar red\n"
                frame += "property uchar green\n"
                frame += "property uchar blue\n"
                pack_type += 'BBB'
            frame += "property float nx\n"
            frame += "property float ny\n"
            frame += "property float nz\n"
            pack_type += 'fff'
            frame += "element face 0\n"
            frame += "end_header\n"
            stream.write(frame)

            if m.has_colors:
                for i in xrange(m.vertex_count):
                    packed = struct.pack(pack_type,
                                         m.vertexes[i, 0], m.vertexes[i, 1], m.vertexes[i, 2],
                                         m.colors[i, 0], m.colors[i, 1], m.colors[i, 2],
                                         m.normal[i, 0], m.normal[i, 1], m.normal[i, 2])
                    stream.write(packed)
            else:
                for i in xrange(m.vertex_count):
                    packed = struct.pack(pack_type,
                                         m.vertexes[i, 0], m.vertexes[i, 1], m.vertexes[i, 2],
                                         m.normal[i, 0], m.normal[i, 1], m.normal[i, 2])
                    stream.write(packed)

    def run_and_wait(self):
        # params = ["./PoissonRecon",
        #           "--in {0}".format('__poisson_input.ply'),
        #           "--out {0}".format(self.output_name),
        #           "--bType {0}".format(self.boundary_type),
        #           "--depth {0}".format(self.octree_depth),
        #           "--samplesPerNode {0}".format(self.samples_per_node),
        #           "--pointWeight {0}".format(self.point_weight),
        #           "--fullDepth {0}".format(self.full_depth),
        #           "--threads {0}".format(multiprocessing.cpu_count())]
        params = ["./PoissonRecon",
                  "--in", self.input_name,
                  "--out", self.output_name,
                  "--bType", str(self.boundary_type),
                  "--depth", str(self.octree_depth),
                  "--samplesPerNode", str(self.samples_per_node),
                  "--pointWeight", str(self.point_weight),
                  "--fullDepth", str(self.full_depth),
                  "--threads", str(multiprocessing.cpu_count())]
        if self.density:
            params.append("--density")
        if self.linear_fit:
            params.append("--linearFit")
        if self.polygon_mesh:
            params.append("--polygonMesh")

        return_code = subprocess.call(params, stdout=sys.stdout, stderr=sys.stdout)
        if return_code == 0:
            self.executed = True
        else:
            raise RuntimeError('Execution of PoissonRecon was unsuccessful: return code {0}'.format(return_code))

    def __load_binary(self, stream, dtype, count, tri_count, fm):
        data = np.fromfile(stream, dtype=dtype, count=count)

        fields = dtype.fields

        if 'v' in fields:
            vertexes = data['v']

        if 'n' in fields:
            normal = data['n']

        if 'c' in fields:
            colors = data['c']

        if tri_count > 0:
            tri_data = np.fromfile(stream,
                                   dtype=[('tr', '{0}u1, {0}i4, {0}i4, {0}i4'.format(fm), (1,))],
                                   count=tri_count)
            return tri_data['tr'][['f1', 'f2', 'f3']].view((fm + 'i4', 3)).reshape(tri_count, 3)

    def __load_scene(self, filename):
        with open(filename, "rb") as f:
            dtype = []
            count = 0
            tri_count = 0
            format = None
            line = None
            header = ''

            while line != 'end_header\n' and line != '':
                line = f.readline()
                header += line
            header = header.split('\n')

            if header[0] == 'ply':
                for line in header:
                    if 'format ' in line:
                        format = line.split(' ')[1]
                        break

                if format is not None:
                    if format == 'binary_big_endian':
                        fm = '>'
                    elif format == 'binary_little_endian':
                        fm = '<'

                df = {'float': fm + 'f', 'uchar': fm + 'B'}
                dt = {'x': 'v', 'nx': 'n', 'red': 'c', 'alpha': 'a'}
                ds = {'x': 3, 'nx': 3, 'red': 3, 'alpha': 1}

                for line in header:
                    if 'element vertex ' in line:
                        count = int(line.split('element vertex ')[1])
                    elif 'property ' in line:
                        props = line.split(' ')
                        if props[2] in dt.keys():
                            dtype = dtype + [(dt[props[2]], df[props[1]], (ds[props[2]],))]
                    elif 'element face ' in line:
                        tri_count = int(line.split('element face ')[1])

                dtype = np.dtype(dtype)

                if format is not None:
                    return self.__load_binary(f, dtype, count, tri_count, fm)

    def get_triangles(self):
        assert self.executed
        try:
            triangles = self.__load_scene(self.output_name)
            return triangles
        except:
            return None
