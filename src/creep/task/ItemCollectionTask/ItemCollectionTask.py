# -*- utf-8 -*-
import json
import random
import time
import requests

from src.creep.sysTask.SysTask import SysTask
from src.sysComponents.mongo.MongoTask import MongoMongo
from src.toolComponents.quartz.Quartz import Quartz


class ItemCollectionTask(Quartz):
    total_page = 627
    total_count = 12533
    quartz_info = {
        # 24小时更新
        "interval": 60 * 60 * 24
    }

    header_pool = [
        "_ntes_nnid=1176171809d66c4ca967762dc9767fb9,1566534179292; _ntes_nuid=1176171809d66c4ca967762dc9767fb9; csrf_token=3e353cd8de55920d5f6005d53881765ab26de2a9; game=csgo; _ga=GA1.2.951113250.1569231272; _gid=GA1.2.1683707879.1569231272; NTES_YD_SESS=OQVgNd6Mt5.1MqGz2DEUf0Ldhgi9RcmOYbWHodsYKKMg2xCyAo0JcpVV.lDKRhk7DrHCtzo4uK4xB326q63sEcbL7LES4JkWta0Z.L9rM.XzwNM2RGAM9rlVo77bEC6rTkrguyMmWeS4NvDTSsINzGyILAULBkyPQgqzJS24m44uoWycQR18iJ5qNINiFeOtaxxm81Zyi2wJaIo13im6jo0y5jHc0XGk_hoUb0_zccZqn; S_INFO=1569231332|0|3&80##|17719495332; P_INFO=17719495332|1569231332|1|netease_buff|00&99|bej&1569210568&netease_buff#bej&null#10#0#0|&0|null|17719495332; session=1-pvcz9m5FwuvwYJEvVKIX0SvjMdfxhGUt5KahxhXONttm2043296940; Locale-Supported=zh-Hans; _gat_gtag_UA_109989484_1=1",
        "_ga=GA1.2.1549448114.1565356207; _ntes_nnid=dd304631d7902d3bad049873a6270018,1566042562983; _ntes_nuid=dd304631d7902d3bad049873a6270018; csrf_token=6ad711bfb7082004872317bc396d13b5a4336c4a; game=csgo; _gid=GA1.2.393649929.1569057473; Locale-Supported=zh-Hans; _gat_gtag_UA_109989484_1=1; NTES_YD_SESS=t6fg6GSwvnZleW7tJK.1XIDJ5Gntd6iVKDHBL.vWUH.6uWdmu57zsxdx.dDQHJSXgy0Xm3LN91zkjgfKPBPEapXNnGoEBu2tHaSF5X6QdHfyct_D62uui9aDqxdnNwf9NF3DhMg_Yjx0wHWVw3MASLKMr4E5hf1O9aS_RUHVMkJKmkLZftakSfJkq9995yUbYLGv9SY5YuAMh80NwC0VqjiQEXK4KY_7wELk9K0qXx7jb; S_INFO=1569146666|0|3&80##|15510592723; P_INFO=15510592723|1569146666|1|netease_buff|00&99|bej&1567432959&netease_buff#bej&null#10#0#0|&0|null|15510592723; session=1-TdwJJmnPZQZHY31B_HnidGb_tcetUfw88zN0Vznft5Pa2043074918"
    ]

    headers = {}

    # time_interval_stimulation = [7, 9, 8, 10, 15, 23, 14, 5, 6, 16, 33, 21, 17, 24, 11, 15, 5, 1, 8]
    time_interval_stimulation = [3, 4, 4, 2, 3, 3, 1, 4]
    mongo = None
    sys = None

    def loop(self):
        self.creep()

    def mount(self):
        self.mongo = MongoMongo()
        self.sys = SysTask()
        self.total_page = self.sys.get_item_collection_total_page()
        self.total_count = self.sys.get_item_collection_total_count()

    def creep(self):
        for i in range(129, self.total_page):
            page = str(i + 1)
            # 获取 物品 列表 url
            # url = 'https://buff.163.com/api/market/goods?game=csgo&page_num=' + page + '&_=' + str(int(round(time.time() * 1000)))
            url = 'https://buff.163.com/api/market/goods?game=csgo&page_num=' + page + '&sort_by=price.desc&_=' + str(int(round(time.time() * 1000)))
            # 时间间隔模拟 模拟人手点击访问
            # 提出到Task类
            interval = self.time_interval_stimulation[random.randint(0, self.time_interval_stimulation.__len__()) - 1]
            time.sleep(interval)
            self.print("interval: " + str(interval))

            self.headers['Cookie'] = self.header_pool[0]
            self.header_pool.reverse()
            r = requests.get(url, headers=self.headers, verify=True)
            data = json.loads(r.content)['data']

            # self.print(data)
            # 查看是否total_num变化 变多了会重新跑
            new_total_count = data['total_count']
            if self.total_count != new_total_count:
                self.print("item total count modified, total num: " + str(new_total_count))
                self.total_count = new_total_count
                self.sys.set_item_collection_total_count(new_total_count)
                # 判断页数是否发生变化
                new_total_page = data['total_page']
                if self.total_page != new_total_page:
                    self.print("item total page modified, total page: " + str(new_total_page))
                    self.total_page = new_total_page
                    self.sys.set_item_collection_total_page(new_total_page)
                    self.creep()
                    return

            for item in data['items']:
                select = self.mongo.select("item", query={'market_hash_name': item['market_hash_name']})
                self.print(item['id'])
                if select.__len__() > 0:
                    self.print("item repeat: " + str(item['market_hash_name']))
                else:
                    self.print("add item: " + str(item['market_hash_name']))
                    self.mongo.insert("item", item)
                    self.print("add item completed, item name: " + str(item['market_hash_name']))
            self.print("url: " + url)
            self.print("Cookie: " + self.header_pool[0])
            self.print("page: " + str(page) + " completed!")