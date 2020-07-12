import json
import os

from core.src.frame_classes.design_frame import MyDialogHeightSetting
from core.src.frame_classes.location_update import LocationUpdate
from core.src.frame_classes.names_edit_frame import NamesEditFrame
from core.src.static_classes.static_data import GlobalData


class LevelSettingFrame(MyDialogHeightSetting):
    def __init__(self, parent, height_setting, names, work_path):
        super(LevelSettingFrame, self).__init__(parent)
        self.setting = height_setting
        self.names = names
        self.frame = parent
        self.path = work_path
        self.data = GlobalData()

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

    # answer=wx.MessageBox("即将开始更新，确认？", "信息", wx.ICON_INFORMATION|wx.YES_NO)
    # if answer==wx.YES:
    #     try:
    #         r=requests.get(
    #             "https://raw.githubusercontent.com/OSSSY152/AzurLanePaintingLocalization/master/chs/names.json",
    #             timeout=100)
    #         if r.status_code==200:
    #             overwrite=0
    #             new_item=0
    #             temp_names=self.names
    #             keys=list(temp_names.keys())
    #             new=json.loads(r.text)
    #             temple=new
    #             for key, item in temple.items():
    #                 temp_names[key] = item
    #                 if key in keys:
    #                     overwrite += 1
    #                 else:
    #                     new_item += 1

    #             self.names=temp_names
    #             with open(os.path.join(self.path, "core\\assets\\names.json"), "w")as file:
    #                 json.dump(temp_names, file, indent=4)

    #             wx.MessageBox(f"导入键值对文件成功！\n\t覆盖：{overwrite}\n\t新增：{new_item}", "信息")
    #     except Exception as info:
    #         wx.MessageBox(f"导入键值对文件出现错误！\n{info.__str__()}")

    def edit_names(self, event):
        dialog = NamesEditFrame(self, self.names, self.path)
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

        with open(os.path.join(os.getcwd(), "core\\assets\\height_setting.json"), 'w')as file:
            json.dump(self.setting, file, indent=4)

    def get_setting(self):
        return self.setting

    def get_names(self):
        return self.names
