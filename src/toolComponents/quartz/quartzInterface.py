# -*- coding:utf-8 -*-
# from src.toolComponents.quartz.ManagerReader import ManagerReader
from src.toolComponents.quartz.test.quartzTest import quartzTest
from flask import Flask, request


class TTest:
    def __init__(self):
        pass

app = Flask(__name__)

@app.route('/')
def hello_world():
    # return reader.getQuartz()
    return "123123123"
@app.route('/register', methods=['POST'])

def register():
    print(request.headers)
    print(request.form)
    print(request.form['name'])
    print(request.form.get('name'))
    print(request.form.getlist('name'))
    print(request.form.get('nickname', default='little apple'))
    #do something else
    #
    #
    return 'welcome'

print("adadadadfafafsghhsvmjgjyf")
if __name__ == '__main__':
    quartzTest()
    # reader = ManagerReader()
    # print(reader.getQuartz())
    # app.debug=True
    test = TTest()
    app.run()