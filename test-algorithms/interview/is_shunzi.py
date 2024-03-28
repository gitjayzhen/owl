#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
@author:    jayzhen <jayzhen_testing@163.com>
@share:     https://github.com/gitjayzhen
@file:      is_shunzi
@time:      5/6/21 5:51 PM


新建一个表，
学生id，学生姓名，学科，学科成绩

1，张三 语文 80
1，张三 数学 70
2，李四 英语 90

所有学科成绩都大于80分的学生
create tabel stu_sorce(
    id
    stu_id varchar(30) notnull premary key,
    stu_name varchar(10) notnull,
    class_name varchar(50) notnull,
    sorce int default 0
    index_stu_id ...
    charset...
);

select stu_name from stu_sorce group by stu_id having avg(sorce) > 80


select stu_name from stu_sorce group by stu_id having min(sorce) > 80



一副扑克牌
两个大小王
随机从里面抽五个数
判断是不是顺子
大小王可以充当任何数
0 1 4 5 6
"""


class Node(object):

    def __init__(self):
        self.pre = None
        self.val = None
        self.next = None


def main(data):
    data = sorted(data)
    begin = Node()
    begin.val = data[0]
    for i in range(len(data) - 1):
        tmp = Node()
        tmp.val = data[i + 1]
        tmp.pre = begin


def is_king(x):
    king = ['a', 'b']
    if x in king:
        return True
    return False


def main1(data):
    data = sorted(data)
    king = 0
    res = False
    for n in range(len(data) - 1):
        i = data[n]
        if i == 0:
            king += 1
            continue
        y = data[n + 1]
        tmp = y - i
        if tmp == 1:
            res = True
            continue
        if tmp - 1 - king <= 0:
            res = True
            king -= 1
        else:
            return False
    return res


print(main1([0, 3, 4, 5, 8]))
