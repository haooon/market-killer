# -*- coding:utf-8 -*-

import time
import uuid

import schedule

from src.toolComponents.quartz.Quartz import Quartz
from src.toolComponents.quartz.QuartzManager import QuartzManager
from src.toolComponents.surveillance.Constant import CONSTANT

manager = QuartzManager()


class quartzTest(Quartz):
    quartz = {
        # 唯一id
        "key": None,
        # 定时器名（可重复，不建议重复）
        "name": "test quartz",
        # 定时器描述
        "describe": "test quartz test",
        # 定时器是否延时模式
        "delay": False,
        # 定时器运行时间间隔
        "interval": 1
    }


    def get(self):
        print("test test test")
        return CONSTANT.CHECKPOINT.HAPPY

    # delay = True
    @Quartz.CheckPoint("quartz")
    def loop(self):
        self.get()
        print("test quartz")



quartzTest()
time.sleep(10)