# -*- utf-8 -*-
# 连接器接口
# 用于连接 cache task端的输入输出 IN OUT
from types import MethodType,FunctionType

class Connector:
    memory = None
    # 设置IN端 或OUT端
    def set(self, _memory):
        self.memory = _memory

    # 获取list里的值
    def __get_from_list(self):
        for i in self.memory:
            if "method Connector.get of" in i:
                # get 方法
                return
                pass
            else:
                # 其他所有  如：[1, 2, 3, 4, 5]
                # 直接返回 即可
                return i

    # 用于从IN端获取
    # cache端的Connector  不做处理
    # task端的Connector   从cache端pop值
    def get(self) -> object:
        if isinstance(self.memory, list):
            # 参数为列表
            return self.__get_from_list()
        else:
            # 单参数
            if isinstance(self.memory, MethodType):
                # memory方法为函数
                pass
        pass
    def push(self):
        pass

a = Connector()
print(str(a.get).replace("Connector", "1asdasdadasas"))
print(a.get.__class__)
print(a.get.__dict__)
print(a.get.__name__)
print(a.get.__module__)
print((a.get, Connector.get))