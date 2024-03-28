#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
@author:    jayzhen
@email:     jayzhen_testing@163.com
@site:      https://github.com/gitjayzhen
@software:  PyCharm & Python 3.7
@file:      select_two_sum
@time:      4/9/21 2:09 PM
"""


# int 数组a int 值b，从数组中找到两个数值和等于 a, 所有的情况？


def main(mark, a_list):
    """时间复杂度 T(n) = O(n^2)"""
    # 异常处理
    out = list()
    for i in range(len(a_list)):
        for y in range(len(a_list)):
            if y <= i:
                continue
            if a_list[i] + a_list[y] == mark:
                out.append((a_list[i], a_list[y]))
    return out


def get_sum_tuple_list(data_list, target):
    """时间复杂度 T(n) = O(n)"""
    d_map = {}
    result = []
    # [4, 5, 3, 2, 6, 1, 3, 7] 无序有重复的数
    # for index, value in enumerate(data_list):
    #     d_map[value] = index
    #     tmp = target - value
    #     if tmp in d_map:
    #         result.append((tmp, value))
    #         del d_map[tmp]
    #         del d_map[value]
    
    for index, value in enumerate(data_list):
        tmp = target - value
        if tmp in d_map:
            result.append((tmp, value))
        d_map[value] = index
    return result


if __name__ == '__main__':
    # a = [1, 2, 3, 4, 5, 7, 9, 10]
    # print(main(11, a))

    b = [4, 5, 2, 6, -1, 3, 7]
    print(get_sum_tuple_list(b, 5))
