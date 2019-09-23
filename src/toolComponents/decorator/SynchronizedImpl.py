# -*- coding:utf-8 -*-
import threading


# 线程安全 装饰器
def Synchronized(func):
    func.__lock__ = threading.Lock()

    def sync(*args, **kws):
        with func.__lock__:
            return func(*args, **kws)

    return sync
