# -*- utf-8 -*-
import threading
import time

from src.creep.sysTask.SysTask import SysTask
from src.creep.task.ItemCollectionTask.ItemCollectionTask import ItemCollectionTask
from src.sysComponents.api.Api import Api
from src.sysComponents.mongo.MongoTask import MongoMongo
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
            MongoMongo().init(self.KEY)
            SysTask().init(self.KEY)
            ItemCollectionTask().init(self.KEY)
            # quartzTest().init(self.KEY)
            self.run_flag = True
            return "Task started"


    def mount(self):
        api = Api().init(self.KEY)
        time.sleep(5)
        self.run()


