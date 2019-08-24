# -*- coding:utf-8 -*-

import time
import uuid

from src.toolComponents.quartz.BasizQuartz import BasicQuartz


class quartzTest(BasicQuartz):
    quartz = {
        "interval": 1,
        "name": "11111test",
        "key": uuid.uuid1(),
        "content": {
            "describe": "11111test quartz",
        }
    }
    # delay = True
    def loop(self):
        print("1111111111111111111111111111")