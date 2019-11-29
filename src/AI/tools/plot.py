# -*- utf-8 -*-

from src.toolComponents.decorator.Decorator import Singleton
from src.toolComponents.task.Task import Task
import matplotlib.pyplot as plt
import numpy as np


@Singleton
class plotTask(Task):
    def handle(self):
        pass

    def draw(self, points=None, lines=None):
        if points is not None:
            for point in points:
                plt.plot(point[0], point[1], 'o', color="#800080")
        if lines is not None:
            for line in lines:
                plt.plot(line[0], line[1])
        plt.show()
