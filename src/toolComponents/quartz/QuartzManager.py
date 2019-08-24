# -*- coding:utf-8 -*-
from src.toolComponents.pool.ContentPool.ContentPool import ContentPool
from src.toolComponents.decorator.Decorator import *

# 定时器管理工具 继承定时器接口
@Singleton
class QuartzManager():
    # 用于注册定时器
    __contentPool = None

    # 初始化管理工具
    # 初始化内容池
    # 初始化定时器
    def __init__(self):
        self.__contentPool = ContentPool()

    def getCommonQuartz(self):
        return self.__contentPool.getCommonArray()

    # 注册新的定时器
    def register(self,quartz):
        self.__contentPool.insertCommonArray(quartz["key"], quartz)

manager = QuartzManager()

