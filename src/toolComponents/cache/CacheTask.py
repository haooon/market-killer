# -*- utf-8 -*-
import uuid

from src.toolComponents.decorator.Decorator import Synchronized
from src.toolComponents.task.Task import Task


class CacheTask(Task):
    __waiting_cache = {}
    __suspended_cache = {}
    __running_cache = {}
    __running_count = 0

    def handle(self) -> None:
        # 初始化cache
        self.__cache = {}
        self.__count = 0
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
    def remove(self, key) -> None:
        self.__waiting_cache.pop(key)

    # suspend waiting task
    def suspend(self, key) -> None:
        self.__suspended_cache[key] = self.__waiting_cache[key]
        self.remove(key)

    # pop one task from waiting line
    @Synchronized
    def pop(self) -> object:
        return list(self.__waiting_cache.values())[0]

    # get waiting cache suspended cache and running cache
    def cache(self):
        self.print(self.__waiting_cache.__str__())

    pass
