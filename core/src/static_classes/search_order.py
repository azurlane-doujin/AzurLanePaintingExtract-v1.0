import functools
import re


class SearchOrder(object):
    # 搜索
    @staticmethod
    def pattern_builder(x, y):
        """
        change pattern only char to avoid some problems
        :param x: str
        :param y: str
        :return: str
        """
        if re.match(r'[^.|+*?^$()\]\[\\]', y):
            return f'{x}.*{y}'
        else:
            return f'{x}.*\\{y}'

    @staticmethod
    def find(string: str, array_enter: list):
        """
        search
        :param string: the key words for search
        :param array_enter: a list is searched
        :return: the enable index
        """
        str_search = functools.reduce(SearchOrder.pattern_builder, string, '^') + '.*$'

        array_found = zip(array_enter, range(len(array_enter)))
        out = filter(lambda x: re.match(str_search, x[0], re.IGNORECASE), array_found)
        try:
            return list(zip(*out))[-1]
        except IndexError:
            return ()
