# coding=utf8
# __author__ = 'doc007'

from net.tcpclient import TcpClient
from stream.buffio import NewBuffIO
from handle import *


class Client(TcpClient):

    def OnConnected(self, conn):
        print(self.__class__, " OnConnected!\n")
        # 发送那两个包
        self.SendData(b"22222222222222222222222222")

    def OnRecv(self, data):
        print("Recv:", data)
        bufio = NewBuffIO(data)
        size = bufio.GetUInt16()
        isZip = bufio.GetUInt16()
        cmd = bufio.GetUInt16()

        login_handle.LoginHandle().Execute(cmd, self, bufio)
        pass

    def heartbeat(self, conn):
        pass

class GateClient(Client):

    def OnConnected(self, conn):
        # 发送另外两个rc5 pak
        pass

    def heartbeat(self, conn):
        # self._isClosed
        pass


def main():
    client = Client()
    client.Connect("127.0.0.1", 22222)


if __name__ == '__main__':
    main()



