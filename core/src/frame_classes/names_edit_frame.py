import json
import os
from collections import OrderedDict

import wx

from core.src.frame_classes.design_frame import MyDialogKetValueSetting


class NamesEditFrame(MyDialogKetValueSetting):
    def __init__(self, parent, names, path):
        super(NamesEditFrame, self).__init__(parent)
        self.names = names
        self.edit_group = OrderedDict(self.names)
        self.key_group = list(self.edit_group.keys())
        self.show_list = []
        self.path = path
        self.is_changed = False

    @staticmethod
    def string_format(key, value):
        return f'"{key}"->"{value}"'

    def get_names(self):
        return self.names

    def clear_data(self):
        self.m_textCtrl_new_value.Clear()
        self.m_textCtrl_new_key.Clear()

    def editor_init(self, event):
        for key, item in self.edit_group.items():
            self.show_list.append(f'"{key}"->"{item}"')

        self.m_listBox_name_exist.Clear()
        self.m_listBox_name_exist.Set(self.show_list)

    def view_item(self, event):
        index = event.GetSelection()
        key = self.key_group[index]
        value = self.edit_group.get(key)
        wx.MessageBox(f"'{key}'->'{value}'", "信息")

    def edit_exist_item(self, event):
        index = event.GetSelection()
        key = self.key_group[index]
        value = self.edit_group.get(key)

        self.m_textCtrl_new_key.SetValue(key)
        self.m_textCtrl_new_value.SetValue(value)

    def add_item(self, event):
        key = self.m_textCtrl_new_key.GetValue()
        value = self.m_textCtrl_new_value.GetValue()

        if key == "" or value == "":
            wx.MessageBox("键或值不能为空白！", "错误", wx.ICON_ERROR)

        else:
            if key in self.key_group:
                index = self.key_group.index(key)
                feedback = wx.MessageBox(f"【{key}】已经存在键组中，点击【确认】将会使用新值覆盖", "信息", wx.YES_NO | wx.ICON_INFORMATION)
                if feedback == wx.YES:
                    self.edit_group[key] = value
                    self.m_listBox_name_exist.SetString(index, f'"{key}"->"{value}"')
                    self.is_changed = True

            else:
                self.key_group.append(key)
                self.edit_group[key] = value
                self.is_changed = True
                self.m_listBox_name_exist.Append(f'"{key}"->"{value}"')

            self.clear_data()

    def clear_item(self, event):
        self.clear_data()

    def import_names(self, event):
        overwrite = 0
        new_item = 0
        dialog = wx.FileDialog(self, "加载键值对文件（json）", os.path.join(self.path, "core\\assets"), "names.json", "*json",
                               wx.FD_FILE_MUST_EXIST | wx.FD_OPEN)
        is_ok = dialog.ShowModal()
        if is_ok:
            try:
                with open(dialog.GetPath(), "r")as file:
                    temple = json.load(file)
                for key, item in temple.items():
                    if not isinstance(item, str):
                        raise TypeError("不可用文件")
                    self.edit_group[key] = item
                    if key in self.key_group:
                        overwrite += 1
                        index = self.key_group.index(key)
                        self.m_listBox_name_exist.SetString(index, self.string_format(key, item))
                    else:
                        new_item += 1
                        self.m_listBox_name_exist.Append(self.string_format(key, item))

                wx.MessageBox(f"导入键值对文件成功！\n\t覆盖：{overwrite}\n\t新增：{new_item}", "信息")
                self.is_changed=True
            except Exception as info:
                wx.MessageBox(f"导入键值对文件出现错误！\n{info.__str__()}")

    def close_save(self, event):
        if self.is_changed:
            feedback = wx.MessageBox("要应用这些变化吗？", "信息", wx.ICON_INFORMATION | wx.YES_NO)
            if feedback == wx.YES:
                save_data={k.lower():v for k,v in self.edit_group.items()}
                with open(os.path.join(self.path, "core\\assets\\names.json"), "w")as file:
                    json.dump(save_data, file, indent=4)

                self.names = dict(self.edit_group)

        super(NamesEditFrame, self).close_save(event)
