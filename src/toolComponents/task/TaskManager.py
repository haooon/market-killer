# -*- coding:utf-8 -*-
import uuid

from src.toolComponents.decorator.Decorator import Singleton
from src.toolComponents.surveillance.Constant import CONSTANT


@Singleton
class TaskManager:
    __main_key = None
    __task_dict = None
    __task_list = None
    properties = {
        "name": "task manager",
        "status": CONSTANT.TASK.RUNNING,
        "health": 100
    }

    def __init__(self):
        __main_key = ""
        self.__task_list = []
        self.__task_dict = []
        self.__task = {}

    def health(self):
        return self.get_task_health(self.get_task_dict())

    def get_task_health(self, task):
        tmplist = []
        sum = 0
        if task["properties"]["kids"].__len__() > 0:
            for son in task["properties"]["kids"]:
                tmplist.append(self.get_task_health(son))
        else:
             return task["properties"]["health"]
        for i in tmplist:
            sum += i
        task["properties"]["health"] = sum / tmplist.__len__()
        return task["properties"]["health"]

    def register(*args):
        self = args[0]
        task = args[1]
        task.properties["kids"] = []
        key = task.properties["key"] = str(uuid.uuid1())
        if "name" not in task.properties.keys():
            task.properties["name"] = task.__class__.__name__
        if "status" not in task.properties.keys():
            task.properties["status"] = CONSTANT.TASK.RUNNING
        if "health" not in task.properties.keys():
            task.properties["health"] = CONSTANT.TASK.BASIC_HEALTH
        if args.__len__() > 2:
            father_key = args[2]
            for tmp_task in self.__task_list:
                if tmp_task["properties"]["key"] == father_key:
                    task.properties["father"] = father_key
                    tmp_task["properties"]["kids"].append({"properties": task.properties})
                    break
        else:
            self.__task_dict.append({"properties": task.properties})
        self.__task[key] = task
        self.__task_list.append({"properties": task.properties})
        print("register: ", task.properties["name"])
        if task.properties["name"] in ['main', 'Main']:
            self.__main_key = key
        return key

    def get_task_list(self):
        return self.__task_list

    def get_main(self):
        return self.__task[self.__main_key]

    def get(self, key):
        return self.__task[key]

    def suspend_task(self, key):
        self.__task[key].properties["status"] = CONSTANT.TASK.SUSPEND
        # self.__task[key].properties["health"] = 50
        for task in self.__task[key].properties["kids"]:
            self.suspend_task(task["properties"]["key"])
        return {"properties": self.__task[key].properties}

    def restart_task(self, key):
        self.__task[key].properties["status"] = CONSTANT.TASK.RUNNING
        # self.__task[key].properties["health"] = 50
        for task in self.__task[key].properties["kids"]:
            self.restart_task(task["properties"]["key"])
        return {"properties": self.__task[key].properties}

    def get_task_dict(self):
        return self.__task_dict[0]
        # main = {"properties": {
        #     "name": "main",
        #     "status": CONSTANT.TASK.RUNNING,
        #     "health": 100,
        #     "kids": self.__task_dict
        # }}
        # return main
