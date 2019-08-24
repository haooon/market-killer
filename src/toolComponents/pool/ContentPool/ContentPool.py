# -*- coding:utf-8 -*-

class ContentPool:
    __CommonArrayItemCount = 0
    __FastArrayItemCount = 0
    __CommonArray = {}
    __FastArray = {}
    def __init__(self):
        self.__CommonArray = {}
        self.__FastArray = {}
        self.__CommonArrayItemCount = 0
        self.__FastArrayItemCount = 0
    def getCommonArray(self):
        return self.__CommonArray
    def insertCommonArray(self, key, content):
        self.__CommonArray[key] = content