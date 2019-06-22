# coding=utf-8
# __author__ = 'doc007'

import six
from abc import ABCMeta
from util.singleton import Singleton


@six.add_metaclass(metaclass=ABCMeta)
class HandleMap(Singleton):

    def __init__(self):
        self.__Hmap = {}

    def bind(self, mId):
        def dec(cls):
            def warp(*args, **kwargs):
                c = cls(*args, **kwargs)
                c.Mid = mId
                self.__Hmap.update({mId: c})
                return c

            return warp

        return dec

    def SelectHandle(self, mId):
        return self.__Hmap.get(mId)


HMAP = HandleMap()
