#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
@author:    jayzhen <jayzhen_testing@163.com>
@share:     https://github.com/gitjayzhen
@file:      thread_sync
@time:      5/8/21 10:17 AM
"""


import threading
import time


def thread():
    time.sleep(2)
    print('---子线程结束---')


def main():
    t1 = threading.Thread(target=thread)
    # t1.setDaemon(True)        # 设置子线程守护主线程
    t1.start()
    t1.join(timeout=1)          # 会先等子线程结束在结束主线程
    print('---主线程结束---')


if __name__ == '__main__':
    main()
# 执行结果 ---主线程结束--- #只有主线程结束，子线程来不及执行就被强制结束
