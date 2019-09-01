# -*- coding:utf-8 -*-
import time

from src.toolComponents.quartz.Quartz import Quartz
from src.toolComponents.surveillance.Constant import CONSTANT
from src.toolComponents.task.Task import Task

class Trrrs(Task):
    info = {
        "name": "Trrrs",
        "status": CONSTANT.TASK.RUNNING,
        "health": 100
    }

class TestTasks(Task):
    # def __init__(self, fatherTask):
    #     print("self: ", self)
    #     super().__init__()
    #     # if kwargs["key"] != None:
    #     #     self.test = Trrrs(self.KEY)
    #     # else:
    #     self.test = Trrrs()

    info = {
        "name": "TestTasks",
        "status": CONSTANT.TASK.RUNNING,
        "health": 100
    }
    @Task.CheckPoint("get_data_correct")
    def get_data_correct(self, param):
        print(param)
        for i in range(10):
            self.runLoop(i)
        return CONSTANT.CHECKPOINT.HAPPY

    # @Task.CheckPoint("runLoop")
    def runLoop(self, i):
        pass
        # print(i)
        return CONSTANT.CHECKPOINT.HAPPY

class quartzTest(Quartz):
    # def __init__(self):
    #     super().__init__()
    #     print(self.KEY)
    info = {
        "name": "quartzTest",
        "status": CONSTANT.TASK.RUNNING,
        "health": 100
    }

    quartz = {
        # 唯一id
        "key": None,
        # 定时器名（可重复，不建议重复）
        "name": "test quartz",
        # 定时器描述
        "describe": "test quartz test",
        # 定时器是否延时模式
        "delay": False,
        # 定时器运行时间间隔
        "interval": 1
    }

    def get(self):
        # print("test test test")
        return CONSTANT.CHECKPOINT.HAPPY

    # delay = True
    @Quartz.CheckPoint("quartz test")
    def loop(self):
        TestTasks(self.KEY)
        self.get()
        # print("test quartz")
        return CONSTANT.CHECKPOINT.HAPPY


# from src.toolComponents.task.TaskManager import TaskManager
# # quartz_test = quartzTest()
# # mana = TaskManager()
# # print(mana.get_task_list())
# # time.sleep(2)
# # print(mana.get_task_dict())