import collections

import wx

import core.src.structs_classes as dt
from .basic_class import BasicInfo, BasicInfoList


class PerLocation(BasicInfo):
    def __init__(self, key, name, parent, state=dt.EXIST):
        super(PerLocation, self).__init__(key, name)
        self.state = state
        self.parent = parent
        self.old_data = None
        self.id = ...

    def __str__(self):
        return f"键->\"{self.name}\"；值->\"{self.val}\""

    def add_to_tree(self, tree: wx.TreeCtrl, exist_root, new_root, cover_root):
        if self.state == dt.EXIST:
            target_root = exist_root
        elif self.state == dt.NEW:
            target_root = new_root
        elif self.state == dt.COVER:
            target_root = cover_root
        else:
            return

        item_root = tree.AppendItem(target_root, str(self))
        tree.AppendItem(item_root, f"本地化原始名：”{self.name}“")
        if self.state == dt.COVER:
            tree.AppendItem(item_root, f"原始本地化名称：”{self.old_data}“")
        tree.AppendItem(item_root, f"本地化名：”{self.val}“")


class LocationList(BasicInfoList):
    def __init__(self, item: collections.Iterable=None):
        super(LocationList, self).__init__(item)
        self.exist_count = 0
        self.cover_count = 0
        self.new_count = 0

        self.exist_root = ...
        self.cover_root = ...
        self.new_root = ...

    def compare(self, values: dict, value_new: dict):
        """
        比对，生成列表
        :param values: 原始键值对
        :param value_new: 新键值对
        :return:
        """
        for key, item in value_new.items():
            if key not in values.keys():
                self[key] = PerLocation(key, item, self, dt.NEW)
                self.new_count += 1
            else:
                if item == values[key]:
                    self[key] = PerLocation(key, item, self, dt.EXIST)
                    self.exist_count += 1
                else:
                    temporary = PerLocation(key, item, self, dt.COVER)
                    temporary.old_data = values[key]

                    self[key] = temporary
                    self.cover_count += 1

    def add_to_tree(self, tree: wx.TreeCtrl, root):
        self.exist_root = tree.AppendItem(root, f"已经存在的本地化资源（{self.exist_count}）")
        self.cover_root = tree.AppendItem(root, f"覆盖原有的本地化资源（{self.cover_count}）")
        self.new_root = tree.AppendItem(root, f"新增的的本地化资源（{self.new_count}）")

        for value in self:
            value.add_to_tree(tree, self.exist_root, self.new_root, self.cover_root)

    def transform_all(self):
        group = filter(lambda x: x.state == dt.NEW or x.state == dt.COVER, self)
        value = {key.name.lower(): key.val for key in group}
        return value

    def transform_new(self):
        group = filter(lambda x: x.state == dt.NEW, self)
        value = {key.name.lower(): key.val for key in group}
        return value

    def transform_cover(self):
        group = filter(lambda x: x.state == dt.COVER, self)
        value = {key.name.lower(): key.val for key in group}
        return value
