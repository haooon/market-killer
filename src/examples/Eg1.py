# -*- utf-8 -*-
from src.toolComponents.pool.ThreadPool.ThreadPool import TaskThreadPool
from src.toolComponents.task.Task import Task

# 继承Task基类
class Test(Task):
    # 任务初始化 一般用于挂载子任务
    def mount(self):
        self.blue("print blue  debug")
        self.print("print level debug")

    # 任务初始化 一般用于状态初始化
    def handle(self):
        self.debug("print debug debug")
        self.error("print error debug")

    def test(self):
        self.print("这个世界每天那么多擦肩而过 谢谢你停下脚步读懂我.")

if __name__ == '__main__':
    # 初始化线程池 线程池内容参考文档
    TaskThreadPool().init()
    # 初始化任务
    t = Test().init()
    # 使用任务逻辑服务
    t.test()
