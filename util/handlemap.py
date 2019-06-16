# coding=utf8
# __author__ = 'doc007'

from abc import ABCMeta, abstractmethod


class CallMap(metaclass=ABCMeta):

    def __init__(self):
        self.funcDict = {}
        self.Register()

    def bind(self, cmd, Func):
        if not cmd in self.funcDict:
            self.funcDict.update({cmd: Func})

    @abstractmethod
    def Register(self):
        pass

    # 执行  交给具体的处理函数
    def Execute(self, cmd, *Args):
        if cmd in self.funcDict:
            self.funcDict.get(cmd)(*Args)
    #     else:
    #         LogManager.WRITE_LOG(LogLevel.ERROR, u"Handle %s :找不到对应的处理方法" % Handle, None)



if __name__ == '__main__':
    pass
