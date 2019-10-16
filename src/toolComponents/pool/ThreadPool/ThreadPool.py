# -*- utf-8 -*-
from concurrent.futures.thread import ThreadPoolExecutor
from typing import Callable

from src.toolComponents.decorator.Decorator import Singleton
from src.toolComponents.surveillance.Constant import CONSTANT


@Singleton
class TaskThreadPool:
    __pool = {}
    __executor = None

    def init(self):
        self.__executor = ThreadPoolExecutor(max_workers=CONSTANT.TASK.POOL_MAX_SIZE)

    def add(self, func, params=None):
        if not isinstance(func, Callable):
            self.error(func, " is not Callable")
        else:
            if params is None:
                self.__executor.submit(func)
            else:
                self.__executor.submit(func, params)

