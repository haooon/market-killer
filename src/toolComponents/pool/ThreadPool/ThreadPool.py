# -*- utf-8 -*-
from concurrent.futures.thread import ThreadPoolExecutor
from typing import Callable

from src.toolComponents.decorator.Decorator import Singleton
from src.toolComponents.surveillance.Constant import CONSTANT


@Singleton
class TaskThreadPool:
    __pool = {}
    __executor = None
    __uninit = True


    def init(self):
        if(self.__uninit):
            self.__executor = ThreadPoolExecutor(max_workers=CONSTANT.TASK.POOL_MAX_SIZE)
            self.__uninit = False
        return self

    def futurerrr(self, future):
        print(future)

    def add(self, func, params=None):
        if not isinstance(func, Callable):
            self.error(func, " is not Callable")
        else:
            if params is None:
                self.__executor.submit(func)
                # self.__executor.submit(self.futurerrr, future)
            else:
                self.__executor.submit(func, *params)
                # self.__executor.submit(self.futurerrr, future)

