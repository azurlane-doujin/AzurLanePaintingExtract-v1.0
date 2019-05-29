import json
import os
import shutil
import sys
import time

import wx

from core.src.frame_classse.design_frame import MainFrame as Mf
from core.src.static_classes.search_order import SearchOrder
from core.src.struct_classes.drag_order import DragOrder
from core.src.struct_classes.extect_struct import PerWorkList
from core.src.theard_classes.extract_thead import RestoreThread
from core.src.theard_classes.qiuck_view import QuickRestore


class MainFrame(Mf):
    def __init__(self, parent, path=""):
        super(MainFrame, self).__init__(parent)

        self.names = {}
        with open(os.path.join(os.getcwd(), "core\\assets\\names.json"), "r")as file:
            self.names = json.load(file)

        self.path = path
        self.root = self.m_treeCtrl_info.AddRoot(u"碧蓝航线")
        self.painting_work = PerWorkList()

        self.pos, self.type_is, self.name = None, None, None

        self.drop = DragOrder(self.painting_work, self)
        self.m_treeCtrl_info.SetDropTarget(self.drop)

        self.thread_quick = None
        self.thread_main = None

        self.enter_exit = False

        self.save_path = ""

        self.__dialog = None

        self.setting_info = {}
        self.full = {}

        self.search_info = PerWorkList()
        self.search_type = False

    @staticmethod
    def run():
        """
        运行入口函数
        :return:
        """
        app = wx.App()
        frame = MainFrame(None)

        frame.Show()

        app.MainLoop()

    # 以下为辅助函数，新增部分
    def change_path(self, pos, type_is, target):
        if pos:
            if type_is:
                dialog = wx.SingleChoiceDialog(self, "选择更改Texture文件", "选择更改文件", target.get_select(type_is))
                if dialog.ShowModal() == wx.ID_OK:
                    index = dialog.GetSelection()
                    id, data = target.set_tex(index)

                    self.m_treeCtrl_info.SetItemText(id, data)
            else:
                dialog = wx.SingleChoiceDialog(self, "选择更改Mesh文件", "选择更改文件", target.get_select(type_is))
                if dialog.ShowModal() == wx.ID_OK:
                    index = dialog.GetSelection()
                    id, data = target.set_mesh(index)

                    self.m_treeCtrl_info.SetItemText(id, data)

    # 以下为原有函数
    def restart(self):

        self.thread_main = RestoreThread(1, 'restore', self.painting_work.build_able(),
                                         self.painting_work.build_unable(), self, self.setting_info, self.full,
                                         self.names, self.save_path)

        self.m_staticText_info.SetLabel("重置还原进度！")

        self.m_gauge_state.SetValue(0)

    # export

    def export_choice(self):
        self.__dialog = wx.DirDialog(self, "保存", os.getcwd(), style=wx.DD_NEW_DIR_BUTTON)

        if self.__dialog.ShowModal() == wx.ID_OK:
            self.m_gauge_state.SetValue(0)
            self.save_path = self.__dialog.GetPath()
            self.restart()

        self.m_gauge_state.SetValue(100)

    def export_all(self, path, for_work: PerWorkList = None):
        # if self.setting["new_dir"]:
        #     path += r"\碧蓝航线-导出"

        os.makedirs(path, exist_ok=True)

        self.restart()
        self.save_path = path
        self.m_gauge_state.SetValue(0)

        if isinstance(for_work, PerWorkList):
            for_work = for_work
            for_work = for_work.build_able()
        else:
            for_work = self.painting_work.build_able()
        # if isinstance(for_work, PerWorkList):
        #    for_work = for_work
        #    for_work = for_work.build_able()
        # else:
        #    for_work = self.able
        #    for_unable = self.able

        # if self.full["skip_had"]:
        #    self.save_path_list = function.all_file_path(self.save_path)
        #
        #    self.skip = for_work.build_skip(self.save_path_list[1])
        #    able = for_work.remove(self.skip)
        #
        # else:
        able = for_work

        self.thread_main.add_save_path(self.save_path)
        self.thread_main.update_value(able, self.painting_work.build_unable())
        if self.thread_main.is_alive():
            self.thread_main.stop_(True)
            while self.thread_main.is_alive():
                time.sleep(1)
            self.thread_main.start()
        else:
            self.thread_main.start()

    def copy_file(self):
        self.__dialog = wx.DirDialog(self, "保存", os.getcwd(),
                                     style=wx.DD_DIR_MUST_EXIST | wx.DD_CHANGE_DIR | wx.DD_NEW_DIR_BUTTON
                                           | wx.DD_DEFAULT_STYLE)
        if self.__dialog.ShowModal() == wx.ID_OK:
            unable = self.painting_work.build_unable()
            path = self.__dialog.GetPath()
            num = 0
            self.m_gauge_state.SetValue(0)
            for name in unable:
                num += 1
                name.add_save(path)
                shutil.copyfile(name.tex_path, name.save_path)

                self.m_gauge_state.SetValue(round(100 * (num / len(unable))))

        # if self.full['auto_open']:
        #    os.system(r'"%s"' % self.save_path)

        # search

    # 以下为回调函数
    def on_info_select(self, event):
        if not self.enter_exit:
            self.m_button_change.Enable(False)
            val = event.GetItem()
            is_ok, name = self.painting_work.find_by_id(val)
            if is_ok:
                self.m_staticText_info.SetLabel(f"选择：{name.cn_name}")

                self.thread_quick = QuickRestore(name, self)
                self.thread_quick.start()
            # 寻找tex或mesh路径句柄
            else:
                is_ok, pos, type_is, index, name = self.painting_work.find_in_each(val)
                if is_ok:
                    pass
                # 显示图片，如果可以
                if is_ok:
                    self.m_button_change.Enable(True)
                    self.pos, self.type_is, self.name = pos, type_is, name

                if is_ok:
                    if pos:
                        pos = "单个类型"
                    else:
                        pos = "列表"
                    if type_is:
                        type_is = "texture文件"
                    else:
                        type_is = "mesh文件"

                    self.m_staticText_info.SetLabel(
                        f"选择： {name.cn_name}中的{pos}{type_is}: {self.m_treeCtrl_info.GetItemText(val)}")

    def choice_file(self, event):
        self.change_path(self.pos, self.type_is, self.name)

        self.thread_quick = QuickRestore(self.name, self)
        self.thread_quick.run()

    def work(self, event):
        show = []
        if len(self.painting_work.build_able()) != 0:
            show.append("导出全部可还原")
        else:
            show.append("")
        if len(self.painting_work.build_unable()) != 0:
            show.append("拷贝不可还原")
        else:
            show.append("")
        if self.name is not None:
            show.append("导出选择项")
        else:
            show.append("")
        self.__dialog = wx.SingleChoiceDialog(self, "选择类型", "选择导出类型", show)

        if self.__dialog.ShowModal() == wx.ID_OK:
            type_s = self.__dialog.GetStringSelection()
            index = self.__dialog.GetSelection()
            if index == 0 and type_s != "":
                title = '保存'
                title += "-碧蓝航线"

                address = os.getcwd()
                dialog = wx.DirDialog(self, title, address, style=wx.DD_DEFAULT_STYLE | wx.DD_NEW_DIR_BUTTON)

                if dialog.ShowModal() == wx.ID_OK:
                    temp = dialog.GetPath()

                    if self.painting_work.build_able().__len__() > 0:
                        self.export_all(temp, self.painting_work.build_able())

                else:
                    pass

            if index == 1 and type_s != "":
                self.copy_file()
            if index == 2 and type_s != "":
                self.export_choice()

    def filter_work(self, event):
        pass

    def search(self, event):

        value = event.GetString()

        if value != '':
            indexes = SearchOrder.find(value, self.painting_work.build_search())

            self.search_type = True

            self.search_info = self.painting_work.build_from_indexes(indexes)

            self.enter_exit = True
            self.m_treeCtrl_info.DeleteAllItems()
            self.search_info.show_in_tree(self.m_treeCtrl_info, self.root)
            self.enter_exit = False
        else:
            self.search_type = False

            self.enter_exit = True
            self.m_treeCtrl_info.DeleteAllItems()
            self.painting_work.show_in_tree(self.m_treeCtrl_info, self.root)
            self.enter_exit = False

    def setting(self, event):
        pass

    def exit(self, event):
        self.enter_exit = True
        self.m_treeCtrl_info.DeleteAllItems()
        self.m_treeCtrl_info.Destroy()
        self.Destroy()
        sys.exit()
