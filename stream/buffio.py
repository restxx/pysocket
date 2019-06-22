# coding=utf-8
# __author__ = 'doc007'

from util.dec_warp import excepts
from stream.crypto import EncDec


class BufferIO(object):

    def __init__(self, enc=False):
        self.pr = 0  # 读指针
        self.pw = 0  # 写指针
        self.pd = 0  # 解密指针
        self.buf = [0] * 65535

        self.__decFun = None
        if enc:
            self.__decFun = EncDec().Dec

    # 可供读取的长度
    @property
    def len(self):
        return self.pd - self.pr

    @excepts(__name__)
    def Write(self, bData):
        encs = list(bData)

        if (len(self.buf) - self.pw) < len(encs):
            self.buf.extend(encs)
        else:
            def _c(i, v):
                self.buf[self.pw + i] = v

            _ = [_c(i, v) for i, v in enumerate(encs)]
        self.pw += len(encs)

        # 再解密  无须解密的情况
        if not self.__decFun:
            self.pd = self.pw
            return

        remain = self.__decFun(self.buf, self.pd, self.pw, False)
        if remain < 0:  # 剩余未解密字节数
            raise Exception('Decrypt Error code=%d' % remain)
        self.pd = (self.pw - remain)

    def Peek(self, n):
        if n <= (self.pd - self.pr):
            return self.buf[self.pr:self.pr + n]

    def Next(self, n):
        ls = self.Peek(n)
        if ls:
            self.pr += n
            return ls

    def Empty(self):
        return self.pw == self.pr

    def Reset(self):
        self.pr = 0  # 读指针
        self.pw = 0  # 写指针
        self.pd = 0  # 解密指针

    def GetUInt8(self):
        ls = self.Next(1)
        if ls:
            return int.from_bytes(ls, "little", signed=False)

    def GetInt8(self):
        ls = self.Next(1)
        if ls:
            return int.from_bytes(ls, "little", signed=True)

    def GetUInt16(self):
        ls = self.Next(2)
        if ls:
            return int.from_bytes(ls, "little", signed=False)

    def GetInt16(self):
        ls = self.Next(2)
        if ls:
            return int.from_bytes(ls, "little", signed=True)

    def GetUInt32(self):
        ls = self.Next(4)
        if ls:
            return int.from_bytes(ls, "little", signed=False)

    def GetInt32(self):
        ls = self.Next(4)
        if ls:
            return int.from_bytes(ls, "little", signed=True)

    def GetUInt64(self):
        ls = self.Next(8)
        if ls:
            return int.from_bytes(ls, "little", signed=False)

    def GetInt64(self):
        ls = self.Next(8)
        if ls:
            return int.from_bytes(ls, "little", signed=True)

    def GetFloat(self):
        x = self.Next(4)
        if x:
            return struct.unpack('<f', struct.pack('4b', *x))[0]


def NewBuffIO(data):
    b = BufferIO(False)
    b.Write(data)
    return b


if __name__ == '__main__':
    import struct

    x = [10, -41, -119, 65]
    l = list(x)
    a = struct.unpack('<f', struct.pack('4b', *x))[0]

    bufio = BufferIO(False)
    bufio.Write(b'1111111111')
    bufio.Write(b'2222222222')

    bufio.Next(1)
    pass
