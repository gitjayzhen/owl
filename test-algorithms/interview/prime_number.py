#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
@author:    jayzhen <jayzhen_testing@163.com>
@share:     https://github.com/gitjayzhen
@file:      prime_number.py
@time:      4/27/21 10:56 AM
"""


def is_sushu(i):

    for x in range(2, i//2+1):
        if i % x == 0:
            return False
    return True


def main():
    """
    获取1000-10000之间的所有素数，素数是只能被1和自身整除

    思路：
        1. 第一步的思想就是for循环处理，这里可能时间复杂度比较高，可以优化验证素数的方法，降低循环的次数

    :return:
    """
    for i in range(1000, 10001):
        res = is_sushu(i)
        if res:
            print(i)


if __name__ == '__main__':
    main()
