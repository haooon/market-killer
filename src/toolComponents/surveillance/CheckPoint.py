# -*- utf-8 -*-

# @Author: haooon
# @Date: 2019/8/26
# @name: Class Function level surveillance Decorator
# self      obj     indicate self.
# name      str     indicate check point method
# expect for check whether the result(return value) from decorated function is
# correct
"""
class TestTask(Task):
    @Task.Check(self, name="")
    def get_data(self, param)
        cursor.fetch() ... ...
        if ... :
            return CONSTANT.CHECKPOINT.HAPPY
        else:
            CONSTANT.CHECKPOINT.SAD
"""
from src.toolComponents.List.LenLimitList import LenLimitList
from src.toolComponents.decorator.Decorator import Singleton
import time

from src.toolComponents.surveillance.Constant import CONSTANT


def checkPoint(name="default", correct=None):
    def check_expect(func):
        def wrapper(*args, **kwargs):
            # 第一位传入参数为self 为继承了 Task类 的任务类
            # 因为 Task类 继承了 Check类 所以可用self调用 Check类中方法
            # 这里目的是保存Check类状况
            task_class = args[0]
            if func(*args, **kwargs) == CONSTANT.CHECKPOINT.HAPPY:
                task_class.check(name, CONSTANT.CHECKPOINT.HAPPY)
                # print("id:", id(args[0]))
                # print("args:", args[0])
                # print("kwargs:", kwargs)
            else:
                task_class.check(name, CONSTANT.CHECKPOINT.SAD)

        return wrapper

    return check_expect


class Check:
    __check_points = None
    __check_list = None

    # 注入装饰器 减少import
    CheckPoint = checkPoint

    def __init__(self):
        self.__check_points = {}
        self.__check_list = LenLimitList(CONSTANT.CHECKPOINT.CHECK_MAX_HISTORY)

    def __add_point_check(self, name, health):
        self.__add_point(name)
        self.__check_points[name]['check_list'].append({"time": time.time(), "health": health})

    def __add_point(self, name):
        # 1.存数据库 待解决
        # 2.容量控制 待解决
        if name in self.__check_points.keys():
            return
        else:
            self.__check_points[name] = {"check_list": LenLimitList(CONSTANT.CHECKPOINT.POINT_MAX_HISTORY)}
            return

    # 主入口
    def check(self, name, health):
        self.__add_point_check(name, health)
        self.__check_list.append({"name": name, "time": time.time(), "health": health})

    def get_class_health(self):
        if CONSTANT.DEBUG:
            print(self.__check_list)
        return self.__check_list

    def get_points_history(self):
        if CONSTANT.DEBUG:
            print(self.__check_points)
        return self.__check_points
