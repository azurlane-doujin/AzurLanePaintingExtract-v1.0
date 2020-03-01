import json
import os

import requests
import wx

from .design_frame import MyDialogUpdateLocation
from ..structs_classes.location_group import LocationList


class LocationUpdate(MyDialogUpdateLocation):
    def __init__(self, parent, names, path):
        super(LocationUpdate, self).__init__(parent)
        self.path = path
        self.names = names
        self.load_data = {}

        self.root = self.m_treeCtrl_info.AddRoot("")

        self.local_work = LocationList()

        self.available_list = (
            "https://raw.githubusercontent.com/OSSSY152/AzurLanePaintingLocalization/master/chs/names.json",)

    def compare(self):
        self.local_work = LocationList()
        self.local_work.compare(self.names, self.load_data)
        self.m_treeCtrl_info.DeleteChildren(self.root)
        self.local_work.add_to_tree(self.m_treeCtrl_info, self.root)

    def update(self, data):
        self.m_staticText_info.SetLabel("正在更新数据...")
        for key, item in data.items():
            self.names[key] = item
        with open(os.path.join(self.path, "core\\assets\\names.json"), "w")as file:
            json.dump(self.names, file)

        wx.MessageBox("完成!", "信息", wx.ICON_INFORMATION)
        self.Destroy()

    def request_info(self, event):
        index = event.GetSelection()

        def work():
            try:
                r = requests.get(self.available_list[index], timeout=1000)
                if r.status_code == 200:
                    self.load_data = json.loads(r.text)
                self.compare()
                self.m_staticText_info.SetLabel(f"加载完成！来自{event.GetString()}提供的本地化方案")
            except Exception as info:
                wx.MessageBox(f"{info.__str__()}")

        self.m_staticText_info.SetLabel(f"加载中，请稍后~~")
        work()

    def load_file(self, event):
        dialog = wx.FileDialog(self, "选择json文件", self.path, "Names.json", "*.json",
                               wx.FD_OPEN | wx.FD_CHANGE_DIR | wx.FD_PREVIEW | wx.FD_FILE_MUST_EXIST)

        if wx.ID_OK == dialog.ShowModal():
            path = dialog.GetPath()

            with open(path, "r")as file:
                data = json.load(file)
                if isinstance(data, dict):
                    self.load_data = data

            self.m_staticText_info.SetLabel("加载完成！来自本地文件")

            self.compare()

    def apply_all(self, event):
        data = self.local_work.transform_all()
        self.update(data)

    def apply_cover(self, event):
        data = self.local_work.transform_cover()
        self.update(data)

    def apply_new(self, event):
        data = self.local_work.transform_new()
        self.update(data)

    def cancel(self, event):
        self.Destroy()
