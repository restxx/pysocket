# coding=utf8
# __author__ = 'doc007'

from util.singleton import Singleton
from util.handlemap import CallMap


class LoginHandle(CallMap, Singleton):

    def cmd_11(self, conn, bIO):
        conn.SendData(b"11111111111111")
        conn.SendData(b"11111111111111")
        conn.sendStopCmd()

    def cmd_104_21(self, conn, bIO):
        pass

    def Register(self):
        self.bind(0x0B, self.cmd_11)
        self.bind(0x00, self.cmd_104_21)
        pass


if __name__ == '__main__':
    a = LoginHandle()

    pass
