# -*- utf-8 -*-
import random

from src.toolComponents.task.Task import Task
from bs4 import BeautifulSoup
import requests
import urllib

class ProxyPoolTask(Task):
    headers = {
        "Cookie": '_free_proxy_session=BAh7B0kiD3Nlc3Npb25faWQGOgZFVEkiJTBiMTU4NjU0NzBmYzIwMGI3NTgwYmM4NzZlNGI4M2MwBjsAVEkiEF9jc3JmX3Rva2VuBjsARkkiMVBoUzJUSEQ1eERUK3VsdE5LUVNLbm5yWHR4NThRMThhM0JNbUtObW52Vlk9BjsARg%3D%3D--ffc164116ca44528f7ea23e5891298b9e844c9d7; Hm_lvt_0cf76c77469e965d2957f0553e6ecf59=1568968970; Hm_lpvt_0cf76c77469e965d2957f0553e6ecf59=1568969007',
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": 'zh-CN,zh;q=0.9',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',

    }
    url = "http://www.xicidaili.com/nn/"
    ip_list = []

    def __getHTMLText(self, url, proxies):
        try:
            r = requests.get(url, proxies=proxies)
            r.raise_for_status()
            r.encoding = r.apparent_encoding
        except:
            return 0
        else:
            return r.text

    def __get_ip_list(self):
        web_data = requests.get(self.url, self.headers)
        print(web_data.content)
        soup = BeautifulSoup(web_data.text, 'html')
        ips = soup.find_all('tr')
        ip_list = []
        for i in range(1, len(ips)):
            ip_info = ips[i]
            tds = ip_info.find_all('td')
            ip_list.append(tds[1].text + ':' + tds[2].text)
        # 检测ip可用性，移除不可用ip：（这里其实总会出问题，你移除的ip可能只是暂时不能用，剩下的ip使用一次后可能之后也未必能用）
        for ip in ip_list:
            try:
                proxy_host = "https://" + ip
                proxy_temp = {"https": proxy_host}
                res = urllib.urlopen(self.url, proxies=proxy_temp).read()
            except Exception as e:
                ip_list.remove(ip)
                continue
        return ip_list

    def get_proxy(self):
        proxy_list = []
        for ip in self.ip_list:
            proxy_list.append('http://' + ip)
        proxy_ip = random.choice(proxy_list)
        proxies = {'http': proxy_ip}
        return proxies

    def handle(self):
        self.url = 'http://www.xicidaili.com/nn/'
        self.ip_list = self.__get_ip_list()

proxy = ProxyPoolTask().init()
for i in range(10):
    print(proxy.get_proxy())