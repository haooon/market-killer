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

    def select(self, collection_name, query={}, scope=None, limit=None) -> dict:
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
        self.print("selected records total: " + str(data.__len__()))
        return data

    def insert(self, collection_name, record) -> None:
        self.collection[collection_name].insert_one(record)

    def update(self, collection_name, value, scope={}, limit=None) -> int:
        if limit == 1:
            self.print("updated records total: " +
                       str(self.collection[collection_name].update_one(scope, {"$set": value}).modified_count))
        elif limit is None:
            self.print("updated records total: " +
                       str(self.collection[collection_name].update_many(scope, {"$set": value}).modified_count))
            pass

    def delete(self, collection_name, scope={}, limit=None):
        if limit == 1:
            self.print("removed records total: " +
                       str(self.collection[collection_name].delete_one(scope).deleted_count))
        elif limit is None:
            self.print("removed records total: " +
                       str(self.collection[collection_name].delete_many(scope).deleted_count))
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


# mongo = MongoMongo().init()
# mongo.insert("test", {"nnn": "RUNOOB", "alexa": "10000", "url": "https://www.runoob.com"})
# print(mongo.select("test"))
# mongo.update("test", scope={"nnn": "RUNOOB"}, value={"alexa":'123123'})
# print(mongo.select("test"))
# mongo.delete("test")
# print(mongo.select("test"))
