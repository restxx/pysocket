# coding=utf-8
# __author__ = 'doc007'
import six
from abc import ABCMeta


@six.add_metaclass(metaclass=ABCMeta)
class CallMap(object):

    def __init__(self):
        self.Mid = None
        self.funcDict = {}

    def route(self, cmd):
        def dec(func):
            self.funcDict.update({cmd: func})

            def warp(*agrs, **kwargs):
                return func(*agrs, **kwargs)

            return warp

        return dec

    # 执行  交给具体的处理函数
    def Execute(self, cmd, *Args):
        if cmd in self.funcDict:
            self.funcDict.get(cmd)(*Args)

    #     else:
    #         LogManager.WRITE_LOG(LogLevel.ERROR, u"Handle %s :找不到对应的处理方法" % Handle, None)

    def __repr__(self):
        return "MID:{}".format(self.Mid)


if __name__ == '__main__':
    pass
