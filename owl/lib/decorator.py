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


# 单例模式
# 方法1,实现__new__方法
# 并在将一个类的实例绑定到类变量_instance上,
# 如果cls._instance为None说明该类还没有实例化过,实例化该类,并返回
# 如果cls._instance不为None,直接返回cls._instance
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


# 共享状态的单例，通过继承
class SingletonClass:
    # 单例模式写法,参考：http://ghostfromheaven.iteye.com/blog/1562618
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance or not hasattr(cls, '_instance'):
            cls._instance = super(SingletonClass, cls).__new__(cls, *args, **kwargs)
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

