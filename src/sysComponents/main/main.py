# -*- utf-8 -*-
from flask import Flask

from src.sysComponents.api.Api import Api
from src.toolComponents.quartz.QuartzManager import QuartzManager
from src.toolComponents.quartz.test.quartzTest import quartzTest
from src.toolComponents.surveillance.Constant import CONSTANT
from src.toolComponents.task.Task import Task
from src.toolComponents.task.TaskManager import TaskManager


class Main(Task):
    info = {
        "name": "task manager",
        "status": CONSTANT.TASK.RUNNING,
        "health": 100
    }

    def run(self):
        quartzTest().init()
        api = Api().init(self.KEY)


if __name__ == '__main__':
    Main().init().run()
    while True:
        pass
