# -*- utf-8 -*-
import pymongo

from src.toolComponents.decorator.Decorator import Singleton
from src.toolComponents.surveillance.Constant import CONSTANT
from src.toolComponents.task.Task import Task


@Singleton
class MongoMongo(Task):
    collection = {}
    client = None
    db = None

    def mount(self):
        pass

    def select(self, collection_name, query=None, scope=None, limit=None) -> list:
        if query is None:
            query = {}
        data = None
        if limit is None:
            if scope is None:
                data = self.collection[collection_name].find(query)
            else:
                data = self.collection[collection_name].find(query, scope)
        else:
            if scope is None:
                data = self.collection[collection_name].find(query).limit(limit)
            else:
                data = self.collection[collection_name].find(query, scope).limit(limit)
        data = list(data)
        # self.print("selected records total: " + str(data.__len__()) + '\t' + "coll: " + collection_name)
        return data

    def insert(self, collection_name, record) -> None:
        self.collection[collection_name].insert_one(record)
        self.print("inserted total: " + str(1))

    def update(self, collection_name, value, query=None, limit=None):
        if query is None:
            query = {}
        if limit == 1:
            self.print("updated records total: " +
                       str(self.collection[collection_name].update_one(query, {"$set": value}).modified_count) + '\t' +
                       "coll: " + collection_name)
        elif limit is None:
            self.print("updated records total: " +
                       str(self.collection[collection_name].update_many(query, {"$set": value}).modified_count) + '\t' +
                       "coll: " + collection_name)
            pass

    def delete(self, collection_name, query=None, limit=None):
        if query is None:
            query = {}
        if limit == 1:
            self.print("removed records total: " +
                       str(self.collection[collection_name].delete_one(query).deleted_count) + '\t' +
                       "coll: " + collection_name)
        elif limit is None:
            self.print("removed records total: " +
                       str(self.collection[collection_name].delete_many(query).deleted_count) + '\t' +
                       "coll: " + collection_name)
            pass

    def handle(self) -> None:
        self.client = pymongo.MongoClient(
            'mongodb://' + CONSTANT.MONGO.USER + ':' + CONSTANT.MONGO.PASSWORD + '@' + CONSTANT.MONGO.URL + ':' + CONSTANT.MONGO.PORT)
        self.print("connected to mongo: " + str(self.client))
        db_list = self.client.list_database_names()
        self.print("find mongo dbs: " + str(db_list))
        if CONSTANT.MONGO.DATABASE in db_list:
            self.print("find database: " + CONSTANT.MONGO.DATABASE)
            self.print("ready to connect with database: " + CONSTANT.MONGO.DATABASE)
        self.db = self.client[CONSTANT.MONGO.DATABASE]
        self.print("connect with db: " + str(self.db))
        coll_list = self.db.list_collection_names()
        self.print("find " + CONSTANT.MONGO.DATABASE + " dbs: " + str(coll_list))
        for coll in CONSTANT.MONGO.COLLECTIONS:
            self.collection[coll] = self.db[coll]
            self.print("fetch collection: " + str(coll))
        pass

    pass

#
# mongo = MongoMongo().init()
# mongo.insert("test", {"nnn": "RUNOOB", "alexa": "10000", "url": "https://www.runoob.com"})
# print(mongo.select("test"))
# mongo.update("test", query={"nnn": "RUNOOB"}, value={"alexa":'123123'})
# print(mongo.select("test"))
# mongo.delete("test")
# print(mongo.select("test"))

# 系统设置使用
# mongo = MongoMongo().init()
# mongo.insert("sys", {"id": "0", "item_collection_total_page": 627, "item_collection_total_count": 12533})
# print(mongo.select("sys"))
