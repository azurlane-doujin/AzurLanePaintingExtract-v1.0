import os
import re

import wx
from PIL import Image

from core.src.frame_classes.design_frame import MyDialogAtlasSpilt
from core.src.static_classes.image_deal import ImageWork
from core.src.structs_classes.drop_order import AtlasDropOrder
from core.src.structs_classes.extract_structs import PerInfo
from core.src.thread_classes.quick_view import QuickRestore


class AtlasSpiltFrame(MyDialogAtlasSpilt):
    def __init__(self, parent, target):
        super(AtlasSpiltFrame, self).__init__(parent)
        self.target: PerInfo = target
        self.atlas_path = ''
        self.items = {}
        self.names = []

        self.show_thread: QuickRestore = ...

        self.drop_order = AtlasDropOrder(self, self.drop_path)
        self.m_filePicker_target_atlas.SetDropTarget(self.drop_order)

        self.bg_size = tuple(self.m_bitmap_show.GetSize())

        self.m_staticText_target_name.SetLabel(f'目标名称：{self.target.cn_name}')

        self.dialog = ...

    def split_work(self):
        img = Image.open(self.target.tex_path)
        self.items = ImageWork.atlas_split_main(img, atlas_file=self.atlas_path)
        self.names = list(self.items.keys())
        self.m_listBox_spilt_items.Clear()
        self.m_listBox_spilt_items.Set(self.names)

    def drop_path(self, path):
        self.m_filePicker_target_atlas.SetPath(path)
        self.atlas_path = path
        self.split_work()

    def load_atlas(self, event, ):
        self.atlas_path = event.GetPath()
        self.split_work()

    def view_item(self, event):
        index = event.GetSelection()
        pic = self.items[self.names[index]]
        img, size = ImageWork.pic_size_transform(pic, self.bg_size, False)

        temp = wx.Bitmap.FromBufferRGBA(img.width, img.height, img.tobytes())
        self.m_bitmap_show.ClearBackground()
        self.m_bitmap_show.SetBitmap(temp)

        self.m_staticText_info.SetLabel(f"当前正在显示{self.target.cn_name}->{self.names[index]}")

    def save_item(self, event):
        index = event.GetSelection()
        pic = self.items[self.names[index]]

        self.dialog = wx.FileDialog(self, f"保存组件“{self.names[index]}”", defaultFile=f"{self.names[index]}.png",
                                    wildcard="*.png",
                                    style=wx.FD_CHANGE_DIR | wx.FD_SAVE | wx.FD_OVERWRITE_PROMPT)
        if wx.ID_OK == self.dialog.ShowModal():
            path = self.dialog.GetPath()
            pic.save(path)

    def save_all(self, event):
        self.dialog = wx.DirDialog(self, f"保存组件“{self.target.cn_name}”",
                                   style=wx.DD_CHANGE_DIR | wx.DD_DIR_MUST_EXIST | wx.DD_NEW_DIR_BUTTON)
        if wx.ID_OK == self.dialog.ShowModal():
            path = self.dialog.GetPath()
            os.makedirs(path, exist_ok=True)
            for key in self.names:
                key = re.sub(r'[/\\?*<>:]', '-', key)
                out_path = os.path.join(path, f'{key}.png')
                self.items[key].save(out_path)

            self.m_staticText_info.SetLabel(f'完成导出，导出文件夹：{path}')
