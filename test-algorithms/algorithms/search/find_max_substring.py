#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
@author:    jayzhen
@email:     jayzhen_testing@163.com
@site:      https://github.com/gitjayzhen
@software:  PyCharm & Python 3.7
@file:      find_max_substring
@time:      4/23/21 10:26 AM
"""


def find_longest_no_repeat_substr(one_str):
    '''
    找出来一个字符串中最长不重复子串
    :param one_str:
    :return:
    '''
    res_list = []
    length = len(one_str)
    for i in range(length):
        tmp = one_str[i]
        for j in range(i+1, length):
            if one_str[j] not in tmp:
                tmp += one_str[j]
            else:
                break
    res_list.append(tmp)
    res_list.sort(lambda x,y: cmp(len(x),len(y)))
    return res_list[-1]


if __name__ == '__main__':
    str_list = ['120135435', 'abdfkjkgdok', '123456780423349']
    for one_str in str_list:
        res = find_longest_no_repeat_substr(one_str)
        print('{0}最长非重复子串为：{1}'.format(one_str, res))
