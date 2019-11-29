# -*- utf-8 -*-
import time
from concurrent import futures
from concurrent.futures.thread import ThreadPoolExecutor

def download_one(cc):
    time.sleep(5)
    return cc

def download_many(cc_list):
    executor = ThreadPoolExecutor(max_workers=5)
    future_list = []
    for cc in cc_list:
        # 使用submit提交执行的函数到线程池中，并返回futer对象（非阻塞）
        future = executor.submit(download_one, cc)
        future_list.append(future)
    return future_list

future_list = download_many(["aa", "bb", "cc"])
print("finish thread pool")
result = []
# as_completed方法传入一个Future迭代器，然后在Future对象运行结束之后yield Future
for future in futures.as_completed(future_list):
    # 通过result()方法获取结果
    res = future.result()
    print(res, future)
    result.append(res)