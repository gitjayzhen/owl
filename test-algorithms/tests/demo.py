#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
@author:    jayzhen
@email:     jayzhen_testing@163.com
@site:      https://github.com/gitjayzhen
@software:  PyCharm & Python 3.7
@file:      demo
@time:      4/13/21 9:53 AM
"""


def main():
    content = '3898888821'
    mark = ''
    index = 0
    count = 1
    for i in range(len(content) - 1):
        if content[i] == content[i+1]:
            mark = content[i]
            if index == 0:
                index = i
            count += 1

    print(mark, index, count)


import collections


def main2(content):
    if content is None or str(content).strip() == "":
        return None
    count = collections.Counter(content)
    print(count)
    count_list = []
    for i in count.items():
        count_list.append((i))
    print(content)
    res = sorted(count_list, key=lambda x: x[1], reverse=True)
    max_res = res[0]
    n = 0
    for y in range(len(content)):
        if content[y] == max_res[0]:
            n += 1
            continue
        else:
            n = 0
        if n == max_res[1]:
            return y, max_res[1]
    return None


def main3(content):

    tmp = []
    for i in content:
        t = list(i)
        tmp.append("".join(sorted(t, key=lambda x: x, reverse=False)))
    tmp_set = set(tmp)
    res = {}
    for y in tmp_set:
        for n in range(len(tmp)):
            if y == tmp[n]:
                if y in res:
                    res[y].append(content[n])
                    continue
                res[y] = [content[n]]
    return res


class Node():

    def __init__(self, val):
        self.val = val
        self.val2 = "".join(sorted(list(val)))
        self.next = None


def main4(content):
    """
    ["eat", "tea", "tan", "ate", "nat", "bat"] 异位同位元素 分组
    :param content:
    :return:
    """
    head = None
    tmp = None
    for i in range(len(content)):
        n = Node(content[i])
        if head is None:
            head = tmp = n
            continue
        tmp.next = n
        tmp = n
    res = {}
    while True:
        if head is None:
            break
        print(head.val)
        if head.val2 in res:
            res[head.val2].append(head.val)
        else:
            res[head.val2] = [head.val]
        head = head.next
    return res


def main5(content):
    res = {}
    for i in content:
        tmp = "".join(sorted(list(i)))
        if tmp in res:
            res[tmp].append(i)
            continue
        res[tmp] = [i]
    return res

# print(main("3898888821"))


if __name__ == '__main__':
    # main()
    print(main5(["eat", "tea", "tan", "ate", "nat", "bat"]))
