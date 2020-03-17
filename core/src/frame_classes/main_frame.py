import json
import os
import shutil
import sys
import time

import wx

from core.src.frame_classes.SpriteSpiltFrame import SpriteSplitFrame
from core.src.frame_classes.atlas_spilt_frame import AtlasSpiltFrame
from core.src.frame_classes.design_frame import MainFrame as Mf
from core.src.frame_classes.face_match_frame import FaceMatchFrame
from core.src.frame_classes.setting_frame import Setting
from core.src.static_classes.file_read import FileFilter
from core.src.static_classes.image_deal import ImageWork
from core.src.static_classes.search_order import SearchOrder
from core.src.static_classes.static_data import GlobalData
from core.src.structs_classes.drop_order import DragOrder
from core.src.structs_classes.extract_structs import PerWorkList
from core.src.thread_classes.extract_thread import RestoreThread
from core.src.thread_classes.quick_view import QuickRestore


class MainFrame(Mf):
    """
    主窗口类
    """

    def __init__(self, parent, path=os.getcwd()):
        super(MainFrame, self).__init__(parent)
        # 添加图标
        icon = wx.Icon(os.path.join(path, "core\\assets\\sf_icon.ico"))
        self.SetIcon(icon)
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
        # 查找tree索引的信息，pos->[单个true，列表中false]；type_is->类型【texture，mesh】，name->点击的位置的对象
        self.is_single, self.type_is, self.name = None, None, None
        self.index = -1
        # 设置拖动绑定
        self.drop = DragOrder(self.painting_work, self.view_work, self, self.get_input_data)
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
        # 搜索数据
        self.select_data = None

        self.frame_size = self.Size

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

    def get_input_data(self, view_work, painting_group):
        self.view_work = view_work
        self.painting_work = painting_group

    # 以下为辅助函数，新增部分
    def change_path(self, is_single, type_is, target, index):
        """
        修改指向文件方法
        :param is_single: 选中的tree中元素是否为列表外元素
        :param type_is: 选中类型 （tex,mesh）
        :param target: 指向目标方法 type：PerInfo
        :return: bool
        """
        if is_single is None: return False
        # 当选择对象为单个，而不是列表中项目（其他文件的跟标签）
        # 选择的是texture
        if type_is:
            if is_single:
                dialog = wx.SingleChoiceDialog(self, "选择更改Texture文件", "选择更改文件", target.get_select(type_is))
                if dialog.ShowModal() == wx.ID_OK:
                    index = dialog.GetSelection()
                # 重定向texture文件
            id, data = target.set_tex(index)
            self.m_treeCtrl_info.SetItemText(id, data)
        # 选择的是mesh
        else:
            if is_single:
                dialog = wx.SingleChoiceDialog(self, "选择更改Mesh文件", "选择更改文件", target.get_select(type_is))
                if dialog.ShowModal() == wx.ID_OK:
                    index = dialog.GetSelection()
                # 重定向mesh文件
            id, data = target.set_mesh(index)
            self.m_treeCtrl_info.SetItemText(id, data)

        if target.is_able():
            self.m_treeCtrl_info.SetItemTextColour(target.key, wx.Colour(253, 86, 255))
        else:

            self.m_treeCtrl_info.SetItemTextColour(target.key, wx.Colour(255, 255, 255))
        return True

    # action 响应函数
    def independent_target(self, target):
        """
        新建独立目标（新建一个和目标相同的独立对象）
        :param target: 要新建的目标
        :return: None
        """

        self.__dialog = wx.TextEntryDialog(parent=None, message='', caption="独立组合的名称",
                                           value=f"{target.name}-#{target.sub_data}", )

        is_ok = self.__dialog.ShowModal()

        if is_ok == wx.ID_OK:
            name = self.__dialog.GetValue()
            if name in self.painting_work:
                wx.MessageBox("该名称已经存在！", "错误", wx.OK | wx.ICON_ERROR)
                self.independent_target(target)
            else:
                target.independent(name, self.m_treeCtrl_info, self.root)

    def face_match_target(self, target):
        if not target.is_able_work:
            self.m_staticText_info.SetLabel("换头失败！必须是可还原对象")
            return
        self.m_staticText_info.SetLabel("开始换头！")
        self.__dialog = FaceMatchFrame(self, target)
        self.__dialog.ShowModal()

    def atlas_split_target(self, target):
        if not os.path.isfile(target.tex_path):
            self.m_staticText_info.SetLabel("切割失败，必须有一个可用Texture2D文件")
            return
        else:
            self.m_staticText_info.SetLabel("开始换头！")
            self.__dialog = AtlasSpiltFrame(self, target)
            self.__dialog.ShowModal()

    def set_able_target(self, target):
        target.transform_able()
        self.m_treeCtrl_info.DeleteChildren(target.tree_ID)
        target.append_item_tree(self.m_treeCtrl_info)
        self.m_staticText_info.SetLabel(f"{target.cn_name}已转换,现在为{target.must_able}")

    def remove_target(self, target):
        info = wx.MessageBox(f"确实要移除\n{target}\n?", '信息', wx.YES_NO | wx.ICON_INFORMATION)
        if info == wx.YES:
            self.m_treeCtrl_info.Delete(target.tree_ID)
            self.painting_work.remove([target])
            if self.search_type or self.filter_type:
                self.select_data.remove([target])

    def split_target_only(self, target):
        if not target.is_able_work:
            self.m_staticText_info.SetLabel(f"{target}无法切割，为非可还原对象")
            return
        self.__dialog = wx.DirDialog(self, "选择保存文件夹", self.work_path, wx.DD_NEW_DIR_BUTTON | wx.DD_DIR_MUST_EXIST)
        if wx.ID_OK == self.__dialog.ShowModal():
            path = self.__dialog.GetPath()
            if self.setting_info[self.data.sk_make_new_dir]:
                path = os.path.join(path, "碧蓝航线-导出")
                os.makedirs(path, exist_ok=True)
                ImageWork.split_only_one(target, path)
                self.m_staticText_info.SetLabel(f"{target.cn_name}切割已完成，保存于{path}")

    def sprite_split(self, target):
        if not os.path.isfile(target.tex_path):
            self.m_staticText_info.SetLabel(f"{target}无法切割，至少需要一个Texture2D")
            return
        self.m_staticText_info.SetLabel("开始Sprite切割！")
        self.__dialog = SpriteSplitFrame(self, target)
        self.__dialog.ShowModal()

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
        """
        导出选择项
        :return: none
        """
        target = self.name
        self.__dialog = wx.FileDialog(self, "保存", os.getcwd(), f'{target.cn_name}.png', "*.png",
                                      wx.FD_SAVE | wx.FD_OVERWRITE_PROMPT | wx.FD_PREVIEW)

        if self.__dialog.ShowModal() == wx.ID_OK:
            self.m_gauge_state.SetValue(0)
            self.save_path = self.__dialog.GetPath()
            self.restart()

            target.set_single_path(self.__dialog.GetPath())
            ImageWork.restore_tool(target)

        self.m_gauge_state.SetValue(100)

        if self.setting_info[self.data.sk_finish_exit]:
            self.exit()

    def export_all(self, path, for_work: PerWorkList = None):
        """
        导出全部
        :param path:导出目标目录
        :param for_work: 导出用列表结构体
        :return:
        """
        data = self.data

        if self.setting_info[data.sk_make_new_dir]:
            path += r"\碧蓝航线-导出"

        os.makedirs(path, exist_ok=True)
        # 重置进度
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
        """
        导出不可还原部分（拷贝）
        :return: none
        """
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
        """
        tree元素选择响应方法
        :param event: 事件
        :return:
        """
        # 如果不是在退出状态（在退出的时候tree会鬼畜）
        if not self.enter_exit:

            # 选择修改键复位
            self.m_button_change.Enable(False)
            # 获取选择元素的id
            val = event.GetItem()

            # 如果没用使用搜索或筛选器，就使用默认储存类
            # 查找id，是否为标题标签
            if not self.search_type and not self.filter_type:
                is_ok, name = self.painting_work.find_by_id(val)
            else:
                is_ok, name = self.view_work.find_by_id(val)

            # 如果是，显示预览图
            if is_ok:
                self.m_staticText_info.SetLabel(f"选择：{name.cn_name}")

                self.select_data = self.name = name
                self.thread_quick = QuickRestore(name, self)
                self.thread_quick.start()

            # 寻找tex或mesh路径句柄或触发按键
            else:
                # 从每个元素中查找id
                if not self.search_type and not self.filter_type:
                    is_ok, pos, type_is, index, name = self.painting_work.find_in_each(val)
                else:
                    is_ok, pos, type_is, index, name = self.view_work.find_in_each(val)
                # 找到了

                if is_ok:
                    # 可用修改
                    self.m_button_change.Enable(True)
                    self.is_single, self.type_is, self.name = pos, type_is, name
                    self.index = index
                    # 生成用于显示的对象
                    is_able, value = name.build_sub(pos, type_is, index)
                    if is_able:
                        # 生成对象的texture文件是正常文件
                        self.thread_quick = QuickRestore(value, self)
                        self.thread_quick.start()
                        self.select_data = value
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

                # 没找到，查找功能按键
                else:
                    if not self.search_type and not self.filter_type:
                        is_ok, type_is, target = self.painting_work.find_action(val)
                    else:
                        is_ok, type_is, target = self.view_work.find_action(val)

                    if is_ok:
                        print(target.name)
                        if type_is == self.data.at_independent:
                            self.independent_target(target)
                        if type_is == self.data.at_face_match:
                            self.face_match_target(target)
                        if type_is == self.data.at_atlas_split:
                            self.atlas_split_target(target)
                        if type_is == self.data.at_set_able:
                            self.set_able_target(target)
                        if type_is == self.data.at_remove_item:
                            self.remove_target(target)
                        if type_is == self.data.at_split_only:
                            self.split_target_only(target)
                        if type_is==self.data.at_sprite_split:
                            self.sprite_split(target)

    def choice_file(self, event):
        # 选择对应文件
        is_ok = self.change_path(self.is_single, self.type_is, self.name, self.index)
        if not is_ok:
            wx.MessageBox("无数据！", "错误", wx.OK | wx.ICON_ERROR)
            return

        self.thread_quick = QuickRestore(self.name, self)
        self.thread_quick.run()

    def work(self, event):
        """
        进行导出文件工具
        :param event:
        :return:
        """
        data = self.data
        show = ["导出全部可还原", "拷贝全部不可还原", "导出选择项", "导出当前列表项"]
        # 添加不可用后缀
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
            # 导出全部
            if index == data.et_all:
                # 如果没有可用列表，退出导出
                if len(self.painting_work.build_able()) == 0:
                    wx.MessageBox("不可用！", "错误")
                    return
                # 开始导出目标文件夹选择
                title = '保存-碧蓝航线'
                address = os.getcwd()
                dialog = wx.DirDialog(self, title, address, style=wx.DD_DEFAULT_STYLE | wx.DD_NEW_DIR_BUTTON)

                if dialog.ShowModal() == wx.ID_OK:
                    temp = dialog.GetPath()
                    if self.painting_work.build_able().__len__() > 0:
                        # 开始导出
                        self.export_all(temp, self.painting_work)
            # 拷贝不可还原
            if index == data.et_copy_only:
                if len(self.painting_work.build_unable()) == 0:
                    wx.MessageBox("不可用！！", "错误")
                    return
                self.copy_file()
            # 导出选择项
            if index == data.et_select:
                if self.name is None:
                    wx.MessageBox("不可用！！", "错误")
                    return
                self.export_choice()

            # 导出当前列表项
            if index == data.et_list_item:
                if self.filter_type or self.search_type:
                    if self.view_work.__len__() == 0:
                        wx.MessageBox("不可用！！", "错误")
                        return
                else:
                    if len(self.painting_work) == 0:
                        wx.MessageBox("不可用！！", "错误")
                        return
                title = '保存'"-碧蓝航线"
                address = os.getcwd()
                dialog = wx.DirDialog(self, title, address, style=wx.DD_DEFAULT_STYLE | wx.DD_NEW_DIR_BUTTON)
                if dialog.ShowModal() == wx.ID_OK:
                    temp = dialog.GetPath()
                    if self.view_work.build_able().__len__() > 0:
                        self.export_all(temp, self.view_work)

    def filter_work(self, event):
        """
        筛选器行为
        :param event:
        :return:
        """
        index = event.GetSelection()
        value = self.data.fp_pattern_group[index]

        # 如果筛选器选择全部，重置显示全部
        if index == self.data.tf_all:
            self.filter_type = False

            self.enter_exit = True
            self.m_treeCtrl_info.DeleteChildren(self.root)
            self.painting_work.show_in_tree(self.m_treeCtrl_info, self.root)
            self.enter_exit = False
        else:
            # 根据状态显示不同
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
        """
        查找器行为
        :param event:
        :return:
        """
        # 获取搜索关键字
        if event is None:
            value = self.m_searchCtrl1.GetValue()
        else:
            value = event.GetString()

        # 如果搜索关键字不为空
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
        # 如果搜索为空，重置列表
        else:
            self.search_type = False

            self.enter_exit = True
            self.m_treeCtrl_info.DeleteChildren(self.root)
            self.painting_work.show_in_tree(self.m_treeCtrl_info, self.root)
            self.enter_exit = False

    def setting(self, event):
        """
        打开设置
        :param event:
        :return:
        """
        self.__dialog = Setting(self, self.setting_info, self.work_path, self.names)

        self.__dialog.ShowModal()
        # 重置设置
        self.setting_info = self.__dialog.get_setting()
        self.names = self.__dialog.get_names()

    def resize(self, event):
        """
        重置窗口尺寸（鸡肋）
        :param event:
        :return:
        """
        if self.frame_size != self.GetSize():
            self.thread_quick = QuickRestore(self.select_data, self)
            self.thread_quick.start()

    def exit(self, event=None):
        # 退出
        self.enter_exit = True
        self.m_treeCtrl_info.DeleteChildren(self.root)
        self.m_treeCtrl_info.Destroy()
        self.Destroy()
        sys.exit()
