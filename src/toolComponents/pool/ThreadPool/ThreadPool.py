# -*- utf-8 -*-
import threading

from src.toolComponents.decorator.Decorator import Singleton
from src.toolComponents.task.Task import Task


@Singleton
class ThreadPool(Task):
    __pool = {}

    def mount(self):
        pass

    def handle(self):
        pass

    def thread(self, target, **args):
        new = threading.Thread(target=target, **args)
        self.debug(new)
        new.start()
        pass
    pass

def test():
    print("testfunfunfun")

# https://www.jianshu.com/p/7b6a80faf33f
ThreadPool().init().thread(test)
print(threading.Event())
