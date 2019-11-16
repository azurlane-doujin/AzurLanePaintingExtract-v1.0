import os
import re
from threading import Thread

import wx
from PIL import Image

from core.src.static_classes.image_deal import ImageWork
from core.src.structs_classes.drop_order import FaceDragOrder
from core.src.structs_classes.extract_structs import PerInfo
from core.src.thread_classes.quick_view import QuickRestore
from .design_frame import MyDialogAddFace


class FaceMatchFrame(MyDialogAddFace):
    def __init__(self, parent, target: PerInfo):
        super(FaceMatchFrame, self).__init__(parent)
        # 目标对象和导入的表情
        self.target = target
        self.input_values = {}
        # self.face_file_group = {}
        self.view_list = []
        self.is_all_only = True

        # 生成目标立绘
        self.target_img = ImageWork.az_paint_restore(target.mesh_path, target.tex_path)
        self.target_size = self.target_img.size
        # 目标表情
        self.target_face = Image.Image()
        # 主图片显示区尺寸
        self.main_view_w, self.main_view_h = list(self.m_bitmap_main_view.GetSize())
        # 背景画布
        self._bg_size = self.target_size
        self.bg_paint = Image.new("RGBA", self.bg_size, (0, 0, 0, 255))
        # 立绘位于背景画布位置
        self.target_paint_x = 0
        self.target_paint_y = 0
        # 背景画布尺寸扩展
        self._top_extend = 0
        self._left_extend = 0
        self._right_extend = 0
        self._button_extend = 0
        # 表情坐标
        self._pos_x = 0
        self._pos_y = 0
        # 相对显示区坐标
        self.pos_x_a = 0
        self.pos_y_a = 0
        # 画布显示区域左上角坐标
        self._target_x = 0
        self._target_y = 0
        # 表情选择
        self.select_index = -1
        self.select_count = 0
        # 表情导入
        self.drop_order = FaceDragOrder(self, self.callback)
        self.m_listBox_import_face.SetDropTarget(self.drop_order)
        # 预览图生成器
        self.view_work = ...
        # 步长
        self.step = 1
        self.save_path = ""

        self.m_bitmap_main_view.SetDoubleBuffered(True)

    # 背景扩展处理
    @property
    def bg_size(self):
        return self._bg_size

    @bg_size.setter
    def bg_size(self, value):
        if len(value) == 2:
            self._bg_size = value
            self.bg_paint = Image.new("RGBA", self.bg_size, (0, 0, 0, 0))
            self.bg_paint.paste(self.target_img, (self.target_paint_x, self.target_paint_y))
            self.bg_paint.paste(self.target_face, (self.pos_x, self.pos_y))

    # 换头坐标处理
    @property
    def pos_x(self):
        return self._pos_x

    @pos_x.setter
    def pos_x(self, value):
        value = int(value)
        if value < 0:
            self.left_extend = -value
            value = 0
            self.m_staticText_info.SetLabel(f"画布向左扩展{self.left_extend}像素")
        elif value + self.target_face.width - self.target_size[0] > 0:
            self.right_extend = value + self.target_face.width - self.target_size[0]
            value = self.target_size[0] - self.target_face.width
            self.m_staticText_info.SetLabel(f"画布向右扩展{self.right_extend}像素")

        self._pos_x = value
        self.add_face()

    @property
    def pos_y(self):
        return self._pos_y

    @pos_y.setter
    def pos_y(self, value):
        value = int(value)
        if value < 0:
            self.top_extend = -value
            value = 0
            self.m_staticText_info.SetLabel(f"画布向上扩展{self.top_extend}像素")
        elif value + self.target_face.height - self.target_size[1] > 0:
            self.button_extend = value + self.target_face.height - self.target_size[1]
            value = self.target_size[1] - self.target_face.height
            self.m_staticText_info.SetLabel(f"画布向下扩展{self.button_extend}像素")
        self._pos_y = value
        self.add_face()

    # 画布坐标处理
    @property
    def target_x(self):
        return str(self._target_x)

    @target_x.setter
    def target_x(self, value):
        if value < 0:
            value = 0
        if value + self.main_view_w > self.bg_size[0]:
            value = self.bg_size[0] - self.main_view_w
        self._target_x = value
        # self.pos_x += value - self.main_view_w
        self.paint_move(self._target_x, self._target_y)

    @property
    def target_y(self):
        return str(self._target_y)

    @target_y.setter
    def target_y(self, value):
        if value < 0:
            value = 0
        if value + self.main_view_h > self.bg_size[1]:
            value = self.bg_size[1] - self.main_view_h
        self._target_y = value
        # self.pos_y += value - self.main_view_h
        self.paint_move(self._target_x, self._target_y)

    # 画布扩展处理
    @property
    def top_extend(self):
        return self._top_extend

    @property
    def left_extend(self):
        return self._left_extend

    @property
    def right_extend(self):
        return self._right_extend

    @property
    def button_extend(self):
        return self._button_extend

    @top_extend.setter
    def top_extend(self, value):
        self.target_paint_y += value
        self.bg_size = (self.bg_size[0], self.bg_size[1] + value)
        self._top_extend += value

    @left_extend.setter
    def left_extend(self, value):
        self.target_paint_x += value
        self.bg_size = (self.bg_size[0] + value, self.bg_size[1])
        self._left_extend += value

    @right_extend.setter
    def right_extend(self, value):
        self.bg_size = (self.bg_size[0] + value, self.bg_size[1])
        self._right_extend += value

    @button_extend.setter
    def button_extend(self, value):
        self.bg_size = (self.bg_size[0], self.bg_size[1] + value)
        self._button_extend += value

    def callback(self, values, is_all_only):
        self.input_values = values
        self.view_list = list(values.keys())
        self.m_listBox_import_face.Clear()
        self.m_listBox_import_face.Set(self.view_list)
        self.is_all_only = is_all_only

        if self.view_list:
            self.m_panel7.Enable(True)

        # for key in values.keys():
        #    value = values[key]
        #    temp = []
        #    for each in value:
        #        if os.path.isfile(each):
        #            pic = Image.open(each)
        #            temp.append(pic)
        #    self.face_file_group[key] = temp

    def paint_move(self, target_x, target_y):

        pic = self.bg_paint.crop((target_x, target_y, self.main_view_w + target_x, self.main_view_h + target_y))

        temp = wx.Bitmap.FromBufferRGBA(pic.width, pic.height, pic.tobytes())
        self.m_bitmap_main_view.ClearBackground()
        self.m_bitmap_main_view.SetBitmap(temp)

    def add_face(self):
        self.bg_paint = Image.new("RGBA", self.bg_size, (0, 0, 0, 0))
        self.bg_paint.paste(self.target_img, (self.target_paint_x, self.target_paint_y))
        self.bg_paint.paste(self.target_face, (self.pos_x, self.pos_y))
        self.paint_move(self._target_x, self._target_y)

    def export_all(self):
        bg_size = self.bg_size
        pos = (self.pos_x, self.pos_y)
        target_pos = (self.target_paint_x, self.target_paint_y)
        face_size = self.target_face.size
        save_path = self.save_path
        name = self.target.cn_name
        target_img = self.target_img

        os.makedirs(save_path, exist_ok=True)

        for key, values in self.input_values.items():
            count = 0
            for value in values:
                count += 1
                temp = Image.open(value)
                if temp.size == face_size:
                    pic = Image.new("RGBA", bg_size, 0)
                    pic.paste(target_img, target_pos)
                    pic.paste(temp, pos)
                    path = os.path.join(save_path, f"{name}-{key}-{count}.png")

                    self.m_staticText_info.SetLabel(f"正在接头：{name}-{key}-{count}")
                    pic.save(path)
                else:
                    continue
        self.m_staticText_info.SetLabel(f"接头完成")

    def initial(self, event):
        self.bg_paint.paste(self.target_img, (0, 0))
        self.paint_move(0, 0)

        self.m_panel7.Enable(False)

        # self.m_bitmap_main_view.SetSize(*self.target_size)
        # self.view_work = QuickRestore(self.target, None,
        #                              size=tuple(self.target_size),
        #                              bitmap_show=self.m_bitmap_main_view,
        #                              info_show=self.m_staticText_info)
        # self.view_work.start()
        # self.m_scrolledWindow2.Update()

    def select_face(self, event):
        index = event.GetSelection()
        values = self.input_values[self.view_list[index]]
        if index == self.select_index:
            if self.select_count < len(values) - 1:
                self.select_count += 1
            else:
                self.select_count = 0
        else:
            self.select_index = index
            self.select_count = 0

        guid = values[self.select_count]
        temp = PerInfo(f"{self.view_list[index]}-{self.select_count}",
                       f"{self.view_list[index]}-{self.select_count}",
                       False)
        temp.tex_path = guid

        self.view_work = QuickRestore(temp, None,
                                      size=tuple(self.m_panel_face.GetSize()),
                                      bitmap_show=self.m_bitmap_face,
                                      info_show=self.m_staticText_info)
        self.view_work.start()

        self.m_notebook_info.SetSelection(2)

        self.target_face = Image.open(guid)
        self.add_face()

    @staticmethod
    def value_check(event):
        """

        :param event:
        :return: if OK return True or return False
        """
        value = event.GetString()
        temp = re.sub(r'[^0-9\-]', "", value)
        temp.replace(".", "")
        temp.replace("-", "-0")
        # temp = re.sub(r'^-', "", temp)
        # temp = re.sub(r'\.\d+$', "", temp)
        if temp != value or temp == "":
            return False, temp
        else:
            return True, temp

    def value_check_x(self, event):
        is_ok, value = self.value_check(event)
        self.pos_x = value
        if not is_ok:
            # self.m_textCtrl_x_value.Clear()
            self.m_textCtrl_x_value.SetLabel(self.pos_x)
        else:
            pass

    def value_check_y(self, event):
        is_ok, value = self.value_check(event)
        self.pos_y = value
        if not is_ok:
            # self.m_textCtrl_y_value.Clear()
            self.m_textCtrl_y_value.SetLabel(self.pos_y)
        else:
            pass

    def value_check_px(self, event):
        is_ok, value = self.value_check(event)
        self.target_x = int(value)
        if not is_ok or value != self.target_x:
            # self.m_textCtrl_pic_x.Clear()
            self.m_textCtrl_pic_x.SetLabel(self.target_x)
        else:
            pass

    def value_check_py(self, event):
        is_ok, value = self.value_check(event)
        self.target_y = int(value)
        if not is_ok or value != self.target_y:
            # self.m_textCtrl_pic_y.Clear()
            self.m_textCtrl_pic_y.SetLabel(self.target_y)
        else:
            pass

    def wheel_x(self, event):
        angle = event.GetWheelRotation()
        guide = -angle // abs(angle)
        self.pos_x = self.pos_x + guide * self.step
        self.m_textCtrl_x_value.SetLabel(str(self.pos_x))

    def y_wheel(self, event):
        angle = event.GetWheelRotation()
        guide = -angle // abs(angle)
        self.pos_y = self.pos_y + guide * self.step
        self.m_textCtrl_y_value.SetLabel(str(self.pos_y))

    def px_wheel(self, event):
        angle = event.GetWheelRotation()
        guide = -angle // abs(angle)
        self.target_x = self._target_x + guide * self.step
        self.m_textCtrl_pic_x.SetLabel(self.target_x)

    def py_wheel(self, event):
        angle = event.GetWheelRotation()
        guide = -angle // abs(angle)
        self.target_y = self._target_y + guide * self.step
        self.m_textCtrl_pic_y.SetLabel(self.target_y)

    def set_step(self, event):
        value = event.GetString()
        self.step = int(value)

    def on_erase(self, event):
        pass

    def export(self, event):
        dialog = wx.SingleChoiceDialog(self, "选择导出类型", "选择导出类型", ("仅导出当前表情组合", "导出全部相同尺寸表情组合"))
        if dialog.ShowModal() == wx.ID_OK:
            select = dialog.GetSelection()
            if select == 1:
                dialog = wx.FileDialog(self, f"导出{self.target.cn_name}-{self.select_index}表情组合", "./"
                                       , f"{self.target.cn_name}-{self.select_index}.png",
                                       style=wx.FD_SAVE | wx.FD_OVERWRITE_PROMPT)
                if dialog.ShowModal() == wx.ID_OK:
                    path = dialog.GetPath()
                    self.bg_paint.save(path)
            else:

                dialog = wx.DirDialog(self, "导出文件夹", "./",
                                      wx.DD_NEW_DIR_BUTTON | wx.DD_CHANGE_DIR | wx.DD_DEFAULT_STYLE)
                if dialog.ShowModal() == wx.ID_OK:
                    self.save_path = dialog.GetPath()
                    thread = Thread(target=self.export_all)

                    thread.start()
