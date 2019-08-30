# -*- utf-8 -*-
from flask import Flask
import threading
import flask


class Api:
    # 实例化Flask对象
    app = Flask(__name__)

    def __init__(self):
        # 启动api服务监听
        self.run()

    # 生成路由关系，并把关系保存到某个地方,app对象的 url_map字段中
    @app.route('/test')  # @decorator
    def index(self):
        return "test"

    def run(self):
        threading.Thread(target=self.app.run).start()
