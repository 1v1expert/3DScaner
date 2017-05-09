# -*- coding: utf-8 -*-
# This file is part of the Horus Project

__author__ = 'Jesús Arroyo Torrens <jesus.arroyo@bq.com>'
__copyright__ = 'Copyright (C) 2014-2016 Mundo Reader S.L.'
__license__ = 'GNU General Public License v2 http://www.gnu.org/licenses/gpl2.html'

"""
PLY file point cloud loader.

    - Binary, which is easy and quick to read.
    - Ascii, which is harder to read, as can come with windows, mac and unix style newlines.

This module also contains a function to save objects as an PLY file.

http://en.wikipedia.org/wiki/PLY_(file_format)
"""

import struct
import numpy as np

from horus import __version__
from horus.util import model

import logging
logger = logging.getLogger(__name__)


def _load_ascii(mesh, stream, dtype, count, tri_count):
    fields = dtype.fields

    v = 0
    c = 0

    if 'c' in fields:
        mesh.has_colors = True
        c += 3
    if 'n' in fields:
        mesh.has_normals = True
        c += 3

    i = 0
    vertexes = []
    while i < count:
        i += 1
        data = stream.readline().split(' ')
        if data is not None:
            vertexes.append([float(data[v]), float(data[v + 1]), float(data[v + 2])])
            mesh._add_vertex(data[v], data[v + 1], data[v + 2], data[c], data[c + 1], data[c + 2])

    i = 0
    if tri_count > 0:
        triangles_indexes = []
        while i < tri_count:
            i += 1
            data = stream.readline().split(' ')
            triangles_indexes.append([int(data[1]), int(data[2]), int(data[3])])
        triangles_indexes = np.array(triangles_indexes)

        # Reconstruct vertexes via triangles order and set object not_point_cloud
        mesh._prepare_face_count(tri_count)
        for index in triangles_indexes:
            mesh._add_face(vertexes[index[0]][0], vertexes[index[0]][1], vertexes[index[0]][2],
                           vertexes[index[1]][0], vertexes[index[1]][1], vertexes[index[1]][2],
                           vertexes[index[2]][0], vertexes[index[2]][1], vertexes[index[2]][2])
    return not tri_count > 0


def _load_binary(mesh, stream, dtype, count, tri_count, fm):
    data = np.fromfile(stream, dtype=dtype, count=count)

    fields = dtype.fields
    mesh.vertex_count = count

    if 'v' in fields:
        mesh.vertexes = data['v']
    else:
        mesh.vertexes = np.zeros((count, 3))

    if 'n' in fields:
        mesh.normal = data['n']
        mesh.has_normals = True
    else:
        mesh.normal = np.zeros((count, 3))

    if 'c' in fields:
        mesh.colors = data['c']
        mesh.has_colors = True
    else:
        mesh.colors = 255 * np.ones((count, 3))

    if tri_count > 0:
        tri_data = np.fromfile(stream,
                               dtype=[('tr', '{0}u1, {0}i4, {0}i4, {0}i4'.format(fm), (1,))],
                               count=tri_count)
        triangles_indexes = tri_data['tr'][['f1', 'f2', 'f3']].view((fm + 'i4', 3)).reshape(tri_count, 3)

        # Reconstruct vertexes via triangles order and set object not_point_cloud
        vertexes = mesh.vertexes
        mesh._prepare_face_count(tri_count)
        for index in triangles_indexes:
            mesh._add_face(vertexes[index[0]][0], vertexes[index[0]][1], vertexes[index[0]][2],
                           vertexes[index[1]][0], vertexes[index[1]][1], vertexes[index[1]][2],
                           vertexes[index[2]][0], vertexes[index[2]][1], vertexes[index[2]][2])
    return not tri_count > 0


def load_scene(filename):
    obj = model.Model(filename)
    m = obj._add_mesh()
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
                if format == 'ascii':
                    fm = ''
                elif format == 'binary_big_endian':
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

            is_point_cloud = True
            if format is not None:
                if format == 'ascii':
                    m._prepare_vertex_count(count)
                    is_point_cloud = _load_ascii(m, f, dtype, count, tri_count)
                elif format == 'binary_big_endian' or format == 'binary_little_endian':
                    is_point_cloud = _load_binary(m, f, dtype, count, tri_count, fm)

            obj._is_point_cloud = is_point_cloud
            obj._post_process_after_load()
            return obj

        else:
            logger.error("Error: incorrect file format.")
            return None


def save_scene(filename, _object):
    with open(filename, 'wb') as f:
        save_scene_stream(f, _object)


def save_scene_stream(stream, _object):
    m = _object._mesh

    if m is not None:
        pack_type = '<fff'
        frame = "ply\n"
        frame += "format binary_little_endian 1.0\n"
        frame += "comment Generated by Horus {0}\n".format(__version__)
        frame += "element vertex {0}\n".format(m.vertex_count)
        frame += "property float x\n"
        frame += "property float y\n"
        frame += "property float z\n"
        if m.has_colors:
            frame += "property uchar red\n"
            frame += "property uchar green\n"
            frame += "property uchar blue\n"
            pack_type += 'BBB'
        if m.has_normals:
            frame += "property float nx\n"
            frame += "property float ny\n"
            frame += "property float nz\n"
            pack_type += 'fff'
        frame += "element face {0}\n".format(m.vertex_count // 3 if not _object.is_point_cloud() else 0)
        if not _object.is_point_cloud():
            frame += "property list uchar int vertex_indices\n"
        frame += "end_header\n"
        stream.write(frame)

        if m.has_colors and not m.has_normals:
            for i in xrange(m.vertex_count):
                packed = struct.pack(pack_type,
                                     m.vertexes[i, 0], m.vertexes[i, 1], m.vertexes[i, 2],
                                     m.colors[i, 0], m.colors[i, 1], m.colors[i, 2])
                stream.write(packed)
        elif m.has_colors and m.has_normals:
            for i in xrange(m.vertex_count):
                packed = struct.pack(pack_type,
                                     m.vertexes[i, 0], m.vertexes[i, 1], m.vertexes[i, 2],
                                     m.colors[i, 0], m.colors[i, 1], m.colors[i, 2],
                                     m.normal[i, 0], m.normal[i, 1], m.normal[i, 2])
                stream.write(packed)
        elif not m.has_colors and m.has_normals:
            for i in xrange(m.vertex_count):
                packed = struct.pack(pack_type,
                                     m.vertexes[i, 0], m.vertexes[i, 1], m.vertexes[i, 2],
                                     m.normal[i, 0], m.normal[i, 1], m.normal[i, 2])
                stream.write(packed)
        else:
            for i in xrange(m.vertex_count):
                packed = struct.pack(pack_type,
                                     m.vertexes[i, 0], m.vertexes[i, 1], m.vertexes[i, 2])
                stream.write(packed)

        if not _object.is_point_cloud():
            i = 0
            while i < m.vertex_count:
                stream.write(struct.pack("<Biii", 3, i, i + 1, i + 2))
                i += 3
