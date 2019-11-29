# -*- utf-8 -*-
import uuid

from src.toolComponents.decorator.Decorator import Synchronized
from src.toolComponents.surveillance.Constant import NoneObj
from src.toolComponents.task.Task import Task


class plugin:
    __data = None
    def __init__(self, data, cache):
        self.__data = data
        self.__cache = cache
    def get(self):
        return self.__data



class CacheTask(Task):
    __waiting_cache = {}
    __suspended_cache = {}
    __error_cache = {}
    __running_cache = {}
    __running_count = 0

    # obj -> [1,2,3,4,5]
    # obj -> Task.out
    IN = None
    # obj -> [1,2,3,4,5]
    OUT = None

    # load data by list
    def load(self, data_list):
        for data in data_list:
            self.add(data)

    def handle(self) -> None:
        self.IN = self.load
        self.OUT = {"pop": self.pop, "confirm": self.pop_confirm}
        self.__waiting_cache = {}
        self.__suspended_cache = {}
        self.__running_cache = {}
        self.__running_count = 0
        pass

    def mount(self):
        pass

    # add task to waiting line
    @Synchronized
    def add(self, obj) -> str:
        # hash用于唯一
        key = str(uuid.uuid1()).__str__()
        self.__waiting_cache[key] = obj
        return key

    # remove waiting task
    @Synchronized
    def remove(self, key) -> None:
        self.__waiting_cache.pop(key)

    # suspend waiting task
    @Synchronized
    def suspend(self, key) -> None:
        self.__suspended_cache[key] = self.__waiting_cache[key]
        self.remove(key)

    # pop one task from waiting line
    @Synchronized
    def pop(self) -> dict:
        cache_list = list(self.__waiting_cache.keys())
        if cache_list.__len__() is 0:
            return NoneObj()
        if self.__running_count >= cache_list.__len__():
            return NoneObj()
        key = cache_list[self.__running_count]
        # 从等待队列获取
        data = self.__waiting_cache.get(key)
        # 存入运行队列
        # self.__running_count += 1
        # self.__running_cache[key] = data
        # 从等待队列删除
        self.__waiting_cache.pop(key)
        return {"key": key, "data": data}

    # get waiting cache
    def waiting(self):
        return self.__waiting_cache.__str__()

    # get running cache
    # def running(self):
    #     return self.__running_cache.__str__()

    # get suspended cache
    def suspended(self):
        return self.__suspended_cache.__str__()

    # 错误
    def error(self, _data):
        key = _data.get("key")
        data = _data.get("data")
        # 错误信息
        msg = _data.get("msg")
        self.__error_cache[key] = {"data": data, "msg": msg}

    # 否定确认机制
    # 保证多消费者使用时不被重复处理
    # 决定采用错误重启机制
    # def pop_confirm(self, key):
    #     self.__waiting_cache.pop(key)

    # pop from cache and then pop back to update the running count
    # @Synchronized
    # def pop_back(self, key):
    #     self.__running_count -= 1
    #     self.__running_cache.pop(key)

    # def pop_cache(self):
    #     return