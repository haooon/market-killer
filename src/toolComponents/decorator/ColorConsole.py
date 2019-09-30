# -*- utf-8 -*-

# 字背景颜色范围:40----49
# 40:黑
# 41:深红
# 42:绿 43:黄色
# 44:蓝色
# 45:紫色
# 46:深绿
# 47:白色
#
# 字颜色:30-----------39
# 30:黑
# 31:红
# 32:绿
# 33:黄
# 34:蓝色
# 35:紫色
# 36:深绿
# 37:白色


def Red(func):
    def sync(*args):
        tmp = func(*args)
        red = "\033[30;31m" + tmp + "\033[0m"
        print(red)
    return sync


def Blue(func):
    def sync(*args):
        tmp = func(*args)
        blue = "\033[30;34m" + tmp + "\033[0m"
        print(blue)
    return sync


def Yellow(func):
    def sync(*args):
        tmp = func(*args)
        yellow = "\033[30;33m" + tmp + "\033[0m"
        print(yellow)
    return sync


def Green(func):
    def sync(*args):
        tmp = func(*args)
        green = "\033[30;32m" + tmp + "\033[0m"
        print(green)
    return sync


def Black(func):
    def sync(*args):
        tmp = func(*args)
        print(tmp)
    return sync
