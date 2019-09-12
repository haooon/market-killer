# -*- coding:utf-8 -*-
import uuid

from src.toolComponents.decorator.Decorator import Singleton
from src.toolComponents.surveillance.Constant import CONSTANT


@Singleton
class TaskManager:
    __main_key = None
    __task_dict = None
    __task_list = None
    info = {
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
        if task["info"]["kids"].__len__() > 0:
            for son in task["info"]["kids"]:
                tmplist.append(self.get_task_health(son))
        else:
             return task["info"]["health"]
        for i in tmplist:
            sum += i
        task["info"]["health"] = sum / tmplist.__len__()
        return task["info"]["health"]

    def register(*args):
        self = args[0]
        task = args[1]
        task.info["kids"] = []
        key = task.info["key"] = str(uuid.uuid1())
        if "name" not in task.info.keys():
            task.info["name"] = task.__class__.__name__
        if "status" not in task.info.keys():
            task.info["status"] = CONSTANT.TASK.RUNNING
        if "health" not in task.info.keys():
            task.info["health"] = CONSTANT.TASK.BASIC_HEALTH
        if args.__len__() > 2:
            father_key = args[2]
            for tmp_task in self.__task_list:
                if tmp_task["info"]["key"] == father_key:
                    task.info["father"] = father_key
                    tmp_task["info"]["kids"].append({"info": task.info})
                    break
        else:
            self.__task_dict.append({"info": task.info})
        self.__task[key] = task
        self.__task_list.append({"info": task.info})
        print("register: ", task.info["name"])
        if task.info["name"] in ['main', 'Main']:
            self.__main_key = key
        return key

    def get_task_list(self):
        return self.__task_list

    def get_main(self):
        return self.__task[self.__main_key]

    def get(self, key):
        return self.__task[key]

    def suspend_task(self, key):
        self.__task[key].info["status"] = CONSTANT.TASK.SUSPEND
        self.__task[key].info["health"] = 50
        return {"info": self.__task[key].info}

    def get_task_dict(self):
        return self.__task_dict[0]
        # main = {"info": {
        #     "name": "main",
        #     "status": CONSTANT.TASK.RUNNING,
        #     "health": 100,
        #     "kids": self.__task_dict
        # }}
        # return main
