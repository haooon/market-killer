# -*- utf-8 -*-
import json
import threading

from src.toolComponents.quartz.QuartzManager import QuartzManager
from src.toolComponents.task.TaskManager import TaskManager
from src.toolComponents.task.Task import Task
from flask import Flask, request
from flask_cors import CORS

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

@app.route('/tasklist', methods=['GET'])  # @decorator
def task_list():
    task_manager = TaskManager()
    return str(task_manager.get_task_list())

@app.route('/quartz', methods=['GET'])
def quartz():
    quartz_manager = QuartzManager()
    return quartz_manager.get_quartz_dict()

@app.route('/run', methods=['GET'])
def quartzRun():
    TaskManager().get_main().run()
    task_manager = TaskManager()
    return task_manager.get_task_dict()

@app.route('/suspend', methods=['GET'])
def task_suspend():
    # key = request.form.get("key")
    key = request.args.get("key")
    return TaskManager().suspend_task(key)

@app.route('/restart', methods=['GET'])
def task_restart():
    # key = request.form.get("key")
    key = request.args.get("key")
    return TaskManager().restart_task(key)

class Api(Task):
    __app = app

    def handle(self):
        app.run(host="0.0.0.0", debug=False, port=8888, threaded=True)