# coding=utf8
# __author__ = 'doc007'

import queue
from util.dec_warp import excepts, coroutine

TIME_OUT = 10  # 秒
MAXS_SIZE = 100


class MessageQueue(object):

    def __init__(self):
        self._Q = queue.Queue(maxsize=MAXS_SIZE)

    @excepts(__name__)
    def put(self, item):
        self._Q.put(item, block=True, timeout=TIME_OUT)

    def get(self):
        return self._Q.get()


if __name__ == '__main__':
    pass
