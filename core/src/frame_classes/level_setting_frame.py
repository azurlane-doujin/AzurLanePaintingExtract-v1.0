import json
import os

from core.src.frame_classes.design_frame import MyDialogHeightSetting
from core.src.frame_classes.location_update import LocationUpdate
from core.src.frame_classes.names_edit_frame import NamesEditFrame
from core.src.static_classes.static_data import GlobalData


class LevelSettingFrame(MyDialogHeightSetting):
    def __init__(self, parent, height_setting, names, work_path,miss_names,path):
        super(LevelSettingFrame, self).__init__(parent)
        self.setting = height_setting
        self.names = names
        self.frame = parent
        self.path = work_path
        self.data = GlobalData()

        self.miss_names=miss_names

        self.path=path

    def prepare_data(self, event):
        data = self.data
        self.m_textCtrl_mesh_first.SetValue(self.setting[data.sk_mash_match][0])
        self.m_textCtrl_mesh_second.SetValue(self.setting[data.sk_mash_match][1])

        self.m_textCtrl_tex_first.SetValue(self.setting[data.sk_texture_match][0])
        self.m_textCtrl_tex_second.SetValue(self.setting[data.sk_texture_match][1])

    def update_names(self, event):
        dialog = LocationUpdate(self, self.names, self.path, self.setting[self.data.sk_local_data])
        dialog.ShowModal()

        self.setting[self.data.sk_local_data] = dialog.get_local_data()

    def edit_names(self, event):
        dialog = NamesEditFrame(self, self.names, self.path,self.miss_names)
        dialog.ShowModal()
        self.names = dialog.get_names()

    def ok_click(self, event):
        self.change_data()
        self.Destroy()

    def cancel_click(self, event):
        self.Destroy()

    def change_data(self):
        data = self.data
        self.setting[data.sk_mash_match][0] = self.m_textCtrl_mesh_first.GetValue()
        self.setting[data.sk_mash_match][1] = self.m_textCtrl_mesh_second.GetValue()

        self.setting[data.sk_texture_match][0] = self.m_textCtrl_tex_first.GetValue()
        self.setting[data.sk_texture_match][1] = self.m_textCtrl_tex_second.GetValue()

        with open(os.path.join(self.path, "core\\assets\\height_setting.json"), 'w')as file:
            json.dump(self.setting, file, indent=4)

    def get_setting(self):
        return self.setting

    def get_names(self):
        return self.names
