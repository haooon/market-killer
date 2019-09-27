# -*- utf-8 -*-
import threading


class ThreadAble(threading.Thread):

    def __init__(self):
        super(ThreadAble, self).__init__()
        self._stop_event = threading.Event()

    def stop(self):
        self._stop_event.set()

    def stopped(self):
        return self._stop_event.is_set()
