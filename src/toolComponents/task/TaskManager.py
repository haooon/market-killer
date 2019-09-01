# -*- coding:utf-8 -*-
import uuid

from src.toolComponents.decorator.Decorator import Singleton
from src.toolComponents.surveillance.Constant import CONSTANT

@Singleton
class TaskManager:
    __task_dict = None
    __task_list = None
    info = {
        "name": "task manager",
        "status": CONSTANT.TASK.RUNNING,
        "health": 100
    }

    def __init__(self):
        self.__task_list = []
        self.__task_dict = []
        self.__task = {}

    def register(*args):
        self = args[0]
        task = args[1]
        task.info["kids"] = []
        key = task.info["key"] = str(uuid.uuid1())
        print("register:: ", args.__len__())
        print("register:: ", args)
        if args.__len__() > 2:
            father_key = args[2]
            for tmp_task in self.__task_dict:
                if tmp_task["info"]["key"] == father_key:
                    tmp_task["info"]["kids"].append({"info": task.info})
                    break
        else:
            self.__task_dict.append({"info": task.info})
        self.__task[key] = task
        self.__task_list.append({"info": task.info})
        return key

    def get_task_list(self):
        return self.__task_list

    def get_task_dict(self):
        main = {"info":{
            "name": "main",
            "status": CONSTANT.TASK.RUNNING,
            "health": 100,
            "kids": self.__task_dict
        }}
        return main


