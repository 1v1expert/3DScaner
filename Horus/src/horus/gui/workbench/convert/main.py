import sys
import wx._core
import threading

from horus.util import resources, system
from horus.gui.engine import driver
from horus.gui.workbench.workbench import Workbench


class ConvertWorkbench(Workbench):
    def __init__(self, parent, toolbar_convert, scanning_workbench,
                 on_normal_computing_ended=None, on_mesh_reconstruction_ended=None):
        Workbench.__init__(self, parent, name=_('Converting workbench'))
        self.toolbar_convert = toolbar_convert
        ToolbarConvert(parent, self.toolbar_convert, scanning_workbench,
                       on_normal_computing_ended, on_mesh_reconstruction_ended)

    def on_open(self):
        pass

    def reset(self):
        pass

    def on_close(self):
        pass

    def setup_engine(self):
        pass

    def add_pages(self):
        pass

    def add_panels(self):
        pass


class ToolbarConvert:
    def __init__(self,
                 parent,
                 toolbar,
                 scanning_workbench,
                 on_normal_computing_ended,
                 on_mesh_reconstruction_ended):
        self.parent = parent
        self.toolbar = toolbar
        self.on_normal_computing_ended = on_normal_computing_ended
        self.on_mesh_reconstruction_ended = on_mesh_reconstruction_ended
        self.scanning_workbench = scanning_workbench
        # Elements
        self.normals_calculation_tool = self.toolbar.AddLabelTool(
            wx.NewId(), _("Normals calculation"),
            wx.Bitmap(resources.get_path_for_image("connect.png")), shortHelp=_("Normals calculation"))
        self.mesh_reconstruction_tool = self.toolbar.AddLabelTool(
            wx.NewId(), _("Mesh reconstruction"),
            wx.Bitmap(resources.get_path_for_image("disconnect.png")), shortHelp=_("Mesh reconstruction"))
        self.toolbar.Realize()

        self._enable_tool(self.normals_calculation_tool, True)
        self._enable_tool(self.mesh_reconstruction_tool, True)

        self.normals_calculation_thread = None
        self.normals_calculation_thread_dialog = None
        self.normals_is_calculated = False

        self.reconstruction_thread = None
        self.reconstruction_thread_dialog = None
        self.is_reconstructed = False

        # Events
        self.toolbar.Bind(wx.EVT_TOOL, self.on_normals_calculation_clicked, self.normals_calculation_tool)
        self.toolbar.Bind(wx.EVT_TOOL, self.on_mesh_reconstruction_clicked, self.mesh_reconstruction_tool)

    def __normals_calculation(self):
        try:
            self.scanning_workbench.scene_view._object._mesh.calculate_normals_with_normal_estimation()	
            self.normals_is_calculated = True
            wx.CallAfter(lambda: self.normals_calculation_thread_dialog.Update(100, ''))
            wx.CallAfter(lambda: self.on_normal_computing_ended(True))
        except Exception as e:
            wx.CallAfter(lambda: self.normals_calculation_thread_dialog.Update(100, ''))
            wx.CallAfter(lambda: self.on_normal_computing_ended(False))

    def __reconstruction(self):
        try:
            output = self.scanning_workbench.scene_view._object._mesh.reconstruct_poisson()	
            self.is_reconstructed = True
            wx.CallAfter(lambda: self.scanning_workbench.scene_view.load_file(output))
            wx.CallAfter(lambda: self.reconstruction_thread_dialog.Update(100, ''))
            wx.CallAfter(lambda: self.on_mesh_reconstruction_ended(True))
        except Exception as e:
            wx.CallAfter(lambda: self.reconstruction_thread_dialog.Update(100, ''))
            wx.CallAfter(lambda: self.on_mesh_reconstruction_ended(False))

    def on_normals_calculation_clicked(self, event):
        self.normals_calculation_thread_dialog = wx.ProgressDialog("Waiting normals computation",
                                                                   "Please, wait normals computation",
                                                                   maximum=100,
                                                                   parent=self.parent,
                                                                   style=wx.PD_APP_MODAL | wx.PD_AUTO_HIDE
                                                                       | wx.PD_SMOOTH | wx.PD_ELAPSED_TIME)
        if self.scanning_workbench.scene_view._object is not None:
            self.normals_is_calculated = False
            self.normals_calculation_thread = threading.Thread(target=self.__normals_calculation)
            self.normals_calculation_thread.start()
            while not self.normals_is_calculated:
                self.normals_calculation_thread_dialog.Pulse('')
                threading._sleep(0.025)
            if sys.platform == "win32":
			    self.normals_calculation_thread_dialog.Destroy()
        else:
            self._show_message(_("ToolbarConvert"), wx.ICON_ERROR, _("Object is empty"))

    def on_mesh_reconstruction_clicked(self, event):
        self.reconstruction_thread_dialog = wx.ProgressDialog("Waiting reconstruction",
                                                              "Please, wait mesh reconstruction",
                                                              maximum=100,
                                                              parent=self.parent,
                                                              style=wx.PD_APP_MODAL | wx.PD_AUTO_HIDE
                                                                    | wx.PD_SMOOTH | wx.PD_ELAPSED_TIME)
        if self.scanning_workbench.scene_view._object is not None:
            self.is_reconstructed = False
            self.reconstruction_thread = threading.Thread(target=self.__reconstruction)
            self.reconstruction_thread.start()
            while not self.is_reconstructed:
                self.reconstruction_thread_dialog.Pulse('')
                threading._sleep(0.025)
            if sys.platform == "win32":
                self.reconstruction_thread_dialog.Destroy()
        else:
            self._show_message(_("ToolbarConvert"), wx.ICON_ERROR, _("Object is empty"))

    def _show_message(self, title, style, desc):
        dlg = wx.MessageDialog(self.toolbar, desc, title, wx.OK | style)
        dlg.ShowModal()
        dlg.Destroy()

    def _enable_tool(self, item, enable):
        self.toolbar.EnableTool(item.GetId(), enable)
