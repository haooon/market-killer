from concurrent.futures import ThreadPoolExecutor, as_completed
import time

# 参数times用来模拟网络请求的时间
def get_html(times):
    time.sleep(times)
    print("get page {}s finished".format(times))
    return times


print(get_html)
executor = ThreadPoolExecutor(max_workers=2)
urls = [2, 2, 2, 2, 2, 2,] # 并不是真的url
all_task = [executor.submit(get_html, (url)) for url in urls]


url = [2,2,]
for u in url:
    print(executor.submit(get_html, (u)))

# for future in as_completed(all_task):
#     data = future.result()
    # print("in main: get page {}s success".format(data))