# -*- coding:utf-8 -*-
import uuid

from src.toolComponents.quartz.QuartzManager import QuartzManager
from src.toolComponents.task.Task import Task
import schedule
import threading


class Quartz(Task):

    # 引入检查点
    CheckPoint = Task.CheckPoint
    # 时钟线程 在无延迟模式使用
    __quartz = None
    __threat_quartz = None
    quartz = {}

    # 循环函数
    # *** 修改需要继承后重写 ***
    def loop(self):
        pass

    def thread_loop(self):
        self.__threat_loop = threading.Thread(target=self.loop).start()

    def __init__(self, *args,  **kwargs):
        self.quartz_manager = QuartzManager()
        # reset quartz info
        self.quartz = {}
        # 默认5秒执行
        if "interval" not in self.quartz.keys():
            self.quartz["interval"] = 5
        super().__init__(**kwargs)
        # 判断是否延迟模式
        if "delay" in self.quartz.keys():
            if self.quartz["delay"]:
                # schedule 延迟模式
                self.__quartz = schedule.every(self.quartz["interval"]).seconds.do(self.loop)
                self.quartz["quartz"] = self.__quartz
                self.quartz["delay"] = True
            else:
                # schedule 非延迟模式 线程模式
                self.__threat_quartz = schedule.every(self.quartz["interval"]).seconds.do(self.thread_loop)
                self.quartz["quartz"] = self.__threat_quartz
                self.quartz["delay"] = False
        else:
            self.__threat_quartz = schedule.every(self.quartz["interval"]).seconds.do(self.thread_loop)
            self.quartz["quartz"] = self.__threat_quartz
            self.quartz["delay"] = False
        # 注册定时器
        # 绑定时钟对象
        if "name" not in self.quartz.keys():
            self.quartz["name"] = self.__class__.__name__
        if "describe" not in self.quartz.keys():
            self.quartz["describe"] = self.quartz["name"] + ": " + str(self.quartz["quartz"])
        self.quartz["key"] = str(uuid.uuid1())
        self.quartz_manager.register(self.quartz)

    # 获取定时器线程
    def getQuartz(self):
        return self.__quartz
