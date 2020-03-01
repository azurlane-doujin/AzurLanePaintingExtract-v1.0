import os
import threading

import wx

from core.src.static_classes.image_deal import ImageWork
from core.src.structs_classes.extract_structs import PerInfo


class QuickRestore(threading.Thread):

    def __init__(self, info: PerInfo, father=None, work_path='', full=None,
                 back=2, size=tuple, bitmap_show=None, info_show=None):
        threading.Thread.__init__(self)

        self.info = info
        self.father = father
        if father is None:
            self.size = size
            self.bitmap_show = bitmap_show
            self.info_show = info_show
        else:
            self.size = tuple(self.father.m_scrolledWindow2.GetSize())
            self.bitmap_show = self.father.m_bitmap_show
            self.info_show = self.father.m_staticText_info

        self.path = work_path
        self.full = full

        self.back = back

    def run(self):
        try:
            if not os.path.isfile(self.info.tex_path):
                info_str = f"{self.info.cn_name}:无法预览"
            else:
                size = self.size
                if self.info.get_is_able_work():
                    pic, pic_size = ImageWork.restore_tool_no_save(self.info.mesh_path, self.info.tex_path, size)
                    info_str = f"可还原立绘预览：{self.info.cn_name}；尺寸：{pic_size}"
                elif self.info.lay_in != '':
                    pic, pic_size = ImageWork.pic_transform(self.info.lay_in, size)
                    info_str = f"导出目标同名文件预览：{self.info.cn_name}；尺寸：{pic_size}"
                else:
                    pic, pic_size = ImageWork.pic_transform(self.info.tex_path, size)
                    info_str = f"原始文件预览：{self.info.cn_name}；尺寸：{pic_size}"

                self.bitmap_show.ClearBackground()
                temp = wx.Bitmap.FromBufferRGBA(pic.width, pic.height, pic.tobytes())
                self.bitmap_show.SetBitmap(temp)

            self.info_show.SetLabel(info_str)

        except RuntimeError as info:
            # self.father.append_error(info)
            print(info)
            raise

    #     if self.father.any_error():
    #         self.father.m_notebook_info.SetSelection(2)
