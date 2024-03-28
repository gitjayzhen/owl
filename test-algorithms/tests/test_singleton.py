#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
@author:    jayzhen
@email:     jayzhen_testing@163.com
@site:      https://github.com/gitjayzhen
@software:  PyCharm & Python 3.7
@file:      test_singleton
@time:      4/14/21 10:14 AM
"""


# def Singleton(cls):
#     _instance = {}
#
#     def wapper(*args, **kwargs):
#         if cls not in _instance:
#             _instance[cls] = cls(*args, **kwargs)
#         return _instance[cls]
#
#     return wapper


# @Singleton
# class Foo():
#     pass

# class A(object):
#     """实例化一个对象：首先 new 然后 init ，"""
#
#     def __init__(self):
#         print("__init__")
#
#     def __new__(cls, *args, **kwargs):
#         print("__new__")
#         if not hasattr(cls, '_instance'):
#             cls._instance = super().__new__(cls, *args, **kwargs)
#         return cls._instance
#
#     def __call__(self, *args, **kwargs):
#         print("__call__")

class Singleton(type):

    def __call__(cls, *args, **kwargs):
        print("__call__")
        if not hasattr(cls, '_instance'):
            cls._instance = super().__call__(*args, **kwargs)
        return cls._instance


class Foo(metaclass=Singleton):
    pass


if __name__ == '__main__':

    print("abc"[::-1])

    a = Foo()
    b = Foo()
    print(id(a), id(b))
    print(a is b)
