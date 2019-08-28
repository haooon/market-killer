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
class CONSTANT:
    # 健康检查点用 变量值
    CHECKPOINT = CHECKPOINT()


    # 系统用 变量值
    DEBUG = True

    CHECK_POINT_MAX_HISTORY = 20


CONSTANT = CONSTANT()
