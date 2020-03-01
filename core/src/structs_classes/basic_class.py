import collections.abc


class KeyExistError(KeyError):
    def __init__(self, arg):
        self.arg = arg


class BasicInfo(object):
    def __init__(self, name, val):
        """
        基本结构单元类
        :param name: 每一元素对应名称
        :param val: 每一元素对应值
        """
        self.name = name
        self._val = val

    def __str__(self):
        return f'Key:{self.name}\n' f'Name:{self.val}\n'

    @property
    def val(self):
        return self._val

    @val.setter
    def val(self, val):
        self._val = val

    def rebuild_self(self, value):
        """
        对自身的数据进行修改，用新数据覆盖原有
        :param value: 携带覆盖原有数据的基本结构单元
        :return:
        """
        if isinstance(value, BasicInfo):
            self._val = value.val
        else:
            raise ValueError


class BasicInfoList(object):
    def __init__(self, item: collections.abc.Iterable = None):
        """
        基本数据单元容器
        :param item: 每一元素为基本数据单元或其扩展类的可迭代对象；可选，如果传递，将会基于该对象建立容器
        """
        self._info_dict = {}
        self._key_list = []

        self._start = 0
        self._index = 0

        if isinstance(item, collections.abc.Iterable):
            self.extend(item)

    def __delitem__(self, key):
        if isinstance(key, int):
            key = self._key_list[key]
        else:
            pass
        del self._info_dict[key]
        index = self._key_list.index(key)
        del self._key_list[index]

    def __getitem__(self, item):
        if isinstance(item, int):
            return self._info_dict[self._key_list[item]]
        else:
            return self._info_dict[item]

    def __setitem__(self, key: str, value):
        if key in self:
            index = self._key_list.index(key)
            self._key_list[index] = key
        else:
            self._key_list.append(key)

        self._info_dict[key] = value

    def __iter__(self):
        self._index = self._start
        return self

    def __next__(self):
        if self._index >= len(self._key_list):
            raise StopIteration
        else:
            val = self._info_dict[self._key_list[self._index]]
            self._index += 1
            return val

    def __str__(self):
        return str(list(zip(self._key_list, self._info_dict.values())))

    def __len__(self):
        return len(self._key_list)

    def __bool__(self):
        if len(self) <= 0:
            return False
        else:
            return True

    def __contains__(self, item):
        if isinstance(item, str):
            return item in self._key_list
        if isinstance(item, BasicInfo):
            return item in self._info_dict.values()
        else:
            return False

    @staticmethod
    def form_dict(values: dict = None):
        """
        基于给定的字典生成容器
        :param values: 给定的字典
        :return: 容器对象
        """
        if values is None:
            values = {}
        return BasicInfoList([BasicInfo(key_, value_) for key_, value_ in values.items()])

    def remove(self, item: collections.abc.Iterable):
        """
        移除多个指定的元素
        :param item: 需要移除的基本结构单元的可迭代对象
        :return: 移除指定元素后的容器
        """
        return BasicInfoList(filter(lambda x: x not in item, self))

    def get_new(self, item: collections.abc.Iterable):
        """
        用新的容器与原有的比较，查找新增的基本结构单元
        :param item: 新的容器
        :return: 储存新增基本结构单元的容器
        """
        return BasicInfoList(filter(lambda x: x not in self, item))

    def append_name(self, name, val, *, has_cn=False):
        """
        添加新的元素，如果新元素名称已经存在就不添加
        :param name: 新元素名称
        :param val: 新元素数据
        :param has_cn: 新元素本地化情况
        :return: 新元素名称
        """
        if name not in self._info_dict:
            self[name] = BasicInfo(name, val)
        else:
            pass

        return name

    def append_self(self, value):
        """
        添加新元素，基于基本容器单元
        :param value: 要添加的基本容器单元
        :return: 新元素名称
        """
        if isinstance(value, BasicInfo):
            self[value.name] = value
        else:
            raise ValueError(f'{type(value)}is not able')

    def extend(self, values):
        """
        扩充容器中的元素
        :param values: 要添加基本结构单元组
        :return: 无
        """
        if isinstance(values, collections.abc.Iterable):
            list(map(lambda _x: self.append_self(_x), values))

    def set_self(self, key, value):
        """
        更新指定元素的数据（全部）
        :param key: 指定元素的对应的键（名称）
        :param value: 用于更新的基本容器单元
        :return: 无
        """
        self[key].rebuild_self(value)

    def clear(self):
        """
        清空所有数据
        :return: 无
        """
        self._key_list.clear()
        self._info_dict.clear()

    def get_index(self, value):
        """
        获取对应元素的索引
        :param value: 要查找的元素
        :return:
        """
        if isinstance(value, BasicInfo):
            try:
                return self._key_list.index(value.name)
            except ValueError:
                return None
        if isinstance(value, str):
            try:
                return self._key_list.index(value)
            except ValueError:
                return None

    def is_in_dict(self, item):
        """
        查找某一元素是否在本容器中
        :param item: 被查找元素
        :return: True/False
        """
        return item not in self._info_dict.keys()
