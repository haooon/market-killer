# -*- coding:utf-8 -*-
import uuid

from src.toolComponents.pool.ThreadPool.ThreadPool import TaskThreadPool
from src.toolComponents.quartz.QuartzManager import QuartzManager
from src.toolComponents.task.Task import Task
import schedule


class Quartz(Task):

    # 引入检查点
    CheckPoint = Task.CheckPoint
    # 时钟线程 在无延迟模式使用
    __quartz = None
    quartz_properties = {}

    # 循环函数
    # *** 修改需要继承后重写 ***
    def loop(self):
        pass

    def thread_loop(self):
        # self.__threat_loop = threading.Thread(target=self.loop).start()
        pool = TaskThreadPool()
        pool.add(self.loop)

    def __init__(self, *args,  **kwargs):
        super().__init__(*args, **kwargs)
        self.quartz_manager = QuartzManager()
        # reset quartz info
        # 默认5秒执行
        if "interval" not in self.quartz_properties.keys():
            self.quartz_properties["interval"] = 5
        # 判断是否延迟模式
        if "delay" in self.quartz_properties.keys():
            if self.quartz_properties["delay"]:
                # schedule 延迟模式
                self.loop()
                self.__quartz = schedule.every(self.quartz_properties["interval"]).seconds.do(self.loop)
                self.quartz_properties["type"] = "delay quartz"
                self.quartz_properties["delay"] = True
            else:
                # schedule 非延迟模式 线程模式
                self.thread_loop()
                self.__quartz = schedule.every(self.quartz_properties["interval"]).seconds.do(self.thread_loop)
                self.quartz_properties["type"] = "threat quartz"
                self.quartz_properties["delay"] = False
        else:
            self.thread_loop()
            self.__quartz = schedule.every(self.quartz_properties["interval"]).seconds.do(self.thread_loop)
            self.quartz_properties["type"] = "threat quartz"
            self.quartz_properties["delay"] = False
        # 注册定时器
        # 绑定时钟对象
        if "name" not in self.quartz_properties.keys():
            self.quartz_properties["name"] = self.__class__.__name__
        if "describe" not in self.quartz_properties.keys():
            self.quartz_properties["describe"] = self.quartz_properties["name"] + ": " + str(self.__quartz)
        self.quartz_properties["key"] = str(uuid.uuid1())
        self.quartz_manager.register(self.quartz_properties, self.__quartz)

    # 获取定时器线程
    def getQuartz(self):
        return self.__quartz
