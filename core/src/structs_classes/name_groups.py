import wx

from .basic_class import BasicInfoList, BasicInfo


class NameGroups(BasicInfoList):
    def __init__(self, item):
        super(NameGroups, self).__init__(item=item)

    def show_in_tree(self, tree: wx.TreeCtrl, root: wx.TreeItemId):
        for value in self:
            value: NameInfo
            value.init_add2tree(tree, root)
            value.add2tree()

    def add_new_name(self, key, value):
        if key not in self._key_list:
            new_name = NameInfo(key, value)
            new_name.add_location(key, value)


class NameInfo(BasicInfo):
    """
    本地化处理类
    去除后缀相同的对象放在一起
    """

    def __init__(self, name, val):
        super(NameInfo, self).__init__(name, val)
        self.all_location = {}
        # tree id
        self.title_id = ...
        self.all_ids = []

        # self.content_id = ...
        self.tree = ...

    def add_location(self, key, name):
        """
        先判断key是否是本组本地化对象
        :param key:
        :param name:
        :return: bool 是否成功
        """
        if key in self.all_location.keys():
            return False
        else:
            self.all_location[key] = name
            return True

    def init_add2tree(self, tree: wx.TreeCtrl, root: wx.TreeItemId):
        """
        初始化添加到树[创建title]
        :param tree:
        :param root:
        :return:
        """
        pass

    def add2tree(self):
        """
        添加本对象到目标tree中
        :return:
        """
        pass

    def add2tree_single(self, key="", value=""):
        """
        添加单独项目到tree
        :param key:
        :param value:
        :return:
        """

    def transform2dict(self):
        """
        转换为字典类型
        :return:
        """
        return self.all_location

    def is_self_key(self, id):
        if id == self.title_id or id in self.all_ids:
            return True
        return False
