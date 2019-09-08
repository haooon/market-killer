# -*- utf-8 -*-
import json

from src.toolComponents.quartz.QuartzManager import QuartzManager
from src.toolComponents.surveillance.Constant import CONSTANT
from src.toolComponents.task.TaskManager import TaskManager
from src.toolComponents.task.Task import Task
from flask import Flask
from flask_cors import CORS
import threading

# 实例化Flask对象
app = Flask("name")
CORS(app, resources=r'/*')

@app.route('/test')
def index():
    return "test"


@app.route('/task', methods=['GET'])  # @decorator
def task():
    task_manager = TaskManager()
    return task_manager.get_task_dict()

@app.route('/quartz', methods=['GET'])
def quartz():
    quartz_manager = QuartzManager()
    return quartz_manager.get_quartz_dict()

@app.route('/runquartz', methods=['GET'])
def quartzRun():
    quartz_manager = QuartzManager().run()

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
        app.run(host="0.0.0.0", port=8090, threaded=True)
        print("3113221313221313221313")
