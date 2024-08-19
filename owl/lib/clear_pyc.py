# -*- encoding: utf-8  -*-

""" 
@author: jayzhen
"""

import getopt
import os
import re
import sys


# 返回函数式方法
def file_end_with(*end_str):
    ends = end_str

    def run(s):
        f = map(s.endswith, ends)
        if True in f:
            return s

    return run


def san_path(abs_path, end_string):
    backfunc = file_end_with(end_string)
    for filepath, dirs, filelist in os.walk(abs_path):
        print(filelist)
        if not re.search("\\.git", filepath):
            f_file = filter(backfunc, filelist)
            for i in f_file:
                print(os.path.join(filepath, i))


def pwd_file_list(abs_path, end_string):
    data = []
    backfunc = file_end_with(end_string)
    file_list = os.listdir(abs_path)
    for i in file_list:
        i_path = os.path.join(abs_path, i)
        if os.path.isfile(i) and i.endswith("json"):
            data.append(i)
    return data


"""
file name patinal content
"""


def get_specified_file(fnpc):
    file_list = pwd_file_list(os.getcwd(), '.json')
    reg = re.compile(fnpc)
    for i in file_list:
        if re.search(reg, i):
            print(i)


if __name__ == '__main__':
    # print os.getcwd()
    # san_path(os.getcwd(),('.json'))
    # print pwd_file_list(os.getcwd(),('.json'))
    pattern, args = getopt.getopt(sys.argv[1:], "t:")
    if pattern is None or len(pattern) <= 0:
        sys.exit(0)
    for op, value in pattern:
        if op == "-t":
            reg_param = value
            get_specified_file(reg_param)
