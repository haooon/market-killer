# -*- utf-8 -*-
from src.toolComponents.cache.CacheTask import CacheTask
from src.toolComponents.pool.ThreadPool.ThreadPool import TaskThreadPool

a = {}
a["123"] = 123
a["222"] = 222
a["333"] = 333
a["444"] = 444
a["555"] = 555
a["666"] = 666

for i in range(a.__len__()):
    print(list(a.values())[i])

TaskThreadPool().init()
cache = CacheTask().init()
cache.add("a")
key = cache.add("b")
cache.add("c")
cache.cache()
print(cache.pop())
cache.add("d")
print(key)
cache.remove(key)
cache.cache()
