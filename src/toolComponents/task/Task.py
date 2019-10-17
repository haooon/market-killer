# -*- utf-8 -*-
from src.toolComponents.decorator.Decorator import Red, Blue, Yellow, Black
from src.toolComponents.pool.ThreadPool.ThreadPool import TaskThreadPool
from src.toolComponents.surveillance.CheckPoint import Check
from src.toolComponents.surveillance.Constant import CONSTANT, NoneObj
from src.toolComponents.task.TaskManager import TaskManager


class Task(Check):
    # 防止单利模式下重复init
    un_inited = True
    properties = None

    def init(self, *args, **kwargs):
        if self.un_inited:
            self.un_inited = False
            __manager = TaskManager()
            self.properties = {}
            if args.__len__() == 0:
                if "father" in kwargs.keys():
                    father_key = kwargs["father"]
                    self.KEY = __manager.register(self, father_key)
                else:
                    self.KEY = __manager.register(self)
            else:
                father_key = args[0]
                self.KEY = __manager.register(self, father_key)
            self.mount()
            TaskThreadPool().add(self.handle)
            return self
        else:
            return self

    @Black
    def print(self, *args):
        if CONSTANT.DEBUG:
            info = ""
            for arg in args:
                info += str(arg)
            return "[DEBUG::PRINT] ==> " + "[" + self.__class__.__name__ + "] >>> " + str(info)

    @Yellow
    def debug(self, *args):
        if CONSTANT.DEBUG:
            info = ""
            for arg in args:
                info += str(arg)
            return "[DEBUG::INFOO] ==> " + "[" + self.__class__.__name__ + "] >>> " + str(info)

    @Blue
    def blue(self, *args):
        if CONSTANT.DEBUG:
            info = ""
            for arg in args:
                info += str(arg)
            return "[DEBUG::BLUEE] ==> " + "[" + self.__class__.__name__ + "] >>> " + str(info)

    @Red
    def error(self, *args):
        info = ""
        for arg in args:
            info += str(arg)
        return "[DEBUG::ERROR] ==> " + "[" + self.__class__.__name__ + "] >>> " + str(info)

    def invoke(self, func, cache):
        param = cache.pop()
        while not isinstance(param, NoneObj):
            func(param.get("data"))
            cache.pop_back(param["key"])
            param = cache.pop()

    def mount(self):
        pass

    def handle(self):
        pass

    def __init__(self):
        super().__init__()

    CheckPoint = Check.CheckPoint
    KEY = None

    def get_info(self):
        return self.info

    def __del__(self):
        # self.print("del object")
        pass
