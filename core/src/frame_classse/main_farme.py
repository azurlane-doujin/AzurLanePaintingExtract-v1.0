import json
import os
import shutil
import sys
import time

import wx

from core.src.frame_classse.design_frame import MainFrame as Mf
from core.src.frame_classse.setting_farme import Setting
from core.src.static_classes.file_read import FileFilter
from core.src.static_classes.search_order import SearchOrder
from core.src.static_classes.static_data import GlobalData
from core.src.struct_classes.drag_order import DragOrder
from core.src.struct_classes.extect_struct import PerWorkList
from core.src.theard_classes.extract_thead import RestoreThread
from core.src.theard_classes.qiuck_view import QuickRestore


class MainFrame(Mf):
    """
    主窗口类
    """

    def __init__(self, parent, path=os.getcwd()):
        super(MainFrame, self).__init__(parent)

        # 舰娘名称文件
        self.names = {}
        with open(os.path.join(path, "core\\assets\\names.json"), "r")as file:
            self.names = json.load(file)
        # 设置文件
        with open(os.path.join(path, "core\\assets\\setting.json"), 'r')as file:
            self.setting_info = json.load(file)

        self.root = self.m_treeCtrl_info.AddRoot(u"碧蓝航线")
        # 数据储存结构实例
        self.painting_work = PerWorkList()
        self.view_work = PerWorkList()
        # 查找tree索引的信息
        self.pos, self.type_is, self.name = None, None, None
        # 设置拖动绑定
        self.drop = DragOrder(self.painting_work, self.view_work, self)
        self.m_treeCtrl_info.SetDropTarget(self.drop)
        # 立绘还原线程
        self.thread_quick = None
        self.thread_main = None
        # 进入退出状态
        self.enter_exit = False
        # 保存路径，脚本路径
        self.save_path = ""
        self.work_path = path
        # 之窗口（只有一个）
        self.__dialog = None
        # ，搜索，筛选器
        self.search_type = False
        self.filter_type = False
        # 常参储存类
        self.data = GlobalData()

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
        """
        修改指向文件方法
        :param pos: tree中选择类型（单个，列表中文件）
        :param type_is: 选中类型 （tex,mesh）
        :param target: 指向目标方法 type：PerInfo
        :return: Null
        """
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
        """
        重置还原线程
        :return:
        """
        self.thread_main = RestoreThread(1, 'restore', self.painting_work.build_able(),
                                         self.painting_work.build_unable(), self, self.setting_info,
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

        if self.setting_info[self.data.sk_finish_exit]:
            self.exit()

    def export_all(self, path, for_work: PerWorkList = None):
        data = self.data

        if self.setting_info[data.sk_make_new_dir]:
            path += r"\碧蓝航线-导出"

        os.makedirs(path, exist_ok=True)

        self.restart()
        self.save_path = path
        self.m_gauge_state.SetValue(0)

        if isinstance(for_work, PerWorkList):
            able = for_work.build_able()
        else:
            able = self.painting_work.build_able()

        # 跳过已经存在的处理
        if self.setting_info[data.sk_skip_exist]:
            target_path_list = FileFilter.all_file(path)

            skip = able.build_skip(target_path_list)
            able = able.remove(skip)

        # 启动线程
        self.thread_main.add_save_path(self.save_path)
        self.thread_main.update_value(able, for_work.build_unable())
        if self.thread_main.is_alive():
            self.thread_main.stop_(True)
            while self.thread_main.is_alive():
                time.sleep(1)
            self.thread_main.start()
        else:
            self.thread_main.start()

    def copy_file(self):
        data = self.data
        self.__dialog = wx.DirDialog(self, "保存", os.getcwd(),
                                     style=wx.DD_DIR_MUST_EXIST | wx.DD_CHANGE_DIR | wx.DD_NEW_DIR_BUTTON
                                           | wx.DD_DEFAULT_STYLE)
        if self.__dialog.ShowModal() == wx.ID_OK:
            unable = self.painting_work.build_unable()
            path = self.__dialog.GetPath()
            if self.setting_info[data.sk_output_group] == data.feg_by_type:
                path += "\\拷贝"
            num = 0
            self.m_gauge_state.SetValue(0)
            for name in unable:
                num += 1
                name.add_save(path)
                shutil.copyfile(name.tex_path, name.save_path)

                self.m_gauge_state.SetValue(round(100 * (num / len(unable))))

        if self.setting_info[data.sk_open_output_dir]:
            os.system(r'start "%s"' % self.save_path)
        if self.setting_info[data.sk_finish_exit]:
            self.exit()

    # 以下为回调函数
    def on_info_select(self, event):
        if not self.enter_exit:
            self.m_button_change.Enable(False)
            val = event.GetItem()

            if not self.search_type and not self.filter_type:
                is_ok, name = self.painting_work.find_by_id(val)
            else:
                is_ok, name = self.view_work.find_by_id(val)
            if is_ok:
                self.m_staticText_info.SetLabel(f"选择：{name.cn_name}")

                self.thread_quick = QuickRestore(name, self)
                self.thread_quick.start()
            # 寻找tex或mesh路径句柄
            else:
                if not self.search_type and not self.filter_type:
                    is_ok, pos, type_is, index, name = self.painting_work.find_in_each(val)
                else:
                    is_ok, pos, type_is, index, name = self.view_work.find_in_each(val)
                if is_ok:
                    pass
                # 显示图片，如果可以
                if is_ok:
                    # 可用修改
                    self.m_button_change.Enable(True)
                    self.pos, self.type_is, self.name = pos, type_is, name

                    is_able, value = name.build_sub(pos, type_is, index)
                    if is_able:
                        self.thread_quick = QuickRestore(value, self)
                        self.thread_quick.start()
                        is_able = "可预览"
                    else:
                        is_able = "不可预览"

                    if pos:
                        pos = "单个类型"
                    else:
                        pos = "列表"
                    if type_is:
                        type_is = "texture文件"
                    else:
                        type_is = "mesh文件"

                    self.m_staticText_info.SetLabel(
                        f"选择： {name.cn_name}中的{pos}{type_is}: {self.m_treeCtrl_info.GetItemText(val)}，{is_able}")

    def choice_file(self, event):
        self.change_path(self.pos, self.type_is, self.name)

        self.thread_quick = QuickRestore(self.name, self)
        self.thread_quick.run()

    def work(self, event):
        data = self.data
        show = ["导出全部可还原", "拷贝全部不可还原", "导出选择项", "导出当前列表项"]
        if len(self.painting_work.build_able()) == 0:
            show[data.et_all] += "（不可用）"
        if len(self.painting_work.build_unable()) == 0:
            show[data.et_copy_only] += "（不可用）"
        if self.name is None:
            show[data.et_select] += "（不可用）"
        if self.filter_type or self.search_type:
            if self.view_work.__len__() == 0:
                show[data.et_list_item] += "（不可用）"
        else:
            if len(self.painting_work) == 0:
                show[data.et_list_item] += "（不可用）"

        self.__dialog = wx.SingleChoiceDialog(self, "选择类型", "选择导出类型", show)

        if self.__dialog.ShowModal() == wx.ID_OK:
            index = self.__dialog.GetSelection()
            if index == data.et_all:
                if len(self.painting_work.build_able()) == 0:
                    wx.MessageBox("不可用！", "错误")
                    return

                title = '保存'
                title += "-碧蓝航线"

                address = os.getcwd()
                dialog = wx.DirDialog(self, title, address, style=wx.DD_DEFAULT_STYLE | wx.DD_NEW_DIR_BUTTON)

                if dialog.ShowModal() == wx.ID_OK:
                    temp = dialog.GetPath()

                    if self.painting_work.build_able().__len__() > 0:
                        self.export_all(temp, self.painting_work)

            if index == data.et_copy_only:
                if len(self.painting_work.build_unable()) == 0:
                    wx.MessageBox("不可用！！", "错误")
                    return
                self.copy_file()
            if index == data.et_select:
                if self.name is None:
                    wx.MessageBox("不可用！！", "错误")
                    return

                self.export_choice()
            if index == data.et_list_item:

                if self.filter_type or self.search_type:
                    if self.view_work.__len__() == 0:
                        wx.MessageBox("不可用！！", "错误")
                        return
                else:
                    if len(self.painting_work) == 0:
                        wx.MessageBox("不可用！！", "错误")
                        return

                title = '保存'
                title += "-碧蓝航线"

                address = os.getcwd()
                dialog = wx.DirDialog(self, title, address, style=wx.DD_DEFAULT_STYLE | wx.DD_NEW_DIR_BUTTON)

                if dialog.ShowModal() == wx.ID_OK:
                    temp = dialog.GetPath()

                    if self.painting_work.build_able().__len__() > 0:
                        self.export_all(temp, self.view_work)

    def filter_work(self, event):
        index = event.GetSelection()
        value = self.data.fp_pattern_group[index]

        if index == self.data.tf_all:
            self.filter_type = False

            self.enter_exit = True
            self.m_treeCtrl_info.DeleteChildren(self.root)
            self.painting_work.show_in_tree(self.m_treeCtrl_info, self.root)
            self.enter_exit = False
        else:
            if self.search_type:
                self.view_work = self.view_work.build_from_pattern(value)
            else:
                self.view_work = self.painting_work.build_from_pattern(value)

            self.filter_type = True

            self.enter_exit = True
            self.m_treeCtrl_info.DeleteChildren(self.root)
            self.view_work.show_in_tree(self.m_treeCtrl_info, self.root)
            self.enter_exit = False

    def search(self, event):
        if event is None:
            value = self.m_searchCtrl1.GetValue()
        else:
            value = event.GetString()

        if value != '':
            if not self.filter_type:
                indexes = SearchOrder.find(value, self.painting_work.build_search())
                self.view_work = self.painting_work.build_from_indexes(indexes)
            else:
                indexes = SearchOrder.find(value, self.view_work.build_search())
                self.view_work = self.view_work.build_from_indexes(indexes)

            self.search_type = True

            self.enter_exit = True
            self.m_treeCtrl_info.DeleteChildren(self.root)
            self.view_work.show_in_tree(self.m_treeCtrl_info, self.root)
            self.enter_exit = False
        else:
            self.search_type = False

            self.enter_exit = True
            self.m_treeCtrl_info.DeleteChildren(self.root)
            self.painting_work.show_in_tree(self.m_treeCtrl_info, self.root)
            self.enter_exit = False

    def setting(self, event):
        self.__dialog = Setting(self, self.setting_info, self.work_path)

        self.__dialog.ShowModal()

        self.setting_info = self.__dialog.get_setting()

    def exit(self, event=None):
        self.enter_exit = True
        self.m_treeCtrl_info.DeleteAllItems()
        self.m_treeCtrl_info.Destroy()
        self.Destroy()
        sys.exit()
