import collections.abc


class KeyExistError(KeyError):
    def __init__(self, arg):
        self.arg = arg


class BasicInfo(object):
    def __init__(self, name, val):

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

        if isinstance(value, BasicInfo):
            self._val = value.val
        else:
            raise ValueError


class BasicInfoList(object):
    def __init__(self, item: collections.abc.Iterable = None):

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

        if values is None:
            values = {}
        return BasicInfoList([BasicInfo(key_, value_) for key_, value_ in values.items()])

    def remove(self, item: collections.abc.Iterable):
        return BasicInfoList(filter(lambda x: x not in item, self))

    def get_new(self, item: collections.abc.Iterable):
        return BasicInfoList(filter(lambda x: x not in self, item))

    def append_name(self, name, val, *, has_cn=False):
        if name not in self._info_dict:
            self[name] = BasicInfo(name, val)
        else:
            pass

        return name

    def append_self(self, value):
        if isinstance(value, BasicInfo):
            self[value.name] = value
        else:
            raise ValueError(f'{type(value)}is not able')

    def extend(self, values):
        if isinstance(values, collections.abc.Iterable):
            list(map(lambda _x: self.append_self(_x), values))

    def set_self(self, key, value):
        self[key].rebuild_self(value)

    def clear(self):
        self._key_list.clear()
        self._info_dict.clear()

    def get_index(self, value):
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
        return item not in self._info_dict.keys()
