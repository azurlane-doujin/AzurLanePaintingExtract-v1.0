import os

import wx

from core.src.frame_classes.design_frame import DialogSpiltSprite
from core.src.static_classes.image_deal import ImageWork
from core.src.structs_classes.drop_order import SpriteDropOrder


class SpriteSplitFrame(DialogSpiltSprite):
    def __init__(self, parent, target):
        super(SpriteSplitFrame, self).__init__(parent)
        self.target = target

        self.file_list = []
        self.image_group = {}

        self.drop_order = SpriteDropOrder(self.call_back)
        self.m_listBox_in_files.SetDropTarget(self.drop_order)

        self.m_staticText_name.SetLabel(f"目标=>{target.cn_name}")

        self.show_size = tuple(self.m_bitmap_show.GetSize())

        self.now_index = -1
        self.is_selected = False

        self.text_type = 0
        self.json_type = 1

        self.select = self.m_choice_dump_type.GetSelection()

    def call_back(self, files):
        try:
            self.image_group.clear()
            self.file_list.clear()
            self.m_listBox_in_files.Clear()
            id_num: str = self.m_textCtrl_id.GetValue()
            if id_num == "":
                wx.MessageBox("无效的path_ID，将切割所有导入对象，这可能产生错误的切割结果", "信息", wx.ICON_INFORMATION)
            self.select = self.m_choice_dump_type.GetSelection()
            if self.select == self.text_type:
                end_key = ".txt"
            else:
                end_key = '.json'
            files = list(
                filter(lambda temp_value: temp_value.endswith(end_key), files))

            self.image_group, match = ImageWork.spilt_sprite(self.target, files, id_num.strip(), self.select)
            self.file_list = list(self.image_group.keys())

            self.m_listBox_in_files.Set(self.file_list)
            self.m_staticText_info.SetLabel(f"完成导入{len(files)}个文件(其中{match}个符合Path_ID且读取成功)")
        except Exception as info:
            wx.MessageBox(f"导入时出错！\n{info}", "错误", wx.ICON_ERROR)
            return False
        else:
            return True

    def view_pic(self, event):
        self.is_selected = True
        index = event.GetSelection()
        target_name = self.file_list[index]
        self.now_index = index
        target_image = self.image_group[target_name]

        show_image, size = ImageWork.pic_size_transform(target_image, self.show_size, True)

        ImageWork.show_in_bitmap_contain(show_image, self.m_bitmap_show)
        self.m_staticText_info.SetLabel(f"当前正在预览【{target_name}】,尺寸：{size}")

    def save_all(self, event):
        if self.is_selected:
            choice = ["保存当前预览", "保存全部"]
            dialog = wx.SingleChoiceDialog(self, "选择保存类型", "保存", choice)
            if wx.ID_OK == dialog.ShowModal():
                return_data = dialog.GetSelection()
                if return_data == 1:
                    dialog = wx.DirDialog(self, "选择保存目录（保存全部）", os.getcwd(),
                                          wx.DD_DIR_MUST_EXIST | wx.DD_CHANGE_DIR | wx.DD_NEW_DIR_BUTTON)
                    if dialog.ShowModal() == wx.ID_OK:
                        path = dialog.GetPath()
                        for name, pic in self.image_group.items():
                            pic.save(os.path.join(path, f"{name}.png"))
                elif return_data == 0:
                    dialog = wx.FileDialog(self, f"选择保存路径（保存【{self.file_list[self.now_index]}】）",
                                           os.getcwd(), f"{self.file_list[self.now_index]}.png",
                                           "*.png",
                                           wx.FD_SAVE | wx.FD_OVERWRITE_PROMPT | wx.FD_CHANGE_DIR | wx.FD_CHANGE_DIR)
                    if dialog.ShowModal() == wx.ID_OK:
                        path = dialog.GetPath()
                        target = self.file_list[self.now_index]
                        pic = self.image_group[target]
                        pic.save(path)
        else:
            dialog = wx.DirDialog(self, "选择保存目录(保存全部)", os.getcwd(),
                                  wx.DD_DIR_MUST_EXIST | wx.DD_CHANGE_DIR | wx.DD_NEW_DIR_BUTTON)
            if dialog.ShowModal() == wx.ID_OK:
                path = dialog.GetPath()
                for name, pic in self.image_group.items():
                    pic.save(os.path.join(path, f"{name}.png"))

        self.m_staticText_info.SetLabel(f"完成!")

    def clear_ID(self, event):
        self.m_textCtrl_id.Clear()
