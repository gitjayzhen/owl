# -*- coding:UTF-8 -*-


import sys
import time
import signal
import random
import logging
import logging.handlers
import datetime
import re
import threading
import json

from thrift import Thrift
from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol

conf = dict(
    host="",
    port=0,
    # queryFile = "user.txt",
    threadNum=8,
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
handler = logging.handlers.RotatingFileHandler("./get_req.log", maxBytes=20971520, backupCount=5)
my_logger.addHandler(handler)
my_logger.setLevel(logging.DEBUG)


class MyTest(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.setDaemon(True)
        log_info = "[[thriftTest presstest start at %s]]" % str(datetime.datetime.now())
        my_logger.info(log_info)
        self.time = time.time()
        # self.queryList = queryList
        # print self.queryList

    def send_request(self):
        pass
        # try:
        #    # print query
        #     transport = TSocket.TSocket(conf["host"], conf["port"])
        #     transport = TTransport.TFramedTransport(transport)
        #     protocol = TBinaryProtocol.TBinaryProtocol(transport)
        #     client = CatSvr.Client(protocol)
        #     transport.open()
        #
        #     while True:
        #         try:
        #             req = ActivityReq()
        #             req.uid = random.randint(10000, 1000000)
        #             # req.uid=0
        #             req.qq = 1053867522
        #
        #             # req.page_start = ""
        #             req.start = 0
        #             req.limit = 10
        #
        #             req.context_src = "ld.app.first.category"
        #
        #             begin = time.time()
        #
        #             result = client.get_category_activity_list_req(req)
        #
        #             result_num = len(result.idlist)
        #             if result_num<=0:
        #                 stat["requestCount"]+= 1
        #                 # print result
        #             # result=json.loads(str(result), encoding="utf-8")
        #             # print result.idlist
        #
        #             end = time.time()
        #             stat["requestCount"] += 1
        #
        #             # if len(result)<=2:
        #             #    stat["contextErrorCount"] += 1
        #             #    print query
        #
        #             elapse = (end - begin) * 1000
        #             if elapse > conf["timeout"]:
        #                 stat["timeoutCount"] += 1
        #             stat["timeAll"] += elapse
        #
        #         except Thrift.TException as ex:
        #             stat["errorCount"] += 1
        #             print "Thrift.TException, %s" % (ex.message)
        #             my_logger.error("Error:Thrift.TException, %s" % (ex.message))
        #             print  sys.exc_info()[0],sys.exc_info()[1]
        #         except:
        #             stat["errorCount"] +=1
        #             print "Other Error1!"
        #             my_logger.error("Error:Other Error1!")
        #             print  sys.exc_info()[0],sys.exc_info()[1]
        #     transport.close()
        # except Thrift.TException, ex:
        #     print "Thrift.TException, %s" % (ex.message)
        #     my_logger.error("Error:Thrift.TException, %s" % (ex.message))
        #     print  sys.exc_info()[0],sys.exc_info()[1]
        # except:
        #     print "Error:Other Error2!"
        #     my_logger.error("Error:Other Error2!")
        #     print  sys.exc_info()[0],sys.exc_info()[1]

    def run(self):
        # query = random.choice(self.queryList).rstrip("\n")
        # print query
        self.send_request()


class StatThread(threading.Thread):
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
                         % (self.requestCount, self.timeoutCount, self.errorCount, self.contextErrorCount, \
                            self.avgTimeCost, self.avgQPS)
            stat_info += "\nVerbose:\n"
            stat_info += "###requestCount=%d, timeoutCount=%d, errorCount=%d, contextErrorCount=%d, avgTimeCost=%f, avgQPS=%f " \
                         % (stat["requestCount"], stat["timeoutCount"], stat["errorCount"], stat["contextErrorCount"], \
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


def quitTest(signum, frame):
    print("pressTest quit!")
    sys.exit(0)


def PressTest():
    """try:
        f = open(conf["queryFile"], "r")
    except IOError:
        print "thriftTest-files does not exist!"
        sys.exit(-1)

    queryList = f.readlines()
    #print queryList
    """
    test_threads = []
    for i in range(conf["threadNum"]):
        work = MyTest()
        test_threads.append(work)
        work.start()

    stat_thread = StatThread()
    stat_thread.start()

    if conf["duration"] != 0:
        signal.signal(signal.SIGALRM, quitTest)
        signal.alarm(conf["duration"] + 2)

    while True:
        time.sleep(36000)
    sys.exit(0)


if __name__ == "__main__":
    PressTest()
