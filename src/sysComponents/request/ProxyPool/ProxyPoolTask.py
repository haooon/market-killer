# -*- utf-8 -*-
import json

from src.sysComponents.mongo.MongoTask import MongoMongo
from src.toolComponents.surveillance.Constant import CONSTANT
from src.toolComponents.quartz.Quartz import Quartz
import requests
import random
import time


class ProxyPoolTask(Quartz):
    proxy_pool = None

    quartz_info = {
        "interval": 60 * 5
    }

    def loop(self):
        self.handle()
        pass

    def mount(self):
        pass

    def handle(self):
        self.proxy_pool = json.loads(requests.get(CONSTANT.PROXYPOOL.URL).content)["proxies"]
        for proxy in self.proxy_pool:
            self.print("load proxy: " + proxy['ip'] + ':' + str(proxy['port']))

    def get(self):
        proxy = self.print(self.proxy_pool[random.randint(0, self.proxy_pool.__len__())] - 1)
        return proxy

# proxy = ProxyPoolTask().init()
# for i in range(10):
#     proxy.get()

# 一定要设置Content-Type值为application/json
headers={}
page_max = 627
# headers['Content-Type']='application/json'
headers['Cookie']="_ga=GA1.2.1549448114.1565356207; _ntes_nnid=dd304631d7902d3bad049873a6270018,1566042562983; _ntes_nuid=dd304631d7902d3bad049873a6270018; csrf_token=6ad711bfb7082004872317bc396d13b5a4336c4a; game=csgo; _gid=GA1.2.393649929.1569057473; Locale-Supported=zh-Hans; _gat_gtag_UA_109989484_1=1; NTES_YD_SESS=t6fg6GSwvnZleW7tJK.1XIDJ5Gntd6iVKDHBL.vWUH.6uWdmu57zsxdx.dDQHJSXgy0Xm3LN91zkjgfKPBPEapXNnGoEBu2tHaSF5X6QdHfyct_D62uui9aDqxdnNwf9NF3DhMg_Yjx0wHWVw3MASLKMr4E5hf1O9aS_RUHVMkJKmkLZftakSfJkq9995yUbYLGv9SY5YuAMh80NwC0VqjiQEXK4KY_7wELk9K0qXx7jb; S_INFO=1569146666|0|3&80##|15510592723; P_INFO=15510592723|1569146666|1|netease_buff|00&99|bej&1567432959&netease_buff#bej&null#10#0#0|&0|null|15510592723; session=1-TdwJJmnPZQZHY31B_HnidGb_tcetUfw88zN0Vznft5Pa2043074918"
# url='https://buff.163.com/api/market/goods?game=csgo&page_num=' + page + '&_=1569210712802'
# data={"username":"ls","password":"toor"}
# 一定要用json.dumps把data格式化成json
# r = requests.post(url,headers=headers,data=json.dumps(data),verify=False)
# 或者直接使用json参数代替data，此时requests会自动进行格式化和设置Content-Type头的工作
# r = requests.get(url,headers=headers,verify=True)
# for i in json.loads(r.content)['data']['items']:
#     print(i)