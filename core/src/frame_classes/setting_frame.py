import json
import os

import wx

from core.src.frame_classes.design_frame import MyDialogSetting
from core.src.frame_classes.names_edit_frame import NamesEditFrame
from core.src.static_classes.image_deal import ImageWork
from core.src.static_classes.static_data import GlobalData
from core.src.structs_classes.setting_structs import SettingHolder, PerSetting


class Setting(MyDialogSetting):

    def __init__(self, parent, setting_info, work_path, names):
        super(Setting, self).__init__(parent)
        self.names = names
        self.frame = parent
        self.setting = setting_info
        self.path = work_path

        self.data = GlobalData()

        pic, _ = ImageWork.pic_transform(os.path.join(self.path, "core\\assets\\img.png"),
                                         list(self.m_bitmap2.GetSize()))
        bitmap = wx.Bitmap.FromBufferRGBA(pic.width, pic.height, pic.tobytes())
        self.m_bitmap2.SetBitmap(bitmap)

        self.setting_hold = SettingHolder(setting_info)

        self.input_filter_tex = tuple(
            map(lambda v: str(v.pattern).replace("$", "\\.[Pp][Nn][Gg]$"), self.data.fp_pattern_group))
        self.input_filter_mesh = tuple(
            map(lambda x: str(x.pattern).replace('$', r'-mesh\.[Oo][Bb][Jj]$'), self.data.fp_pattern_group))

    def save_info(self):
        self.setting_hold.get_value()
        self.setting = self.setting_hold.get_dict()

        data = self.data
        self.setting[data.sk_input_filter_tex] = self.input_filter_tex[self.setting[data.sk_input_filter]]
        self.setting[data.sk_input_filter_mesh] = self.input_filter_mesh[self.setting[data.sk_input_filter]]

        with open(os.path.join(os.getcwd(), "core\\assets\\setting.json"), 'w')as file:
            json.dump(self.setting, file)

    def set_info(self, event):
        data = self.data
        val: PerSetting = self.setting_hold[data.sk_input_filter]
        val.set_link = self.m_radioBox_input_filter.SetSelection
        val.get_link = self.m_radioBox_input_filter.GetSelection

        val: PerSetting = self.setting_hold[data.sk_output_group]
        val.set_link = self.m_radioBox_output_group.SetSelection
        val.get_link = self.m_radioBox_output_group.GetSelection

        val: PerSetting = self.setting_hold[data.sk_use_cn_name]
        val.set_link = self.m_checkBox_ex_cn.SetValue
        val.get_link = self.m_checkBox_ex_cn.GetValue

        val: PerSetting = self.setting_hold[data.sk_open_output_dir]
        val.set_link = self.m_checkBox_open_dir.SetValue
        val.get_link = self.m_checkBox_open_dir.GetValue

        val: PerSetting = self.setting_hold[data.sk_skip_exist]
        val.set_link = self.m_checkBox_skip_exist.SetValue
        val.get_link = self.m_checkBox_skip_exist.GetValue

        val: PerSetting = self.setting_hold[data.sk_finish_exit]
        val.set_link = self.m_checkBox_finish_exit.SetValue
        val.get_link = self.m_checkBox_finish_exit.GetValue

        val: PerSetting = self.setting_hold[data.sk_clear_when_input]
        val.set_link = self.m_checkBox_clear_list.SetValue
        val.get_link = self.m_checkBox_clear_list.GetValue

        val: PerSetting = self.setting_hold[data.sk_make_new_dir]
        val.set_link = self.m_checkBox_new_dir.SetValue
        val.get_link = self.m_checkBox_new_dir.GetValue

        val: PerSetting = self.setting_hold[data.sk_export_all_while_copy]
        val.set_link = self.m_checkBox_ex_copy.SetValue
        val.get_link = self.m_checkBox_ex_copy.GetValue

        self.setting_hold.initial_val()

    def ok_press(self, event):
        self.save_info()
        self.Destroy()

    def cancel_press(self, event):
        self.Destroy()

    def apply_press(self, event):
        self.save_info()

    def update_names(self, event):
        wx.MessageBox("敬请期待", "信息", wx.ICON_INFORMATION)

    def edit_names(self, event):
        dialog = NamesEditFrame(self, self.names, self.path)
        dialog.ShowModal()
        self.names = dialog.get_names()

    def get_setting(self):
        return self.setting

    def get_names(self):
        return self.names
