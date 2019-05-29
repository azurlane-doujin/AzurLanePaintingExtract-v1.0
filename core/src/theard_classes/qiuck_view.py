import os
import threading
import time

import wx

from core.src.frame_classse.design_frame import MainFrame
from core.src.static_classes.image_deal import ImageWork
from core.src.struct_classes.extect_struct import PerInfo


class QuickRestore(threading.Thread):

    def __init__(self, info: PerInfo, father: MainFrame = None, work_path='', full=None,
                 back=2):
        threading.Thread.__init__(self)

        self.info = info
        self.father = father

        self.path = work_path
        self.full = full

        self.back = back

    def run(self):
        try:
            size = tuple(self.father.m_bitmap_show.GetSize())
            if self.info.is_able_work:
                pic = ImageWork.restore_tool_no_save(self.info.mesh_path, self.info.tex_path, size)
            elif self.info.lay_in != '':
                pic = ImageWork.pic_transform(self.info.lay_in, size)
            else:
                pic = ImageWork.pic_transform(self.info.tex_path, size)

            self.father.m_bitmap_show.ClearBackground()

            # temp = self.pil_to_wx_image(pic)


            pic.save("%s\\temp.png" % self.path)
            time.sleep(0.5)
            temp = wx.Image('%s\\temp.png' % self.path, wx.BITMAP_TYPE_PNG)
            temp = wx.Bitmap(temp)

            self.father.m_bitmap_show.SetBitmap(temp)


            # time.sleep(3)
            # if
            # self.father.m_notebook_info.SetSelection(self.back)
           # if self.full["auto_open"] and False:
           #     os.system(r'start ' + "\"%s\\temp.png\"" % self.path)

        except RuntimeError as info:
            # self.father.append_error(info)
            print(info)
            raise

  #     if self.father.any_error():
  #         self.father.m_notebook_info.SetSelection(2)

    @staticmethod
    def pil_to_wx_image(pic):
        has_alpha = pic.mode[-1].lower() == "a"
        if has_alpha:

            temp: wx.Image = wx.Image(pic.width, pic.height)

            temp_rgba = pic.copy()
            temp_rgb = temp_rgba.convert('RGB')

            rgb_data = temp_rgb.tobytes()
            temp.SetData(rgb_data)
            temp.SetAlphaBuffer(temp_rgba.tobytes()[3::4])

        else:
            temp: wx.Image = wx.Image(pic.width, pic.height)

            temp_rgb = pic.copy()
            temp_rgb = temp_rgb.convert('RGB')

            rgb_data = temp_rgb.tobytes()
            temp.SetData(rgb_data)

        return temp