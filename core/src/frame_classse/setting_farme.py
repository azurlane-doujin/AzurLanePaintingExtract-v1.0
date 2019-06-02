import json
import os

import wx

from core.src.frame_classse.design_frame import MyDialogSetting
from core.src.static_classes.image_deal import ImageWork
from core.src.static_classes.static_data import GlobalData
from core.src.struct_classes.setting_struct import SettingHolder, PerSetting


class Setting(MyDialogSetting):

    def __init__(self, parent, setting_info, work_path):
        super(Setting, self).__init__(parent)
        self.frame = parent
        self.setting = setting_info
        self.path = work_path
        self.data = GlobalData()

        pic = ImageWork.pic_transform(os.path.join(self.path, "core\\assets\\img.png"), list(self.m_bitmap2.GetSize()))
        bitmap = wx.Bitmap.FromBufferRGBA(pic.width, pic.height, pic.tobytes())
        self.m_bitmap2.SetBitmap(bitmap)

        self.setting_hold = SettingHolder(setting_info)

        self.input_filter_tex = (
            r'^.+(?<!_[\dhg])\.[Pp][Nn][Gg]$',
            r'^.+(?<=_\d)\.[Pp][Nn][Gg]$',
            r'^.+(?<=_g)\.[Pp][Nn][Gg]$',
            r'^.+(?<=_h)\.[Pp][Nn][Gg]$',
            r'^.+_younvy(?:_[\dhg])?\.[Pp][Nn][Gg]$',
        )
        self.input_filter_mesh = (
            r'^.+(?<!_[\dhg])-mesh\.[Oo][Bb][Jj]$',
            r'^.+(?<=_\d)-mesh\.[Oo][Bb][Jj]$',
            r'^.+(?<=_g)-mesh\.[Oo][Bb][Jj]$',
            r'^.+(?<=_h)-mesh\.[Oo][Bb][Jj]$',
            r'^.+_younvy(?:_[\dhg])?-mesh\.[Oo][Bb][Jj]$',
        )

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

    def get_setting(self):
        return self.setting
