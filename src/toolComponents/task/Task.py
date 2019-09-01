# -*- utf-8 -*-
import uuid

from src.toolComponents.surveillance.CheckPoint import Check
from src.toolComponents.task.TaskManager import TaskManager


class Task(Check):
    def __init__(*args):
        print("Task init args:: ", args)
        self = args[0]
        if args.__len__() > 1:
            father_key = args[1]
            super(Task, self).__init__()
            __manager = TaskManager()
            self.KEY = __manager.register(self, father_key)
        else:
            super(Task, self).__init__()
            __manager = TaskManager()
            self.KEY = __manager.register(self)

    CheckPoint = Check.CheckPoint
    info = {
        "key": None,
        "name": "default",
        "status": None,
        "health": None
    }
    KEY = None

    def get_info(self):
        return self.info

    def __del__(self):
        print("del")
