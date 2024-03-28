# -*- coding: utf-8 -*-

"""
@author: jayzhen <jayzhen_testing@163.com>
@site: https://github.com/gitjayzhen
@version: 1.0.0
@license:  Apache Licence
@software: PyCharm & Python 3.7+
@file: 230426-按字典分割字符串.py
@time: 2023/4/26 15:25
"""
from collections import OrderedDict


def parse_string(origin_str: str, words: set):
    result = {}
    for i in words:
        if i in origin_str:
            index = origin_str.index(i)
            result[index] = i
            origin_str = origin_str.replace(i, "-" * len(i), 1)
    # print(result)
    # return " ".join([*result.values()])
    return " ".join([result[n] for n in sorted(result.keys())])


def parer_str_with_set(origin_str: str, words: set):
    str_len = len(origin_str)
    pre, nxt = 0, 1
    result = []
    while nxt <= str_len:
        word = origin_str[pre:nxt]
        print(pre, nxt, word)
        if word in words:
            result.append(word)
            pre = nxt
            nxt = nxt + 1
        else:
            nxt += 1
    return " ".join(result)


if __name__ == '__main__':
    word_set = set(["pie", "apple", "test"])
    res = parse_string("applepietest", word_set)
    assert "apple pie test" == res, res
    res2 = parer_str_with_set("applepietest", word_set)
    assert "apple pie test" == res2, res2
