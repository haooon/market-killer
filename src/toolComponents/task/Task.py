# -*- utf-8 -*-
from src.toolComponents.surveillance.CheckPoint import Check
from src.toolComponents.surveillance.Constant import CONSTANT
from src.toolComponents.task.TaskManager import TaskManager


class Task(Check):
    info = None
    def init(self, *args, **kwargs):
        __manager = TaskManager()
        self.info = {}
        if args.__len__() == 0:
            if "father" in kwargs.keys():
                father_key = kwargs["father"]
                self.KEY = __manager.register(self, father_key)
            else:
                self.KEY = __manager.register(self)
        else:
            father_key = args[0]
            self.KEY = __manager.register(self, father_key)
        self.mount()
        self.handle()
        return self

    def print(self, content):
        if CONSTANT.DEBUG:
            print("[DEBUG] ==> " + str(content))

    def mount(self):
        pass

    def handle(self):
        pass

    def __init__(self):
        super().__init__()

    CheckPoint = Check.CheckPoint
    KEY = None

    def get_info(self):
        return self.info

    def __del__(self):
        self.print("del object")
