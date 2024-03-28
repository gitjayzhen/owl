#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
@author:    jayzhen
@email:     jayzhen_testing@163.com
@site:      https://github.com/gitjayzhen
@software:  PyCharm & Python 3.7
@file:      demo2
@time:      4/18/21 11:59 AM
"""


# coding=utf-8

def main(a, b):
    tmp_a = list(a)[::-1]
    tmp_b = list(b)[::-1]
    num = 0
    tmp = []
    mark = 0
    if len(tmp_a) > len(tmp_b):
        num = len(tmp_b)
    else:
        num = len(tmp_a)
    for i in range(num):
        res = int(tmp_a[i]) + int(tmp_b[i])
        if mark == 1:
            res += mark
            mark = 0
        if res >= 10:
            tmp.append(str(res)[-1])
            mark = 1
        else:
            tmp.append(str(res))
    if len(tmp_a) > len(tmp_b):
        tmp.extend(tmp_a[len(tmp_b):])
    else:
        tmp.extend(tmp_a[len(tmp_a):])
    if mark == 1:
        tmp[num] = str(int(tmp[num]) + 1)
    return "".join(tmp[::-1])


def main2(a, b):
    if len(a) < len(b):
        a, b = b, a
    tmp_a = list(a)[::-1]
    tmp_b = list(b)[::-1]
    num = 0
    tmp = []
    mark = 0
    for i in zip(tmp_a, tmp_b):
        res = int(i[0]) + int(i[1])
        if mark == 1:
            res += mark
            mark = 0
        if res >= 10:
            tmp.append(str(res)[-1])
            mark = 1
        else:
            tmp.append(str(res))
    tmp.extend(tmp_a[len(tmp_b):])
    if mark == 1:
        tmp[num] = str(int(tmp[num]) + 1)
    return "".join(tmp[::-1])


A = '121342342342'
B = '7968700332'
print(main2(B, A))

assert str(int(A) + int(B)) == main2(B, A)

class Solution:
    def twoSum(self,nums,target):
        d = {}
        size = 0
        while size < len(nums):
            if target-nums[size] in d:
                if d[target-nums[size]] <size:
                    return [d[target-nums[size]],size]
                else:
                    d[nums[size]] = size
                size = size +1
solution = Solution()
list = [2,7,11,15]
target = 9
nums = solution.twoSum(list,target)
print(nums)
