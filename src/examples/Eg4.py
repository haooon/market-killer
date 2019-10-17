# -*- utf-8 -*-

# ###################################################################################
# 关于 TaskManager                                                                ###
# ###################################################################################
# TaskManager 用于所有 Task 的创建的管理
# Quartz 继承自 Task 也属于 TaskManager 管理范围

from src.toolComponents.quartz.Quartz import Quartz
from src.toolComponents.task.Task import Task
from src.toolComponents.task.TaskManager import TaskManager


# 创建 Test1 任务
class Test1(Quartz):
    def loop(self):
        pass


# 创建 Test2 任务挂载 Test1 任务
class Test2(Task):
    def mount(self):
        Test1().init(self.KEY)


# 创建 Main 任务 挂载 Test1 和 Test2 任务
class Main(Task):
    def mount(self):
        self.task = TaskManager().init()
        Test1().init(self.KEY)
        Test2().init(self.KEY)

    def handle(self):
        print(self.task.get_task_dict())

if __name__ == '__main__':
    # 初始化 Main任务
    # 框架中最大的任务 只能为 Main 任务， 其余任务均嵌套在 Main 下
    # 拼写不能错 Main 方便可视化管理监控任务树
    Main().init()

