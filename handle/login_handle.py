# coding=utf8
# __author__ = 'doc007'


from util.handlemap import CallMap


map = CallMap(104)

@map.route(0x0B)
def cmd_11(conn, bIO):
    conn.SendData(b"11111111111111")
    conn.SendData(b"11111111111111")

