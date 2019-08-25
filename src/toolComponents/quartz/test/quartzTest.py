# -*- coding:utf-8 -*-

import time
import uuid

from src.toolComponents.quartz.BasizQuartz import BasicQuartz


class quartzTest(BasicQuartz):
    def __init__(self):
        super().__init__()
        print("quartzTest inited")
    quartz = {
        "interval": 5,
        "name": "11111test",
        "delay": False,
        "key": str(uuid.uuid1()),
        "content": {
            "describe": "11111test quartz",
        }
    }
    # delay = True
    def loop(self):
        print("test quartz")