# coding=utf-8
# __author__ = 'doc007'

from util.callmap import CallMap
from util.singleton import Singleton
from handle.handle_map import hMap

# 绑定主包头
@hMap.bind(11)
class LoginMap(CallMap, Singleton):
    pass


login = LoginMap()


# 绑定子包头
@login.route(22)
def cmd_11(conn, bIO):
    conn.SendData(b"11111111111111")
    conn.SendData(b"11111111111111")
