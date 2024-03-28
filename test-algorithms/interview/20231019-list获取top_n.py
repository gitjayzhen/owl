# -*- coding: utf-8 -*-

"""
@author: jayzhen
@license: Apache Licence 
@version: Python 3.8+
@file: 20231019-list获取top_n.py
@time: 2023/10/19 15:36
"""
import functools
import time


# 统计 日志


def log(func):
    print("AAAAAAA")
    # @functools.wraps
    def log_func(*arg, **kw):
        a = time.time()
        res = func(*arg, **kw)
        print("func run cast: {}".format(time.time() - a))
        return res
    return log_func


def decorator_with_args(arg1, arg2):
    print("BBBBBBB")

    def decorator(func):
        def wrapper(*args, **kwargs):
            # 在调用被装饰函数之前执行的代码
            print(f"Decorator arguments: {arg1}, {arg2}")
            result = func(*args, **kwargs)  # 调用被装饰的函数
            # 在调用被装饰函数之后执行的代码
            return result
        return wrapper
    return decorator

@log
@decorator_with_args("arg1_value", "arg2_value")
def test_func(arg):
    print(arg)
    time.sleep(3)
    return True


# top3 的关键词是什么
def get_top_n(keys_data: list, top_n):
    res = {}
    for i in keys_data:
        if i in res.keys():
            res[i] += 1
        else:
            res[i] = 1
    top_data = []
    a = sorted(res.values(), reverse=True)[0:top_n]
    for k, v in res.items():
        if v in a and top_n > 0:
            top_data.append(k)
            top_n -= 1
    return top_data


if __name__ == '__main__':
    assert test_func("test")
    # print(get_top_n(["asdf", "asdf", "asdf", "asdf", "qwer", "qwer", "qwer",
    #                   "asdfasdf", "asfasdfasdfwefaefa", "ijninin","ijninin","ijninin","ijninin", "234234"], 2))
