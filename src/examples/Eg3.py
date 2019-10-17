# -*- utf-8 -*-
from src.toolComponents.pool.ThreadPool.ThreadPool import TaskThreadPool
from src.toolComponents.quartz.Quartz import Quartz

# 集成Quartz基类 创建定时任务
class Test(Quartz):
    # 重写loop方法 定时逻辑 默认5秒定时
    def loop(self):
        self.print("quartz logic service run here")




class Test2(Quartz):
    quartz_properties = {"interval": 1}
    def loop(self):
        self.print("quartz logic service run here")

if __name__ == '__main__':
    # 初始化线程池
    TaskThreadPool().init()
    # # 初始化任务
    t = Test().init()
    t = Test2().init()