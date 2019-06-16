# coding=utf8
# __author__ = 'doc007'

from abc import ABCMeta, abstractmethod


class CallMap(metaclass=ABCMeta):

    def __init__(self):
        self.funcDict = {}
        self.register()

    def Bind(self, Handle, Func):
        if not Handle in self.funcDict:
            self.funcDict.update({Handle: Func})

    @abstractmethod
    def register(self):
        pass

    # 执行sql语句 把结果集 dict 交给具体的处理函数
    # def Execute(self, Handle, *Args):
    #     if Handle in self.funcDict:
    #         self.funcDict.get(Handle)(*Args)
    #     else:
    #         LogManager.WRITE_LOG(LogLevel.ERROR, u"Handle %s :找不到对应的处理方法" % Handle, None)



if __name__ == '__main__':
    pass
