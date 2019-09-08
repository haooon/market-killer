# -*- utf-8 -*-
from src.toolComponents.surveillance.CheckPoint import Check
from src.toolComponents.task.TaskManager import TaskManager


class Task(Check):
    info = None
    def init(self, *args, **kwargs):
        self.info = {}
        if args.__len__() == 0:
            if "father" in kwargs.keys():
                father_key = kwargs["father"]
                __manager = TaskManager()
                self.KEY = __manager.register(self, father_key)
            else:
                __manager = TaskManager()
                self.KEY = __manager.register(self)
        else:
            father_key = args[0]
            __manager = TaskManager()
            self.KEY = __manager.register(self, father_key)
        pass
        self.mount()
        return self

    def mount(self):
        pass

    def __init__(self):
        super().__init__()

    CheckPoint = Check.CheckPoint
    KEY = None

    def get_info(self):
        return self.info

    def __del__(self):
        print("del")
