# -*- utf-8 -*-
from src.toolComponents.pool.ThreadPool.ThreadPool import TaskThreadPool
from src.toolComponents.surveillance.CheckPoint import Check
from src.toolComponents.surveillance.Constant import CONSTANT, NoneObj
from src.toolComponents.task.Debug import Debug
from src.toolComponents.task.TaskManager import TaskManager
import time

class Task(Check, Debug):
    # 防止单利模式下重复init
    __un_inited = True
    # 配置参数
    properties = None
    # 数据缓存通道
    __cache_channel = {}
    # 线程池(global)
    thread_pool = TaskThreadPool().init()

    IN = None
    OUT = None

    def get_cache(self, channel_name) -> object:
        return self.__cache_channel.get(channel_name)

    def load_cache(self, channel_name, cache, delay=None) -> None:
        #  生产者延迟数
        if delay is not None:
            time.sleep(delay)
        self.__cache_channel[channel_name] = cache

    def active(self, *args, **kwargs):
        delay = kwargs.get("delay")
        # 调用参数
        if self.IN is None:
            pass
        else:
            param = self.IN.get()
            while True:
                #  消费者延迟数
                if delay is not None:
                    time.sleep(delay)
                else:
                    future = self.thread_pool.add(self.run, params=param)
                    future_list.append(future)
                    for future in futures.as_completed(
                            future_list):  # 通过result()方法获取结果 res = future.result() print(res, future) result.append(res)
                    self.IN["confirm"]()
                    param = self.self.IN["pop"]()

    def init(self, *args, **kwargs):
        if self.__un_inited:
            self.__un_inited = False
            __manager = TaskManager()
            self.properties = {}
            self.__cache_channel = {}
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

    def continued_invoke(self, func, cache, delay=None):
        param = cache.pop()
        while True:
            #  消费者延迟数
            if delay is not None:
                time.sleep(delay)
            if isinstance(param, NoneObj):
                param = cache.pop()
                continue
            else:
                args = (cache, func, param)
                self.thread_pool.add(self.invoke_callback, params=args)
                param = cache.pop()

    def mount(self):
        pass

    def run_background(self, method, args=None):
        self.thread_pool.add(method, params=args)

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
