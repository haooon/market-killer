# -*- utf-8 -*-

from src.toolComponents.decorator.Decorator import Red, Blue, Yellow, Black
from src.toolComponents.surveillance.Constant import CONSTANT

class Debug:
    @Black
    def print(self, *args):
        if CONSTANT.DEBUG:
            info = ""
            for arg in args:
                info += str(arg)
            return "[DEBUG::PRINT] ==> " + "[" + self.__class__.__name__ + "] >>> " + str(info)

    @Yellow
    def debug(self, *args):
        if CONSTANT.DEBUG:
            info = ""
            for arg in args:
                info += str(arg)
            return "[DEBUG::INFOO] ==> " + "[" + self.__class__.__name__ + "] >>> " + str(info)

    @Blue
    def blue(self, *args):
        if CONSTANT.DEBUG:
            info = ""
            for arg in args:
                info += str(arg)
            return "[DEBUG::BLUEE] ==> " + "[" + self.__class__.__name__ + "] >>> " + str(info)

    @Red
    def error(self, *args):
        info = ""
        for arg in args:
            info += str(arg)
        return "[DEBUG::ERROR] ==> " + "[" + self.__class__.__name__ + "] >>> " + str(info)