# -*- utf-8 -*-
from src.toolComponents.pool.ThreadPool.ThreadPool import TaskThreadPool
from src.toolComponents.surveillance.CheckPoint import Check
from src.toolComponents.surveillance.Constant import CONSTANT, NoneObj
from src.toolComponents.task.Debug import Debug
from src.toolComponents.task.TaskManager import TaskManager


class Task(Check, Debug):
    # 防止单利模式下重复init
    un_inited = True
    properties = None
    thread_pool = TaskThreadPool().init()

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
            self.handle()
            return self
        else:
            return self

    def invoke_callback(self, *args):
        _cache = args[0]
        func = args[1]
        param = args[2]
        func(param.get("data"))
        _cache.pop_back(param.get("key"))

    def invoke(self, func, cache):
        param = cache.pop()
        while not isinstance(param, NoneObj):
            args = (cache, func, param)
            self.thread_pool.add(self.invoke_callback, params=args)
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
