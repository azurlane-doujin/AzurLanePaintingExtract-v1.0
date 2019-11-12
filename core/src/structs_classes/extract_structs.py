import collections
import os
import re
import time
from itertools import filterfalse

import wx

from core.src.static_classes.static_data import GlobalData
from core.src.structs_classes.basic_class import BasicInfo, BasicInfoList


class PerInfo(BasicInfo):
    def __init__(self, name, val, has_cn):
        super(PerInfo, self).__init__(name, val)
        self.sub_data = 1

        self.data = GlobalData()
        # tree储存结构组
        self._tex_path = "Empty"
        self.more_tex = ["Empty"]
        self._mesh_path = "Empty"
        self.more_mesh = ["Empty"]
        # 目标文件位置
        self.lay_in = ""
        # 是否可以使用还原
        self.is_able_work = False
        # 导出目标位置
        self._save_path: str = ""
        # 中文名称
        self.cn_name = val
        self.has_cn = has_cn
        # 父组件
        self.parent = None

        # tree ID
        self.key = ...
        self.tree_ID = ...
        self.tex_id = ...
        self.more_tex_per_id = []
        self.mesh_id = ...
        self.more_mesh_per_id = []
        self.independent_ID = ...
        # 是否以中文保存
        self._is_save_as_cn = True

    def __contains__(self, item):
        if self.name in item or self.cn_name in item:
            return True
        else:
            return False

    @property
    def tex_path(self):
        return self._tex_path

    @tex_path.setter
    def tex_path(self, value):
        self._tex_path = value
        self.is_able_work = self.is_able()

    @property
    def mesh_path(self):
        return self._mesh_path

    @mesh_path.setter
    def mesh_path(self, value):
        self._mesh_path = value
        self.is_able_work = self.is_able()

    @property
    def save_path(self):
        return self._save_path

    @save_path.setter
    def save_path(self, value):
        if self._is_save_as_cn:
            self._save_path = os.path.join(value, self.cn_name + ".png")
        else:

            self._save_path = os.path.join(value, self.name + ".png")

    @property
    def is_save_as_cn(self):
        return self._is_save_as_cn

    @is_save_as_cn.setter
    def is_save_as_cn(self, value):
        if isinstance(value, bool):
            self._is_save_as_cn = value

    @staticmethod
    def is_def(val):
        return bool(val)

    def is_able(self):
        if os.path.isfile(self.tex_path) and os.path.isfile(self.mesh_path):
            return True
        else:
            return False

    def append_to_tree(self, tree: wx.TreeCtrl, tree_root: wx.TreeItemId):
        """
        添加到树，构建tree列表
        :param tree: tree 对象
        :param tree_root: 根id
        :return:
        """
        self.more_mesh_per_id.clear()
        self.more_tex_per_id.clear()

        self.tree_ID = tree.AppendItem(tree_root, self.cn_name)
        # 名称
        self.key = key = tree.AppendItem(self.tree_ID, f"名称：{self.cn_name}")
        if self.is_able_work:
            tree.SetItemTextColour(key, wx.Colour(253, 86, 255))
        tree.AppendItem(self.tree_ID, f"索引名称：{self.name}")
        # texture
        self.tex_id = tree.AppendItem(self.tree_ID, f"Texture文件路径：{self.tex_path}")

        more_tex_id = tree.AppendItem(self.tree_ID, f"其他Texture路径({len(self.more_tex)})")
        for each_path in self.more_tex:
            val = tree.AppendItem(more_tex_id, each_path)
            self.more_tex_per_id.append(val)
        # mesh
        self.mesh_id = tree.AppendItem(self.tree_ID, f"Mesh文件路径：{self.mesh_path}")

        more_mesh_id = tree.AppendItem(self.tree_ID, f"其他Mesh路径({len(self.more_mesh)})")
        for each_path in self.more_mesh:
            val = tree.AppendItem(more_mesh_id, each_path)
            self.more_mesh_per_id.append(val)
        # 功能键
        self.independent_ID = tree.AppendItem(self.tree_ID, "将当前的组合独立")
        tree.SetItemTextColour(self.independent_ID, wx.Colour(255, 0, 166))

    def get_select(self, type_is: bool):
        """
        获取选中的列表
        :param type_is: true ：texture，false：mesh
        :return: list，选中的列表
        """
        if type_is:
            return self.more_tex
        else:
            return self.more_mesh

    # 路径设置相关
    def set_tex(self, index):
        self.tex_path = self.more_tex[index]
        return self.tex_id, f"Texture文件路径：{self.tex_path}"

    def set_mesh(self, index):
        self.mesh_path = self.more_mesh[index]
        return self.mesh_id, f"Mesh文件路径：{self.mesh_path}"

    def add_save(self, path):
        self.save_path = path

    def clear_tex(self):
        self.tex_id, self.more_tex, self.tex_path, self.more_tex_per_id = None, [], "Empty", []

    def clear_mesh(self):

        self.mesh_id, self.more_mesh, self.mesh_path, self.more_mesh_per_id = None, [], "Empty", []

    def build_sub(self, value_type, file_type, index):
        """
        从自身的treeid中寻找目标
        :param value_type:
        :param file_type:
        :param index:
        :return:
        """
        val = PerInfo(self.name, self.val, self.has_cn)
        if value_type == self.data.td_single:
            if file_type == self.data.td_texture_type:
                val.tex_path = self.tex_path
            elif file_type == self.data.td_mesh_type:
                val.mesh_path = self.mesh_path
        elif value_type == self.data.td_list_item:
            if file_type == self.data.td_texture_type:
                val.tex_path = self.more_tex[index]
            elif file_type == self.data.td_mesh_type:
                val.mesh_path = self.more_mesh[index]

        return os.path.isfile(val.tex_path), val

    def independent(self, name, tree, tree_root):
        # 独立
        target = PerInfo(name, f"{self.val}-# {self.sub_data}", self.has_cn)
        target.tex_path = self.tex_path
        target.mesh_path = self.mesh_path
        target.append_to_tree(tree, tree_root)
        self.parent[target.name] = target
        self.sub_data += 1


class PerWorkList(BasicInfoList):
    def __init__(self, item: collections.abc.Iterable = None):
        super(PerWorkList, self).__init__(item)
        self.data = GlobalData()

    # 显示部分
    def show_in_tree(self, tree, tree_root):
        list(map(lambda x: self._info_dict[x].append_to_tree(tree, tree_root), self._key_list))

    def append(self, name, cn_name, has_cn):
        value = PerInfo(name, cn_name, has_cn)

        self[value.name] = value
        return value

    def remove(self, item: collections.abc.Iterable):
        return PerWorkList(super(PerWorkList, self).remove(item))

    # 查找部分
    def find_by_id(self, id):
        values = list(filter(lambda x: self._info_dict[x].tree_ID == id, self._key_list))
        if values.__len__() == 0:
            return False, None
        return True, self[values[0]]

    def find_in_each(self, id) -> (bool, bool, bool, int, PerInfo):
        """
        从每一个中寻找指定id
        :param id:
        :return: (是否成功，类型【单个True，列表False】，类型[tex(True),mesh(False)]，索引，对象本身)
        """
        target = None
        for value in self:
            # 如果id为以下的部分，进入
            if id == value.tex_id == id or id in value.more_tex_per_id or value.mesh_id == id or \
                    id in value.more_mesh_per_id:
                target = value
        if target is None:
            return False, False, False, -1, None
        if id == target.tex_id:
            return True, self.data.td_single, self.data.td_texture_type, 0, target
        elif id == target.mesh_id:
            return True, self.data.td_single, self.data.td_mesh_type, 0, target
        elif id in target.more_tex_per_id:
            return True, self.data.td_list_item, self.data.td_texture_type, target.more_tex_per_id.index(id), target
        elif id in target.more_mesh_per_id:
            return True, self.data.td_list_item, self.data.td_mesh_type, target.more_mesh_per_id.index(id), target

    def find_action(self, id) -> (bool, int, PerInfo):
        """
        查找是否为特殊动作按键
        :param id:
        :return: 是否成功【true/false】，动作类型，作用目标
        """
        target = None
        for value in self:
            # 如果id为以下的部分，进入
            if id == value.independent_ID:
                target = value
                break
        if target is None:
            return False, -1, target
        if id == target.independent_ID:
            return True, self.data.at_independent, target

    # 添加部分
    def set_tex(self, value, name=None):
        """
        添加贴图
        :param name: [可选]新添加的texture地址的指向项目名称，为None会根据value获取
        :param value: 新添加的texture地址
        :return:
        """
        has_ = False
        if isinstance(value, str) and os.path.isfile(value):
            if name is not None:
                key = name
            else:
                key = os.path.splitext(os.path.basename(value))[0]
                if re.match(r'.+\s#\d+\.png', value, re.IGNORECASE):
                    has_ = True
                    key = re.split(r'\s#\d+(\[alpha\])?$', key)[0]

            val: PerInfo = self._info_dict[key]
            if value not in val.more_tex:
                val.more_tex.append(value)

            if val.tex_path.lower() == "empty":
                val.tex_path = value
            if os.path.split(value)[0].lower().endswith("texture2d"):
                val.tex_path = value
            if not has_:
                val.tex_path = value

    def set_mesh(self, value, name=None):
        """
               添加mesh网格
               :param name: [可选]新添加的mesh地址的指向项目名称，为None会根据value获取
               :param value: 新添加的mesh地址
               :return:
               """
        has_ = False
        if isinstance(value, str) and os.path.isfile(value):
            if name is not None:
                key = name
            else:
                key = os.path.splitext(os.path.basename(value))[0]
                if re.match(r'.+\s#\d+\.obj', value, re.IGNORECASE):
                    has_ = True
                    key = re.split(r'\s#\d+(\[alpha\])?$', key)[0]

            val: PerInfo = self._info_dict[key]
            if value not in val.more_mesh:
                val.more_mesh.append(value)

            if val.mesh_path.lower() == "empty":
                val.mesh_path = value
            if os.path.split(value)[0].lower().endswith("mesh"):
                val.mesh_path = value
            if not has_:
                val.mesh_path = value

    def append_name(self, name, names: dict, *, has_cn=False):
        """
        添加新对象
        :param names: 预设键-值对应组
        :param name: 对象索引key
        :param has_cn: 对象是否有中文名
        :return:
        """
        # if name == "unknown4":
        #     print(name)
        if name not in self._key_list:
            if name not in names.keys():
                has_cn = False
                target_cn = name
            else:
                has_cn = True
                target_cn = names[name]
            # 如果中文名为空，也认为没有中文名
            if target_cn == "":
                target_cn = name
                has_cn = False

            value = PerInfo(name, target_cn, has_cn)
            value.parent = self

            self[name] = value

            return name
        else:
            return name

    # 清空部分
    def clear_mesh(self):
        list(map(lambda x: x.clear_mesh(), self))

    def clear_tex(self):
        list(map(lambda x: x.clear_tex(), self))

    # 生成部分
    def build_able(self):
        val = filter(lambda x: x.is_able_work, self)
        value = PerWorkList(val)
        return value

    def build_unable(self):
        val = filterfalse(lambda x: x.is_able_work, self)
        value = PerWorkList(val)
        return value

    def build_search(self):
        val = map(lambda x: f"{x.name}{x.cn_name}", self)
        return list(val)

    def build_filter(self):
        val = map(lambda x: f"{x.name}", self)
        val = list(enumerate(list(val), 0))
        return val

    def build_skip(self, filename):
        filename = list(map(lambda x: os.path.splitext(os.path.basename(x))[0], filename))

        val = filter(lambda x: x in filename, self)

        return PerWorkList(val)

    def build_from_indexes(self, indexes):
        val = map(lambda x: self[x], indexes)
        value = PerWorkList(val)
        return value

    def build_from_pattern(self, pattern):
        val = list(filter(lambda x: re.match(pattern, list(x)[1]), self.build_filter()))
        val = list(zip(*val))
        if len(val) == 2:
            return self.build_from_indexes(val[0])
        else:
            return PerWorkList()
