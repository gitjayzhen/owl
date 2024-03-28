#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
@author:    jayzhen <jayzhen_testing@163.com>
@share:     https://github.com/gitjayzhen
@file:      merge_ordered_arrays
@time:      4/27/21 10:03 AM
"""


def main(a_list, b_list):
    """
    合并两个升序的数组

    思路：
        利用两个都是升序的特性，采用双循环下标的方式，使用while的方式，来操作里面的数据
    :param a_list: 升序
    :param b_list: 升序
    :return: 返回合并的数组，且为升序
    """
    a_len = len(a_list)
    b_len = len(b_list)
    a = 0
    b = 0
    res = list()
    while a < a_len and b < b_len:
        if a_list[a] < b_list[b]:
            res.append(a_list[a])
            a += 1
        else:
            res.append(b_list[b])
            b += 1
    while a < a_len:
        res.append(a_list[a])
        a += 1
    while b < b_len:
        res.append(b_list[b])
        b += 1
    return res


if __name__ == "__main__":
    a = [-1, 10, 100, 123, 333, 1000]
    b = [1, 3, 5, 34, 10000]
    print(main(a, b))
