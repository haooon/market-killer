# -*- utf-8 -*-
import time

from src.toolComponents.surveillance.Constant import CONSTANT
from src.toolComponents.task.TaskInterface import Task


class TestTasks(Task):

    @Task.CheckPoint("get_data_correct")
    def get_data_correct(self, param):
        print(param)
        for i in range(1000000):
            self.runLoop(i)
        return CONSTANT.CHECKPOINT.HAPPY

    # @Task.CheckPoint("runLoop")
    def runLoop(self, i):
        pass
        # print(i)
        return CONSTANT.CHECKPOINT.HAPPY


tools = TestTasks()
timesum = 0
for i in range(10):
    time1 = time.time()
    tools.get_data_correct("start")
    time2 = time.time()
    timesum += time2 - time1
print(timesum/10)
tools.get_class_health()
tools.get_points_history()