# -*- utf-8 -*-
from src.toolComponents.surveillance.Constant import CONSTANT
from src.toolComponents.task.TaskManager import TaskManager
from src.toolComponents.task.Task import Task
from flask import Flask
import threading

# 实例化Flask对象
app = Flask("name")


@app.route('/test')
def index():
    return "test"


@app.route('/task')  # @decorator
def task():
    taskmanaget = TaskManager()
    return str(taskmanaget.get_task_dict())


class Api(Task):
    __app = app
    info = {
        "name": "API",
        "status": CONSTANT.TASK.RUNNING,
        "health": 100
    }

    def __init__(self):
        super().__init__()
        # threading.Thread(target=self.run).start()
        self.run()

    def run(self):
        app.run(host="0.0.0.0", port=5000, threaded=True)
        print("3113221313221313221313")
