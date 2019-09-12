# -*- utf-8 -*-
import threading
import time

from src.sysComponents.api.Api import Api
from src.toolComponents.quartz.QuartzManager import QuartzManager
from src.toolComponents.quartz.test.quartzTest import quartzTest
from src.toolComponents.task.Task import Task
from src.toolComponents.task.TaskManager import TaskManager


class Main(Task):
    run_flag = False

    def handle(self):
        QuartzManager()

    def run(self):
        if self.run_flag != True:
            TaskManager()
            quartzTest().init(self.KEY)
            self.run_flag = True
            return "Task started"


    def mount(self):
        api = Api().init(self.KEY)
        time.sleep(5)
        self.run()

if __name__ == '__main__':
    Main().init()
    while True:
        pass
