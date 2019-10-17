# -*- utf-8 -*-
# ###################################################################################
# 关于 TaskThreadPool                                                             ###
# ###################################################################################
# 线程池 程序公用一个线程池
# 同时最大线程数在 CONSTANT 中设置
# 最大线程数外的线程任务会等待在队列中 稍后执行
import time

from src.toolComponents.cache.CacheTask import CacheTask
from src.toolComponents.pool.ThreadPool.ThreadPool import TaskThreadPool
from src.toolComponents.task.Task import Task


class Test(Task):
    def mount(self):
        self.cache = CacheTask().init(self.KEY)
        self.cache.load([1, 2, 3, 4, 5])

    def get(self, a):
        self.print(a)
        # 延时线程 测试线程池
        time.sleep(5)

if __name__ == '__main__':
    # 初始化线程池
    TaskThreadPool().init()
    # 初始化任务
    t = Test().init()
    # Task中invoke方法载入参数，调用函数
    t.invoke(t.get, t.cache)
