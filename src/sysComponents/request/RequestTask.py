# -*- utf-8 -*-
from src.toolComponents.task.Task import Task
from bs4 import BeautifulSoup
import random
import requests

class RequestTask(Task):
    proxies = {'http': 'http://localhost:1080', 'https': 'http://localhost:1080'}
    url = 'http://www.baidu.com'
    baidu = requests.post(url, verify=False)
    print(baidu.content)
    pass