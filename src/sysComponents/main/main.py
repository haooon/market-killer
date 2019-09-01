# -*- utf-8 -*-
from flask import Flask

from src.sysComponents.api.Api import Api
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

    def job(self):
        quartzTest()

    def __init__(self):
        super().__init__()
        task_manager = TaskManager()
        self.job()
        print(task_manager.get_task_dict())
        api = Api()


if __name__ == '__main__':
    Main()
    while True:
        pass
