import os
import re

import wx

import core.src.struct_classes.extect_struct as es
from core.src.frame_classse.design_frame import MainFrame
from core.src.static_classes.file_read import FileFilter


class DragOrder(wx.FileDropTarget):
    def __init__(self, parent: es.PerWorkList, frame: MainFrame):
        super(DragOrder, self).__init__()
        self.frame = frame

        self.parent = parent

    def OnDropFiles(self, x, y, filenames):
        file_names = filenames
        try:
            file_names = list(file_names)
            self.frame.m_staticText_info.SetLabel(f"开始导入{len(filenames)}个文件")

            dir_name = (filter(lambda x: not os.path.isfile(x), file_names))
            dir_name = map(lambda x: FileFilter.all_file(x), dir_name)
            list(map(lambda x: file_names.extend(x), dir_name))

            file_names = (filter(lambda x: os.path.isfile(x), file_names))

            paths = list(filter(lambda x: re.match(r'^UISprite\s#\d+\.png$', os.path.basename(x)) is None, file_names))

            returned_tex, tex_info = FileFilter.file_deal(paths, self.parent, False, r'.+\.[Pp][Nn][Gg]',
                                                          True, '', self.frame.names, 1)

            returned_mesh, mesh_info = FileFilter.file_deal(paths, self.parent, False,
                                                            r'.+\.[Oo][Bb][Jj]', True, "-mesh", self.frame.names, 2)
            if returned_tex:
                self.frame.m_gauge_state.SetValue(50)
            if returned_mesh:
                self.frame.m_gauge_state.SetValue(100)

            self.parent.show_in_tree(self.frame.m_treeCtrl_info,self.frame.root)

        except RuntimeError:
            return False

        else:

            return True
