# -*- utf-8 -*-
from src.toolComponents.cache.CacheTask import CacheTask
from src.toolComponents.pool.ThreadPool.ThreadPool import TaskThreadPool
from src.toolComponents.task.Task import Task

# 继承Task基类
class Test(Task):
    # 挂载参数cache
    def mount(self):
        # 参数cache初始化，挂入父级KEY（表示嵌套关系）
        self.cache = CacheTask().init(self.KEY)
        # 载入参数「1，2，3，4，5」 参数为 list 类型
        self.cache.load([1, 2, 3, 4, 5])

    # Test任务所提供的逻辑服务代码，需要参数
    def get(self, a):
        self.print(a)

if __name__ == '__main__':
    # 初始化线程池
    TaskThreadPool().init()
    # 初始化任务
    t = Test().init()
    # Task中invoke方法载入参数，调用函数
    t.invoke(t.get, t.cache)

# 需要多参数时 可load([[1,11,111], [2,22,222], [3,33,333]])
# 需要多参数时 可load([{"param1":1, "param2":2, "param3":3}])
# CONSTANT 中 CONSTANT.Cache.MAXSYN 值为 cache运行同时刻最大缓冲数