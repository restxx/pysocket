# coding=utf8
# __author__ = 'doc007'

import asyncio
# import concurrent.futures, sys
from abc import ABCMeta, abstractmethod  # , abstractproperty
from net.msgqueue import MessageQueue
from net.tcpconnect import TcpConnect
from stream.buffio import BufferIO  # , NewBuffIO
from util.dec_warp import coroutine


class TcpClient(metaclass=ABCMeta):
    def __init__(self):
        self.IoLoop = None
        self.__conn = None
        self.__MQ = None
        self._isClosed = False

    def Connect(self, addr, port):
        self.__conn = TcpConnect()
        if -1 == self.__conn.connect(addr, port):
            self.Close()
            return -1

        self.IoLoop = asyncio.get_event_loop()
        self.__MQ = MessageQueue()
        self.OnConnected(self.__conn)
        self.start_proc()
        # self.Run()

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

    @abstractmethod
    @coroutine(None)
    def heartbeat(self, conn):
        # while not self._isClosed:
        pass

    def start_proc(self):
        @coroutine(None)
        def _r():
            bStream = BufferIO()
            while not self._isClosed:
                data = self.__conn.recv_data()
                if not isinstance(data, bytes):
                    self.sendStopCmd()  # 如果关闭向队列中发送一个特殊标记使_s()退出
                    return
                bStream.Write(data)
                # 解析包并做返回操作
                _ = [self.OnRecv(pak) for pak in self.UnPackData(bStream)]

        @coroutine(None)
        def _s():
            while not self._isClosed:
                data = self.__MQ.get()
                if isinstance(data, bytes):
                    self.__conn.sendall(data)
                if data is False:
                    return
        try:
            future = asyncio.gather(*[_r(), _s(), self.heartbeat(self.__conn)])
            self.IoLoop.run_until_complete(future)
        except Exception as err:
            pass

    def SendData(self, data):
        self.__MQ.put(data)
        print("Send", data)

    def Close(self):
        if self.IoLoop and (not self.IoLoop.is_closed()):
            self._isClosed = True
            self.__conn.close()
            self.IoLoop.close()

    def sendStopCmd(self):
        self._isClosed = True
        _ = [self.__MQ.put(False) for i in range(10)]


if __name__ == '__main__':
    pass
