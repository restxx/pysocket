# coding=utf8
# __author__ = 'doc007'

import asyncio, sys
import concurrent.futures
from abc import ABCMeta, abstractmethod  # , abstractproperty
from net.msgqueue import MessageQueue
from net.tcpconnect import TcpConnect
from stream.buffio import BufferIO #, NewBuffIO


class TcpClient(metaclass=ABCMeta):
    def __init__(self):
        self.IoLoop = None
        self.__conn = None
        self.__MQ = None

    def Connect(self, addr, port):
        self.IoLoop = asyncio.get_event_loop()

        self.__conn = TcpConnect()
        if -1 == self.__conn.connect(addr, port):
            self.Close()

        self.__MQ = MessageQueue()
        self.OnConnected(self.__conn)

    @abstractmethod
    def OnConnected(self, conn):
        # print("base TcpClient")
        pass

    @abstractmethod
    def OnRecv(self, data):
        pass

    # @abstractmethod
    def UnPackData(self, bufIO):
        total, paks = 0, []
        while True:
            ls = bufIO.Peek(2)
            if not ls:
                break
            nlen = int.from_bytes(ls, 'little', signed=False) + 4
            if not (bufIO.len >= nlen):
                break
            ls = bufIO.Next(nlen)
            paks.append(ls)
            total += 1

        if total > 0 and bufIO.Empty():
            bufIO.Reset()
        return paks


    async def startProc(self):
        def _r():
            bIO = BufferIO(False)
            while True:
                data = self.__conn.recvData()
                bIO.Write(data)
                # 解析包并做返回操作
                _ = [self.OnRecv(pak) for pak in self.UnPackData(bIO)]


        def _s():
            while True:
                data = self.__MQ.get()
                self.__conn.sendall(data)

        with concurrent.futures.ThreadPoolExecutor(max_workers=8) as executor:
            futures = [
                self.IoLoop.run_in_executor(executor, _r),
                self.IoLoop.run_in_executor(executor, _s)
            ]
            return [ret for ret in await asyncio.gather(*futures)]

    def SendData(self, data):
        self.__MQ.put(data)
        print("Send", data)

    def Run(self):
        self.IoLoop.run_until_complete(self.startProc())

    def Close(self):
        self.IoLoop.close()


if __name__ == '__main__':
    pass
#     client = Client()
#     client.Connect("127.0.0.1", 22222)
#     client.Run()
