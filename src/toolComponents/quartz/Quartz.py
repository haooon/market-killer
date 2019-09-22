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
    quartz_info = {}

    # 循环函数
    # *** 修改需要继承后重写 ***
    def loop(self):
        pass

    def thread_loop(self):
        self.__threat_loop = threading.Thread(target=self.loop).start()

    def __init__(self, *args,  **kwargs):
        super().__init__(*args, **kwargs)
        self.quartz_manager = QuartzManager()
        # reset quartz info
        # 默认5秒执行
        if "interval" not in self.quartz_info.keys():
            self.quartz_info["interval"] = 5
        # 判断是否延迟模式
        if "delay" in self.quartz_info.keys():
            if self.quartz_info["delay"]:
                # schedule 延迟模式
                self.__quartz = schedule.every(self.quartz_info["interval"]).seconds.do(self.loop)
                self.quartz_info["type"] = "delay quartz"
                self.quartz_info["delay"] = True
            else:
                # schedule 非延迟模式 线程模式
                self.__quartz = schedule.every(self.quartz_info["interval"]).seconds.do(self.thread_loop)
                self.quartz_info["type"] = "threat quartz"
                self.quartz_info["delay"] = False
        else:
            self.__quartz = schedule.every(self.quartz_info["interval"]).seconds.do(self.thread_loop)
            self.quartz_info["type"] = "threat quartz"
            self.quartz_info["delay"] = False
        # 注册定时器
        # 绑定时钟对象
        if "name" not in self.quartz_info.keys():
            self.quartz_info["name"] = self.__class__.__name__
        if "describe" not in self.quartz_info.keys():
            self.quartz_info["describe"] = self.quartz_info["name"] + ": " + str(self.__quartz)
        self.quartz_info["key"] = str(uuid.uuid1())
        self.quartz_manager.register(self.quartz_info, self.__quartz)

    # 获取定时器线程
    def getQuartz(self):
        return self.__quartz
