# -*- coding:utf-8 -*-
from src.toolComponents.quartz.QuartzManager import QuartzManager
import schedule
import threading
import uuid

class BasicQuartz():
    # 定时器管理器
    quartzManager = QuartzManager()
    quartz = {
        # 时间间隔默认5秒
        # *** 修改需要继承后重写 ***
        "interval":5,
        # 延迟选项 非延迟 修改需要继承后重写
        "delay":False,
        "name":"default",
        "key":uuid.uuid1(),
        "content": {
            "describe":"default",
        }
    }
    # 时钟线程 在无延迟模式使用
    __quartz = None

    # 循环函数
    # *** 修改需要继承后重写 ***
    def loop(self):
        pass
    # 时钟定时器核心运行处
    # 延迟模式使用
    # 死锁等待
    def run(self):
        while True:
            schedule.run_pending()
    # 线程 时钟定时器核心运行处
    # 非延迟模式使用
    # 死锁等待
    def threadLoop(self):
        threading.Thread(target=self.loop, args=()).start()
    def __init__(self):
        # 判断是否延迟模式
        if "delay" in self.quartz.keys():
            if self.quartz["delay"]:
                # schedule 延迟模式
                schedule.every(self.quartz["interval"]).seconds.do(self.loop)
            else:
                # schedule 非延迟模式 线程模式
                schedule.every(self.quartz["interval"]).seconds.do(self.threadLoop)
        else:
            schedule.every(self.quartz["interval"]).seconds.do(self.threadLoop)
        self.__quartz = threading.Thread(target=self.run, args=())
        self.__quartz.start()

        # 注册定时器

        # 绑定时钟对象
        self.quartz["quartz"] = self
        self.quartzManager.register(self.quartz)

    # 获取定时器线程
    def getQuartz(self):
        return self.__quartz