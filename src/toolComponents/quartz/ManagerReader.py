# -*- coding:utf-8 -*-
from src.toolComponents.quartz.Quartz import BasicQuartz
import uuid


class ManagerReader(BasicQuartz):
    def __init__(self):
        super().__init__()
        print("managerReader inited")

    __quartzBuffer = None
    quartz = {
        "interval": 1,
        "name": "Manager Reader",
        "key": uuid.uuid1(),
        "content": {
            "describe": "Quartz Manager Reader",
        }
    }

    def loop(self):
        # print(self.quartzManager.getCommonQuartz())
        self.__quartzBuffer = self.quartzManager.getCommonQuartz()

    def getQuartz(self):
        return self.quartzManager.getCommonQuartz()
