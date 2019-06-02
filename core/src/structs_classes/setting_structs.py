import collections
import functools

from core.src.structs_classes.basic_class import BasicInfo, BasicInfoList


class PerSetting(BasicInfo):
    def __init__(self, name, val):
        super(PerSetting, self).__init__(name, val)

        self.val = self._val

        self._link_set: collections.Callable = ...
        self._link_get: collections.Callable = ...

    def __str__(self):
        return f"\n" \
            f"\tclass:PerHolder" \
            f"\tname：{self.name}\n" \
            f"\tval：{self.val}\n" \
            f"\tset_link：{self.set_link}\n" \
            f"\tset_link：{self.get_link}\n"

    @property
    def val(self):
        return self._val

    @val.setter
    def val(self, val):
        self._val = val

    @property
    def set_link(self):
        return self._link_set

    @set_link.setter
    def set_link(self, func: collections.abc.Callable):
        if isinstance(func, collections.abc.Callable):
            self._link_set = func

    @property
    def get_link(self):
        return self._link_get

    @get_link.setter
    def get_link(self, func):
        if isinstance(func, collections.abc.Callable):
            self._link_get = func

    @property
    def value(self):
        return self.val

    def set_value(self):
        if isinstance(self.set_link, collections.abc.Callable):
            self.set_link(self.val)

    def get_value(self):
        if isinstance(self.get_link, collections.abc.Callable):
            self.val = self.get_link()

    def set_to_dict(self, value):
        value[self.name] = self.val


class SettingHolder(BasicInfoList):
    def __init__(self, setting: dict = None):
        super(SettingHolder, self).__init__()
        self.able = []

        if setting is not None and isinstance(setting, dict):
            self.from_dict(setting)

    def __getattr__(self, item):

        if item in self._key_list:
            return self._info_dict[item]
        else:
            raise AttributeError

    def __setattr__(self, key, value):

        if key in ['_info_dict', '_key_list', 'able', "_start", "_index"]:
            super(SettingHolder, self).__setattr__(key, value)
        else:
            if key not in self._key_list:
                self._key_list.append(key)

                self._info_dict[key] = PerSetting(key, value)

    def __setitem__(self, key, value):
        self.__setattr__(key, value)

    def __getitem__(self, item):
        return self.__getattr__(item=item)

    def __str__(self):
        val = functools.reduce(lambda x, y: f'{x}\n\t{y.name}：{y}', self._info_dict.values(), f'class:\tSettingHolder')

        return val

    def to_dict(self):
        val = self._info_dict
        var = {}
        for key in val.keys():
            var[key] = val[key].val

        return dict(var)

    def from_dict(self, setting: dict):
        keys = setting.keys()
        values = setting.values()
        list(map(self.__setattr__, keys, values))

    def link_val(self, key, link_set, link_get):
        if key in self._key_list:
            self._info_dict[key].set_link = link_set
            self._info_dict[key].get_link = link_get

    def link_dict(self, val: dict):
        list(map(lambda x: self.link_val(x, val[x][0], val[x][1]), val.keys()))

    def initial_val(self):
        val = self._key_list
        list(map(lambda x: self._info_dict[x].set_value(), val))

    def get_value(self):
        val = self._key_list
        list(map(lambda x: self._info_dict[x].get_value(), val))

    def get_dict(self):
        value = {self._info_dict[val].name: self._info_dict[val].value for val in self._key_list}
        return value
