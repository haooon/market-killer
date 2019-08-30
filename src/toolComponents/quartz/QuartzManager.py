# -*- coding:utf-8 -*-
import threading
import schedule
from src.toolComponents.pool.ContentPool.ContentPool import ContentPool
from src.toolComponents.decorator.Decorator import *


# 定时器管理工具 继承定时器接口
@Singleton
class QuartzManager:
    # 用于注册定时器
    __contentPool = None

    # 初始化管理工具
    # 初始化内容池
    # 初始化定时器
    def __init__(self):
        self.__contentPool = ContentPool()
        threading.Thread(target=self.run).start()

    def getCommonQuartz(self):
        return self.__contentPool.getCommonArray()

    def run(self):
        while True:
            schedule.run_pending()

    # 注册新的定时器
    def register(self, quartz):
        self.__contentPool.insertCommonArray(quartz["key"], quartz)
        args = quartz["param"][0]
        kwargs = quartz["param"][1]
        if "delay" in quartz.keys():
            if quartz["delay"]:

                # schedule 延迟模式
                def delay():
                    quartz["func"](args, kwargs)

                schedule.every(quartz["interval"]).seconds.do(delay)
            else:
                # schedule 非延迟模式 线程模式
                def thread_model():
                    threading.Thread(target=quartz["func"], args=(args, kwargs,)).start()

                schedule.every(quartz["interval"]).seconds.do(thread_model)
        else:
            def thread_model():
                threading.Thread(target=quartz["func"], args=(args, kwargs,)).start()

            schedule.every(quartz["interval"]).seconds.do(thread_model)
