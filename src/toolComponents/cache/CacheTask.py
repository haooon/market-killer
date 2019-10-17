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
    __running_cache = {}
    __running_count = 0

    # load data by list
    def load(self, data_list):
        for data in data_list:
            self.add(data)

    def handle(self) -> None:
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
        if cache_list.__len__() == 0:
            return NoneObj()
        key = cache_list[self.__running_count]
        self.__running_count += 1
        return {"key": key, "data": self.__waiting_cache.get(key)}

    # get waiting cache suspended cache and running cache
    def cache(self):
        return self.__waiting_cache.__str__()

    # pop from cache and then pop back to update the running count
    @Synchronized
    def pop_back(self, key):
        self.__running_count -= 1
        self.__waiting_cache.pop(key)



    def pop_cache(self):
        return
