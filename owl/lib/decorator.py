# -*- coding: utf-8 -*-

"""
@author: jayzhen
@license: Apache Licence 
@version: Python 3.8+
@file: decorator.py
@time: 2023/9/4 18:56
"""
import time
import warnings
from functools import wraps


# 装饰器实现的单例
def singleton(cls):

    instances = {}

    def wrapper(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]

    return wrapper


def record_transaction_time(func):

    @wraps(func)
    def record(*args, **kwargs):
        begin = time.time()
        result = func(*args, **kwargs)
        # time.sleep(random.randint(2, 5))
        # result = int(time.time())
        print(func.__name__, "cost:", int(time.time() - begin), "s")
        return result

    return record


# 共享状态的单例
class SingletonClass:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls, *args, **kwargs)
        return cls._instance


# 元类实现的单例
class SingletonMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]

# class SingletonClass(metaclass=SingletonMeta):
#     pass


def deprecated(func):
    def wrapper(*args, **kwargs):
        warnings.warn(f"OWL Deprecated: {func.__name__} is deprecated.", category=DeprecationWarning, stacklevel=2)
        return func(*args, **kwargs)
    return wrapper

