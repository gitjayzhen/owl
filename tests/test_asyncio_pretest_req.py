#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
基于thrift协议的python协程压力测试
"""
import asyncio
import sys

import time
import signal
import logging.handlers
import datetime
import threading

from jtest.jtest_service.jtestService import *
from jtest.jtest_service.constants import *

from thrift import Thrift
from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol

conf = dict(
    host="",
    port=0,
    queryFile="D:\\6000_input.txt",
    threadNum=1,
    timeout=500,
    interval=5,  # seconds
    duration=0,  # how long to run
)

stat = dict(
    timeAll=0.0,
    requestCount=0,
    timeoutCount=0,
    errorCount=0,
    contextErrorCount=0,
)

cnt = 0
count = 0
mutex = threading.Lock()

my_logger = logging.getLogger("MyLogger")
handler = logging.handlers.RotatingFileHandler("./jtest_service.log", maxBytes=20971520, backupCount=5)
my_logger.addHandler(handler)
my_logger.setLevel(logging.DEBUG)


def read_line(fp, flg, chunk_size=256 * 256):
    """
    生成器模式，按块读取文件内容
    :param fp: 文件句柄
    :param flg: 内容分隔符
    :param chunk_size: 每次读取文件的内容大小
    :return: 读取的内容
    """
    buff = ''
    while True:
        while flg in buff:
            pos = buff.index(flg)
            yield buff[:pos]
            buff = buff[pos + len(flg):]
        chunk = fp.read(chunk_size)
        if not chunk:
            yield buff
            break
        buff += chunk


class MyTest(threading.Thread):
    """测试执行"""

    def __init__(self):
        threading.Thread.__init__(self)
        self.setDaemon(True)
        log_info = "[[thriftTest presstest start at %s]]" % str(datetime.datetime.now())
        my_logger.info(log_info)
        self.time = time.time()

    @classmethod
    def send_request(cls):
        try:
            transport = TSocket.TSocket(conf["host"], conf["port"])
            transport = TTransport.TFramedTransport(transport)
            protocol = TBinaryProtocol.TBinaryProtocol(transport)
            client = Client(protocol)
            transport.open()

            while True:
                try:
                    with open(conf['queryFile'], 'r', encoding='utf-8') as fp:
                        for r in read_line(fp, '\n'):
                            tmp = r.split('\t')
                            if len(tmp) < 2:
                                continue
                            begin = time.time()
                            result = client.run(tmp[0], int(round(time.time()) * 1000), tmp[1], False)
                            end = time.time()
                            stat["requestCount"] += 1
                            if result.returnCode != 0:
                                stat["contextErrorCount"] += 1
                            elapse = (end - begin) * 1000
                            if elapse > conf["timeout"]:
                                stat["timeoutCount"] += 1
                            stat["timeAll"] += elapse
                except Thrift.TException as ex:
                    stat["errorCount"] += 1
                    print("Thrift.TException, %s" % ex.message)
                    my_logger.error("Error:Thrift.TException, %s" % ex.message)
                    print(sys.exc_info()[0], sys.exc_info()[1])
                except:
                    stat["errorCount"] += 1
                    print("Other Error1!")
                    my_logger.error("Error:Other Error1!")
                    print(sys.exc_info()[0], sys.exc_info()[1])
                finally:
                    transport.close()
        except Thrift.TException as ex:
            print("Thrift.TException, %s" % ex.message)
            my_logger.error("Error:Thrift.TException, %s" % ex.message)
            print(sys.exc_info()[0], sys.exc_info()[1])
        except:
            print("Error:Other Error2!")
            my_logger.error("Error:Other Error2!")
            print(sys.exc_info()[0], sys.exc_info()[1])

    def run(self):
        self.send_request()


class StatThread(threading.Thread):
    """统计"""

    def __init__(self):
        threading.Thread.__init__(self)
        self.setDaemon(True)
        self.cnt = 0
        self.requestCount = 0
        self.timeoutCount = 0
        self.errorCount = 0
        self.contextErrorCount = 0
        self.timeAll = 0
        self.avgTimeCost = 0
        self.avgQPS = 0

    def run(self):
        while True:
            time.sleep(conf["interval"])
            self.cnt += 1
            self.requestCount += stat["requestCount"]
            self.timeoutCount += stat["timeoutCount"]
            self.errorCount += stat["errorCount"]
            self.contextErrorCount += stat["contextErrorCount"]
            self.timeAll += stat["timeAll"]
            self.avgTimeCost = self.timeAll * 1.0 / self.requestCount
            self.avgQPS = self.requestCount * 1.0 / (self.cnt * conf["interval"])
            stat_info = "Total:\n"
            stat_info += "###requestCount=%d, timeoutCount=%d, errorCount=%d, contextErrorCount=%d, avgTimeCost=%f, avgQPS=%f###" \
                         % (self.requestCount, self.timeoutCount, self.errorCount, self.contextErrorCount,
                            self.avgTimeCost, self.avgQPS)
            stat_info += "\nVerbose:\n"
            stat_info += "###requestCount=%d, timeoutCount=%d, errorCount=%d, contextErrorCount=%d, avgTimeCost=%f, avgQPS=%f " \
                         % (stat["requestCount"], stat["timeoutCount"], stat["errorCount"], stat["contextErrorCount"],
                            stat["timeAll"] / stat["requestCount"],
                            stat["requestCount"] * 1.0 / conf["interval"])
            # stat["requestCount"]*1.0/(self.cnt*conf["interval"]))
            # stat["requestCount"]/stat["timeAll"]*1000.0*conf["threadNum"] )
            stat["requestCount"] = 0
            stat["timeoutCount"] = 0
            stat["errorCount"] = 0
            stat["contextErrorCount"] = 0
            stat["timeAll"] = 0.0
            print(stat_info)
            sys.stdout.flush()
            my_logger.info(stat_info)
        os.kill(os.getpid(), signal.SIGKILL)


def quit_test(signum, frame):
    print("pressTest quit!")
    sys.exit(0)


tasks = []


def press_test():
    loop = asyncio.get_event_loop()
    start_time = time.time()

    for i in range(100):
        tasks.append(run())

    end_time = time.time()

    loop.run_until_complete(asyncio.wait(tasks))

    loop.close()

    test_threads = []
    for i in range(conf["threadNum"]):
        mt = MyTest()
        test_threads.append(mt)
        mt.start()

    stat_thread = StatThread()
    stat_thread.start()

    if conf["duration"] != 0:
        signal.signal(signal.SIGALRM, quit_test)
        signal.alarm(conf["duration"] + 2)

    while True:
        time.sleep(36000)

    sys.exit(0)


async def run():
    async with ClientSession() as session:
        async with session.get(url) as response:
            response = await response.read()

            # print(response)


if __name__ == "__main__":

    loop = asyncio.get_event_loop()

    start_time = time.time()

    for i in range(100):
        tasks.append(run())

    end_time = time.time()

    loop.run_until_complete(asyncio.wait(tasks))

    loop.close()

    # print("循环次数：",str(counut))

    print("开始时间：", str(start_time))

    print("结束时间：", str(end_time))

    print("运行时间：", str(end_time - start_time))
