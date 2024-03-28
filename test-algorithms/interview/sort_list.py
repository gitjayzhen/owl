#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
@author:    jayzhen <jayzhen_testing@163.com>
@share:     https://github.com/gitjayzhen
@file:      sort_list
@time:      5/15/21 3:50 PM
"""


def maopao(a_list):
    """
    冒泡排序：主要是两两前后比较，把最大或最小的往后送
    :param a_list:
    :return:
    """
    a_len = len(a_list)
    for i in range(a_len - 1):
        for j in range(a_len - i - 1):
            if a_list[j] > a_list[j + 1]:
                a_list[j], a_list[j + 1] = a_list[j + 1], a_list[j]

    print(a_list)


def xuanzhe(a_list):
    """
    第一层的索引跟所有后面的比较，谁小谁在前面
    :param a_list:
    :return:
    """
    print(*a_list)
    a_len = len(a_list)
    for i in range(a_len - 1):
        for j in range(i, a_len):
            if a_list[i] > a_list[j]:
                a_list[i], a_list[j] = a_list[j], a_list[i]
    print(a_list)


def do_quick(a_list, first, end):
    """
    使用递归的方式，对比一个最后或最前的一个值的大小，将所有这个数的值放到左边，
    更替这个中间墙的下标，并将最后的值放到这个下标位，及左边都是小于他，右边都是大于他
    然后前后拆分重复上面的动作，即可排序成功
    :param a_list:
    :param first:
    :param end:
    :return:
    """
    if first < end:
        wall = first
        for i in range(first, end):
            if a_list[i] < a_list[end]:
                a_list[i], a_list[wall] = a_list[wall], a_list[i]
                wall += 1
        print(a_list)
        a_list[wall], a_list[end] = a_list[end], a_list[wall]
        do_quick(a_list, first, wall - 1)
        do_quick(a_list, wall + 1, end)
    return a_list


def quicksort(a_list):
    print(do_quick(a_list, 0, len(a_list) - 1))


if __name__ == '__main__':
    quicksort([2, 4, 8, 3, 9, 1, 5, 2])
