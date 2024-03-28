#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
@author:    jayzhen <jayzhen_testing@163.com>
@share:     https://github.com/gitjayzhen
@file:      attr_read_only.py
@time:      4/27/21 2:01 PM
"""


class A():

    def __init__(self):
        self.__age = 10         # 实例对象无法使用 .__age 的方式来获取参数和设置参数, 且无法通过.__getattribute__获取
        self._address = "a"

    def age(self):
        return self.__age


class B():

    __age = 10          # 实例对象无法使用 .__age 的方式来获取参数和设置参数, 且无法通过.__getattribute__获取
    _address = "b"      # protected 的属性 可以被直接访问

    @property
    def age(self):
        return self.__age

    @property
    def address(self):
        return self._address


if __name__ == '__main__':
    # a = A()
    # a._address = "b"
    # print(dir(a))
    # print(a._address)
    # print(a.age())

    b = B()
    print(b._address)
    b._address = "c"
    print(b._address)
