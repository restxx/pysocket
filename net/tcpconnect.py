# coding=utf8
# __author__ = 'doc007'

import socket
from util.dec_warp import excepts


class TcpConnect(object):

    def __init__(self):
        self.__sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.__sock.setsockopt(socket.SOL_SOCKET, socket.SO_KEEPALIVE, 1)

    @excepts(__name__)
    def connect(self, address, port):
        return self.__sock.connect((address, port))

    @excepts(__name__)
    def recv_data(self, len=65535):
        return self.__sock.recv(len)

    @excepts(__name__)
    def sendall(self, data):
        return self.__sock.sendall(data)

    def close(self):
        self.__sock.close()


if __name__ == '__main__':
    pass
