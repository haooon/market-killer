# -*- coding:utf-8 -*-
from src.toolComponents.quartz.BasizQuartz import BasicQuartz
import uuid

from src.toolComponents.quartz.test.quartzTest import quartzTest


class ManagerReader(BasicQuartz):
    quartz = {
        "interval": 2,
        "name": "Manager Reader",
        "key": uuid.uuid1(),
        "content": {
            "describe": "Quartz Manager Reader",
        }
    }
    def loop(self):
        print(self.quartzManager.getCommonQuartz())

quartzTest()
ManagerReader()