# -*- coding: utf-8 -*-

"""
@author: jayzhen
@license: Apache Licence 
@version: Python 3.8+
@file: decorator.py
@time: 2023/9/4 18:56
"""
import logging
import time
import warnings
from functools import wraps, partial
from inspect import signature


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


def record_exec_time(func):

    @wraps(func)
    def record(*args, **kwargs):
        begin = time.time()
        result = func(*args, **kwargs)
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


def attach_wrapper(obj, func=None):
    """
    Utility decorator to attach a function as an attribute of obj
    """
    if func is None:
        return partial(attach_wrapper, obj)
    setattr(obj, func.__name__, func)
    return func


def logged(level, name=None, message=None):
    """
    Add logging to a function. level is the logging
    level, name is the logger name, and message is the
    log message. If name and message aren't specified,
    they default to the function's module and name.
    """
    def decorate(func):
        logname = name if name else func.__module__
        log = logging.getLogger(logname)
        logmsg = message if message else func.__name__

        @wraps(func)
        def wrapper(*args, **kwargs):
            log.log(level, logmsg)
            return func(*args, **kwargs)

        # Attach setter functions
        @attach_wrapper(wrapper)
        def set_level(newlevel):
            nonlocal level
            level = newlevel

        @attach_wrapper(wrapper)
        def set_message(newmsg):
            nonlocal logmsg
            logmsg = newmsg

        return wrapper

    return decorate


def typeassert(*ty_args, **ty_kwargs):
    def decorate(func):
        # If in optimized mode, disable type checking
        if not __debug__:
            return func

        # Map function argument names to supplied types
        sig = signature(func)
        bound_types = sig.bind_partial(*ty_args, **ty_kwargs).arguments

        @wraps(func)
        def wrapper(*args, **kwargs):
            bound_values = sig.bind(*args, **kwargs)
            # Enforce type assertions across supplied arguments
            for name, value in bound_values.arguments.items():
                if name in bound_types:
                    if not isinstance(value, bound_types[name]):
                        raise TypeError(
                            'Argument {} must be {}'.format(name, bound_types[name])
                            )
            return func(*args, **kwargs)
        return wrapper
    return decorate


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)
    countdown(100)
