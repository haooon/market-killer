# -*- utf-8 -*-
# 检查点最大历史数量
from src.toolComponents.decorator.Decorator import Singleton


@Singleton
class CHECKPOINT:
    HAPPY = True
    SAD = False
    # 检查点历史最大数量
    # 用于查看检查点健康度
    POINT_MAX_HISTORY = 20
    # 任务检查点历史最大数量
    # 用于查看任务健康度
    CHECK_MAX_HISTORY = 100

@Singleton
class TASK:
    # 任务运行状态：运行中
    RUNNING = "RUNNING"
    # 任务运行状态：停止
    STOPPED = "STOPPED"
    # 任务运行状态：挂起
    SUSPEND = "SUSPEND"
    # 任务运行状态：死亡
    DEAD = "DEAD"
    # 基础健康度
    BASIC_HEALTH = 100


@Singleton
class MONGO:
    # 地址
    URL = "39.105.99.88"
    # 端口
    PORT = "27017"
    # 用户名
    USER = "haooon"
    # 密码
    PASSWORD = "1141135276Shr"
    # 库
    DATABASE = "app"
    COLLECTIONS = [
        "test",
        "item",
        # 系统
        "sys",
        # 系统历史
        "sys_history",
    ]

@Singleton
class ProxyPool:
    # 地址
    URL = "http://39.105.99.88:8899/api/v1/proxies?limit=9999"

@Singleton
class CONSTANT:
    # 健康检查点用 变量值
    CHECKPOINT = CHECKPOINT()
    # 任务
    TASK = TASK()
    # mongo数据库
    MONGO = MONGO()
    # 代理
    PROXYPOOL = ProxyPool()
    # 系统用 变量值
    DEBUG = True

    CHECK_POINT_MAX_HISTORY = 20


CONSTANT = CONSTANT()