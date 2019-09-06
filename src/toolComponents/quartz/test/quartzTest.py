# -*- coding:utf-8 -*-
import time

from src.toolComponents.quartz.Quartz import Quartz
from src.toolComponents.surveillance.Constant import CONSTANT
from src.toolComponents.task.Task import Task

class Trrrs(Task):
    pass

class TestTasks(Task):
    testrrr = None
    def mount(self):
        self.testrrr = Trrrs().init(self.KEY)
        self.testrrr = Trrrs().init(self.KEY)
        self.testrrr = Trrrs().init(self.KEY)

    info = {
        "name": "TestTasks",
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
    testTasks = None
    testTasks1 = None
    def mount(self):
        self.testTasks = TestTasks().init(self.KEY)

        self.tresrtrrr = Trrrs().init(self.KEY)
        self.testTasks1 = TestTasks().init(self.KEY)

    info = {
        "name": "quartzTest",
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
        self.get()
        # print("test quartz")
        return CONSTANT.CHECKPOINT.HAPPY


from src.toolComponents.task.TaskManager import TaskManager
quartz_test = quartzTest().init()
mana = TaskManager()
print(mana.get_task_list())

print(mana.get_task_dict())
print(TaskManager().health())

quartz_test.info["health"] = 0

print(mana.get_task_dict())
print(TaskManager().health())