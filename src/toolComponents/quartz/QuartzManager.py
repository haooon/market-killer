# -*- coding:utf-8 -*-
import threading
import schedule
from src.toolComponents.pool.ContentPool.ContentPool import ContentPool
from src.toolComponents.decorator.Decorator import *


# 定时器管理工具 继承定时器接口
@Singleton
class QuartzManager:
    # 用于注册定时器
    __quartz_dict = {}

    # 初始化管理工具
    # 初始化内容池
    # 初始化定时器
    def __init__(self):
        self.__quartz_dict = {}
        threading.Thread(target=self.run).start()

    def get_quartz_dict(self):
        return self.__quartz_dict

    def run(self):
        while True:
            schedule.run_pending()

    # 注册新的定时器
    def register(self, quartz):
        key = quartz["key"]
        self.__quartz_dict[key] = quartz