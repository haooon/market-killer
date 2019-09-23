# -*- utf-8 -*-
from src.sysComponents.mongo.MongoTask import MongoMongo
from src.toolComponents.decorator.Decorator import Singleton
from src.toolComponents.task.Task import Task
import time


@Singleton
class SysTask(Task):
    mongo = None

    def mount(self):
        self.mongo = MongoMongo()

    # 获取item 列表 最大页数动态设置
    def set_item_collection_total_page(self, new_value):
        history = {
            'term': 'item_collection_total_page',
            'old_value': self.get_item_collection_total_page(),
            'new_value': new_value,
            'timestamp': time.time(),
        }
        self.mongo.insert("sys_history", history)
        self.mongo.update("sys", query={'id': '0'}, value={'item_collection_total_page': new_value})
        self.print("updated item collection total page, new total page: " + str(new_value))

    def get_item_collection_total_page(self) -> int:
        query_list = self.mongo.select("sys", query={'id': '0'})
        if query_list.__len__() > 0:
            return query_list[0]['item_collection_total_page']
        else:
            self.error("get item collection total page error, can not get sys data(size 0)")
            return -1

    # 获取item 列表 最大页数动态设置
    def set_item_collection_total_count(self, new_value):
        history = {
            'term': 'item_collection_total_count',
            'old_value': self.get_item_collection_total_count(),
            'new_value': new_value,
            'timestamp': time.time(),
        }
        self.mongo.insert("sys_history", history)
        self.mongo.update("sys", query={'id': '0'}, value={'item_collection_total_count': new_value})
        self.print("updated item collection total count, new total count: " + str(new_value))

    def get_item_collection_total_count(self) -> int:
        query_list = self.mongo.select("sys", query={'id': '0'})
        if query_list.__len__() > 0:
            return query_list[0]['item_collection_total_count']
        else:
            self.error("get item collection total count error, can not get sys data(size 0)")
            return -1

    pass
