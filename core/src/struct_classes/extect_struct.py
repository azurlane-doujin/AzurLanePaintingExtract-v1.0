import collections
import os
import re
from itertools import filterfalse

import wx

from core.src.struct_classes.basic_class import BasicInfo, BasicInfoList


class PerInfo(BasicInfo):
    def __init__(self, name, val, has_cn):
        super(PerInfo, self).__init__(name, val)

        self._tex_path = "Empty"
        self.more_tex = []
        self._mesh_path = "Empty"
        self.more_mesh = []

        self.lay_in = ""

        self.is_able_work = False

        self._save_path: str = ""

        self.cn_name = val
        self.has_cn = has_cn

        self.tree_ID = ...
        self.tex_id = ...
        self.more_tex_per_id = []
        self.mesh_id = ...
        self.more_mesh_per_id = []

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
        self._save_path = os.path.join(value, self.cn_name + ".png")

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
        添加到树
        :param tree: tree 对象
        :param tree_root: 根id
        :return:
        """

        self.tree_ID = tree.AppendItem(tree_root, self.cn_name)

        tree.AppendItem(self.tree_ID, f"名称：{self.cn_name}")
        tree.AppendItem(self.tree_ID, f"原始文件名：{self.name}")

        self.tex_id = tree.AppendItem(self.tree_ID, f"Texture文件路径：{self.tex_path}")

        more_tex_id = tree.AppendItem(self.tree_ID, f"其他Texture路径({len(self.more_tex)})")
        for each_path in self.more_tex:
            val = tree.AppendItem(more_tex_id, each_path)
            self.more_tex_per_id.append(val)

        self.mesh_id = tree.AppendItem(self.tree_ID, f"Mesh文件路径：{self.mesh_path}")

        more_mesh_id = tree.AppendItem(self.tree_ID, f"其他Mesh路径({len(self.more_mesh)})")
        for each_path in self.more_mesh:
            val = tree.AppendItem(more_mesh_id, each_path)
            self.more_mesh_per_id.append(val)

    def get_select(self, type_is: bool):
        if type_is:
            return self.more_tex
        else:
            return self.more_mesh

    def set_tex(self, index):
        self.tex_path = self.more_tex[index]
        return self.tex_id, f"Texture文件路径：{self.tex_path}"

    def set_mesh(self, index):
        self.mesh_path = self.more_mesh[index]
        return self.mesh_id, f"Texture文件路径：{self.tex_path}"

    def add_save(self, path):
        self.save_path = path

    def clear_tex(self):
        self.tex_id, self.more_tex, self.tex_path, self.more_tex_per_id = None, [], "Empty", []

    def clear_mesh(self):

        self.mesh_id, self.more_mesh, self.mesh_path, self.more_mesh_per_id = None, [], "Empty", []


class PerWorkList(BasicInfoList):
    def __init__(self, item: collections.abc.Iterable = None):
        super(PerWorkList, self).__init__(item)

    # 显示部分
    def show_in_tree(self, tree, tree_root):
        list(map(lambda x: self._info_dict[x].append_to_tree(tree, tree_root), self._key_list))

    def append(self, name, cn_name, has_cn):
        value = PerInfo(name, cn_name, has_cn)

        self[value.name] = value
        return value

    # 查找部分
    def find_by_id(self, id):
        values = list(filter(lambda x: self._info_dict[x].tree_ID == id, self._key_list))
        if values.__len__() == 0:
            return False, None
        return True, self[values[0]]

    def find_in_each(self, id) -> (bool, bool, bool, int, PerInfo):
        """

        :param id:
        :return: (是否成功，类型【单个True，列表False】，类型[tex(True),mesh(False)]，索引，对象本身)
        """
        target = None
        for value in self:
            if id == value.tex_id == id or id in value.more_tex_per_id or value.mesh_id == id or \
                    id in value.more_mesh_per_id:
                target = value
        if target is None:
            return False, False, False, -1, None
        if id == target.tex_id:
            return True, True, True, 0, target
        elif id == target.mesh_id:
            return True, True, False, 0, target
        elif id in target.more_tex_per_id:
            return True, False, True, target.more_tex_per_id.index(id), target
        elif id in target.more_mesh_per_id:
            return True, False, False, target.more_mesh_per_id.index(id), target

    # 添加部分
    def set_tex(self, value, name=None):
        """
        添加贴图
        :param name: [可选]新添加的texture地址的指向项目名称，为None会根据value获取
        :param value: 新添加的texture地址
        :return:
        """
        if isinstance(value, str) and os.path.isfile(value):
            if name is not None:
                key = name
            else:
                key = os.path.splitext(os.path.basename(value))[0]
                if re.match(r'.+\s#\d+\.png', value, re.IGNORECASE):
                    key = re.split(r'\s#\d+(\[alpha\])?$', key)[0]

            val: PerInfo = self._info_dict[key]
            if value not in val.more_tex:
                val.more_tex.append(value)

            if val.tex_path.lower() == "empty":
                val.tex_path = value
            if os.path.split(value)[0].lower().endswith("texture2d"):
                val.tex_path = value

    def set_mesh(self, value, name=None):
        """
               添加mesh网格
               :param name: [可选]新添加的mesh地址的指向项目名称，为None会根据value获取
               :param value: 新添加的mesh地址
               :return:
               """
        if isinstance(value, str) and os.path.isfile(value):
            if name is not None:
                key = name
            else:
                key = os.path.splitext(os.path.basename(value))[0]
                if re.match(r'.+\s#\d+\.obj', value, re.IGNORECASE):
                    key = re.split(r'\s#\d+(\[alpha\])?$', key)[0]

            val: PerInfo = self._info_dict[key]
            if value not in val.more_mesh:
                val.more_mesh.append(value)

            if val.mesh_path.lower() == "empty":
                val.mesh_path = value
            if os.path.split(value)[0].lower().endswith("mesh"):
                val.mesh_path = value

    def append_name(self, name, val: dict, *, has_cn=False):
        if name == "unknown4":
            print(name)
        if name not in self._key_list:

            if name not in val.keys():
                has_cn = False
                val = name
            else:
                has_cn = True
                val = val[name]

            if val == "":
                val = name
                has_cn = False

            value = PerInfo(name, val, has_cn)

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

    def build_from_indexes(self, indexes):
        val = map(lambda x: self[x], indexes)
        value = PerWorkList(val)
        return value
