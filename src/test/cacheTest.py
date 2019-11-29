# -*- utf-8 -*-
import time
from src.toolComponents.cache.CacheTask import CacheTask
from src.toolComponents.pool.ThreadPool.ThreadPool import TaskThreadPool
from src.toolComponents.task.Task import Task

#invoke()

# cache===B
# ------------------------------------
# link(cache.out, B.in)
#
#
# A===cache===B
# ------------------------------------
# link(A.out, cache.in)
# link(cache.out, B.in)
#
# 1.
# handle():
# 	for(i in self.cache("aaa"))
#
# 2.
# @Singleton
# CacheManager.link(xxx, xxx)
# CacheManager.create("aaa") -> return cache
# CacheManager.get("aaa") -> return cache
#
#
#
# 		 [===B
# A===cache[	...
# 		 [===C
# ------------------------------------
# link(cache.in, A.out)
# link(cache.out, [B.in, C.in])
#
#
#
# A===cacheA===]
# 	 ...	 ]===C
# B===cacheB===]
# ------------------------------------
# link(cache.in, A.out)
# link(cacheB.in, B.out)
# link(C.in, [cacheA.out, cacheB.out])
#
#
#
# A===cacheA===]===C
# 	...		 ]  ...
# B===cacheB===]===D
# ------------------------------------
# link(A.out, cacheA.in)
# link(B.out, cacheB.in)
# link(C.in, [cacheA.out, cacheB.out])
# link(D.in, [cacheA.out, cacheB.out])


class A(Task):
    def run(self):
        while True:
            time.sleep(3)
            cache = self.get_cache('test_cache')
            for i in range(100):
                cache.load([str(i) + 'a'])


class B(Task):
    def run(self, a):
        self.print(a)


if __name__ == '__main__':
    TaskThreadPool().init()
    cache = CacheTask().init()
    a = A().init()
    a.load_cache("test_cache", cache)
    a.run_background(a.run)
    b = B().init()
    b.load_cache("test_cache", cache)
    b.continued_invoke(b.run, b.get_cache('test_cache'))