# coding=utf8
# __author__ = 'doc007'
from functools import wraps


def excepts(info):
    def dec(func):
        @wraps(func)
        def warp(self, *args, **kwargs):
            try:
                return func(self, *args, **kwargs)
            except Exception as err:
                print("[%s], funcName=[%s], error=[%s][%s]" % (str(self.__class__), func.__name__, info, str(err)))
                return -1

        return warp

    return dec


class a(object):

    @excepts("aaaaaa")
    def ts(self, a, b):
        print(a, b)
        raise Exception("ab error")


if __name__ == '__main__':
    a().ts(1, 3)
    pass
