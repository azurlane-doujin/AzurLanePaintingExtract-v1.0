import os
import re
from itertools import filterfalse

import wx

import core.src.structs_classes.extract_structs as es
from core.src.static_classes.file_read import FileFilter
from core.src.static_classes.static_data import GlobalData


class DropOrder(wx.FileDropTarget):
    def __init__(self, parent: es.PerWorkList, view_work: es.PerWorkList, frame, get_input_data):
        super(DropOrder, self).__init__()
        self.get_input_data = get_input_data
        self.view_work = view_work
        self.frame = frame

        self.parent = parent
        self.data = GlobalData()

    def OnDropFiles(self, x, y, filenames):
        file_names = filenames
        try:
            file_names = list(file_names)
            self.frame.m_staticText_info.SetLabel(f"开始导入{len(filenames)}个文件")

            dir_name = (filter(lambda temple_value: not os.path.isfile(temple_value), file_names))
            dir_name = map(lambda temple_value: FileFilter.all_file(temple_value), dir_name)
            list(map(lambda temple_value: file_names.extend(temple_value), dir_name))
            file_names = (filter(lambda temple_value: os.path.isfile(temple_value), file_names))
            paths = list(
                filterfalse(lambda temple_value: re.match(r'^UISprite\s#\d+\.png$', os.path.basename(temple_value)),
                            file_names))

            returned_tex, tex_info = FileFilter.file_deal(paths, self.parent, False,
                                                          self.frame.setting_info[self.data.sk_input_filter_tex],
                                                          True, '', self.frame.names, self.data.fi_texture_type)

            returned_mesh, mesh_info = FileFilter.file_deal(paths, self.parent, False,
                                                            self.frame.setting_info[self.data.sk_input_filter_mesh],
                                                            True, "-mesh", self.frame.names, self.data.fi_mesh_type)
            if returned_tex:
                self.frame.m_gauge_state.SetValue(50)
            if returned_mesh:
                self.frame.m_gauge_state.SetValue(100)

            self.view_work = es.PerWorkList(self.parent)

            self.frame.m_treeCtrl_info.DeleteChildren(self.frame.root)
            self.parent.show_in_tree(self.frame.m_treeCtrl_info, self.frame.root)

            self.get_input_data(self.view_work, self.parent)
        except RuntimeError:
            return False

        else:

            return True


class FaceDragOrder(wx.FileDropTarget):
    def __init__(self, parent, callback,type_is):
        self.type_is = type_is
        self.parent = parent
        self.callback = callback
        super(FaceDragOrder, self).__init__()

    def OnDropFiles(self, x, y, filenames):
        filenames = list(filenames)
        data = {}
        is_all_only = True
        files = filter(lambda val: os.path.isfile(val), filenames)

        if self.type_is:
            match_pattern = re.compile(r'^(\d+)(\s#\d+?)?\.(?:png|PNG)$')
        else:
            match_pattern=re.compile(r'^(.+?)\.(?:png|PNG)$')
        for value in files:
            file_name = os.path.basename(value)
            matched = match_pattern.match(file_name)
            if matched is None:
                continue
            count = (matched.group(1))
            if count in data.keys():
                data[count].append(value)
                is_all_only = False
            else:
                data[count] = [value]

        self.callback(data, is_all_only)

        return True


class AtlasDropOrder(wx.FileDropTarget):
    def __init__(self, parent, callback):
        self.parent = parent
        self.callback = callback

        super(AtlasDropOrder, self).__init__()

    def OnDropFiles(self, x, y, filenames):
        ables = filter(lambda x: x.endswith("atlas") or x.endswith("atlas.txt"), filenames)
        items = iter(ables)

        self.callback(next(items))
        return True


class SpriteDropOrder(wx.FileDropTarget):
    def __init__(self, callback):
        super(SpriteDropOrder, self).__init__()
        self.files = []
        self.callback = callback


    def OnDropFiles(self, x, y, filenames):
        file_names = list(filenames)
        dir_name = (filter(lambda temple_value: not os.path.isfile(temple_value), file_names))
        dir_name = map(lambda temple_value: FileFilter.all_file(temple_value), dir_name)
        list(map(lambda temple_value: file_names.extend(temple_value), dir_name))
        file_names = (filter(lambda temple_value: os.path.isfile(temple_value), file_names))

        return self.callback(file_names)

