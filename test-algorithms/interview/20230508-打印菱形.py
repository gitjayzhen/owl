# -*- coding: utf-8 -*-

"""
@author: jayzhen <jayzhen_testing@163.com>
@site: https://github.com/gitjayzhen
@version: 1.0.0
@license:  Apache Licence
@software: PyCharm & Python 3.7+
@file: 20230508-打印菱形.py
@time: 2023/5/9 11:12
"""


def print_rhombus(num: int):
    if num % 2 == 0:
        return False
    result = []
    for i in range(num):
        if i % 2 == 0:
            continue
        space = int((num - i) / 2)
        result.append(("{}{}".format(" " * space, "+" * i)))
    for i in [*result, "+" * num, *sorted(result, reverse=True)]:
        print(i)
    return True


def print_rhombus2(num: int):
    if num % 2 == 0:
        return False
    for i in range(num * 2):
        if i % 2 == 0:
            continue
        space = int((num - i % num) / 2) if i < num else int((i % num) / 2)
        print("{}{}".format(" " * space, "+" * (i if i <= num else (num - i % num))))
    return True


def print_rhombus3(num: int):
    if num % 2 == 0:
        return False
    for i in range(num * 2):
        if i % 2 == 0:
            continue
        space = int(abs(i - num) / 2)
        print("{}{}".format(" " * space, "+" * (num - space * 2)))
    return True


if __name__ == '__main__':
    assert not print_rhombus2(4)
    assert print_rhombus3(5)
    assert print_rhombus3(7)
