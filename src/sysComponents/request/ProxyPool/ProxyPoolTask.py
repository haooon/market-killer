# -*- utf-8 -*-
import json

from src.toolComponents.surveillance.Constant import CONSTANT
from src.toolComponents.quartz.Quartz import Quartz
import requests
import random


class ProxyPoolTask(Quartz):
    proxy_pool = None

    quartz_info = {
        "interval": 60 * 5
    }

    def loop(self):
        self.pull()
        pass

    def mount(self):
        pass

    def pull(self):
        self.proxy_pool = json.loads(requests.get(CONSTANT.PROXYPOOL.URL).content)["proxies"]
        i = 0
        for proxy in self.proxy_pool:
            i += 1
            self.debug("load proxy(", i, "): ", proxy['ip'], ':', proxy['port'])

    def get(self):
        proxy = self.proxy_pool[random.randint(0, self.proxy_pool.__len__() - 1)]
        self.debug(proxy)
        return proxy


proxy = ProxyPoolTask().init()
for i in range(10):
    proxy.get()