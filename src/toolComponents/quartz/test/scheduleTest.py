# -*- coding:utf-8 -*-
import threading
import time

import schedule

from src.toolComponents.quartz.Quartz import Quartz


def run():
    print("111111")

# a = schedule.every(1).second.do(run)

class testQuartz(Quartz):
    def loop(self):
        print("333333")


def ppp():
    # schedule.run_pending()
    while True:
        schedule.run_pending()
        pass

testQuartz()
threading.Thread(target = ppp).start()

# print(a)
# time.sleep(10)
# schedule.cancel_job(a)