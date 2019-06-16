# coding=utf8
# __author__ = 'doc007'

from util.singleton import Singleton
from util.handlemap import CallMap

class LoginHandle(CallMap, Singleton):

    def cmd_11(self, conn, bIO):
        conn.SendData(b"11111111111111")

        pass

    def Register(self):
        self.bind(0x0B, self.cmd_11)
        pass


if __name__ == '__main__':
    pass
