# coding=utf-8
# __author__ = 'doc007'

from handle.handle_map import HMAP
from util.callmap import CallMap

@HMAP.bind(11)
class loginMap(CallMap):
    pass


map = loginMap()

@map.route(22)
def cmd_11(conn, bIO):
    conn.SendData(b"11111111111111")
    conn.SendData(b"11111111111111")
