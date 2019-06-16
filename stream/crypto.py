# coding=utf8
# __author__ = 'doc007'

import pydll
from util.singleton import Singleton

class EncDec(Singleton):

    def __init__(self):
        self._enc = pydll.EncDec()

    def Dec(self, items, start, end=0, enc=0):
        return self._enc.Dec(items, start, end, enc)


if __name__ == '__main__':

    e = EncDec()
    ls = [0]*20
    n = e.Dec(ls, 3)

    pass
