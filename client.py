# coding=utf-8
# __author__ = 'doc007'
import time
from handle import *
from net.tcpclient import TcpClient
from stream.buffio import NewBuffIO
from util.dec_warp import coroutine


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

        mid = bufio.GetUInt16()
        sid = bufio.GetUInt16()

        hdl = handle_map.HMAP.SelectHandle(mid)
        if hdl:
            hdl.Execute(sid, self, bufio)

    @coroutine(None)
    def heartbeat(self, conn):
        pass
        # while not self._isClosed:
        #     time.sleep(5)
        #     print("heart heart heart heart")


class GateClient(Client):

    def OnConnected(self, conn):
        # 发送另外两个rc5 pak
        pass

    @coroutine(None)
    def heartbeat(self, conn):
        # self._isClosed
        pass


def main():
    client = Client()
    client.Connect("127.0.0.1", 22222)


if __name__ == '__main__':
    main()



