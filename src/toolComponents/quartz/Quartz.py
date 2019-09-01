# -*- coding:utf-8 -*-
from src.toolComponents.quartz.QuartzManager import QuartzManager
from src.toolComponents.task.Task import Task
import schedule
import threading
import uuid


class Quartz(Task):

    # 引入检查点
    CheckPoint = Task.CheckPoint
    # 时钟线程 在无延迟模式使用
    __quartz = None
    quartz = {
        # 唯一id
        "key": None,
        # 定时器名（可重复，不建议重复）
        "name": None,
        # 定时器描述
        "describe": None,
        # 定时器是否延时模式
        "delay": False,
        # 定时器运行时间间隔
        "interval": None
    }

    # 循环函数
    # *** 修改需要继承后重写 ***
    def loop(self):
        pass

    def thread_loop(self):
        threading.Thread(target=self.loop).start()

    def __init__(*args):
        self = args[0]
        if args.__len__() > 1:
            super(Quartz, self).__init__(args[1])
        else:
            super(Quartz, self).__init__()
        self.quartz_manager = QuartzManager()
        # 判断是否延迟模式
        if "delay" in self.quartz.keys():
            if self.quartz["delay"]:
                # schedule 延迟模式
                schedule.every(self.quartz["interval"]).seconds.do(self.loop)
            else:
                # schedule 非延迟模式 线程模式
                schedule.every(self.quartz["interval"]).seconds.do(self.thread_loop)
        else:
            schedule.every(self.quartz["interval"]).seconds.do(self.thread_loop)
        # self.__quartz = threading.Thread(target=self.run, args=())
        # self.__quartz.start()
        # 注册定时器

        # 绑定时钟对象
        # self.quartzManager.register(self.quartz)

    # 获取定时器线程
    def getQuartz(self):
        return self.__quartz
