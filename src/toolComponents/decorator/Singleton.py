# -*- coding:utf-8 -*-
from src.toolComponents.decorator.Synchronized import Synchronized

# 单利类
def Singleton(cls):
    instances = {}
    @Synchronized
    def getInstance(*args, **kw):
        if cls not in instances:
            instances[cls] = cls(*args, **kw)
        return instances[cls]
    return getInstance