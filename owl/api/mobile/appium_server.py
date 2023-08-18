# -*-coding=utf8 -*-
"""
@version: v1.0
@author: jayzhen
@license: Apache Licence
@contact: jayzhen_testing@163.com
@site: https://blog.csdn.net/u013948858
@software: PyCharm
@time: 2017/5/13  
"""
import subprocess
import threading
import time
from multiprocessing import Process

from owl.api.mobile.services.CreateConfigFile import CreateConfigFile
from owl.core.adb.adb import AndroidDebugBridge
from owl.exception.device_type import NoDeviceConnectionException
from owl.lib.common import Utils
from owl.lib.reporter.logging_porter import LoggingPorter


class RunServer(threading.Thread):

    def __init__(self, cmd):
        threading.Thread.__init__(self)
        self.cmd = cmd

    def run(self):
        # 20170802 尽可能使用subprocess代替os.system执行命令，避免一些错误
        # os.system(i)
        # fp = open("AppiumTestProject/testresult/logs4appium/933733961f382.txt", 'a')
        # 20171219 可以使用fp对象传给stdout
        p = subprocess.Popen(self.cmd, shell=True, stderr=subprocess.PIPE, stdout=subprocess.PIPE)
        p.wait()
        time.sleep(5)


class ServicePort(object):

    def __init__(self):
        self.log4py = LoggingPorter()
        self.cfg = CreateConfigFile()
        self.appium_log_path = self.cfg.get_appium_logs_path()
        self.appium_port_list = []
        self.bootstrap_port_list = []
        self.device_list = []
        self.android = AndroidDebugBridge()

        self.tmp = {}

    def __get_port_list(self, start):
        """
        只用传送一个开始值，就行了
        """
        if self.device_list is not None:
            device_num = self.device_list
        else:
            device_num = self.android.get_device_list()
        port_list = Utils.generate_port_list(start, len(device_num))
        return port_list

    def __generate_service_command(self):
        """
        generate_port_list (service_port, conn_port, udid)->command
        :return 是一个以端口号为key的dict
        """
        self.appium_port_list = self.__get_port_list(4490)
        self.bootstrap_port_list = self.__get_port_list(2233)
        # 20170804 将service_cmd list类型换成dict --> {port:cmd,port1:cmd2} ,port留作执行cmd后的端口校验
        service_cmd = {}
        for i in range(len(self.device_list)):
            # 20170802 命令中如果带有路径尽量使用斜杠，不使用反斜杠（win环境中是单个），如使用记得变成双斜杠 appium_path = 'start /b node
            # D:/Android/Appium/node_modules/appium/lib/server/main.js -p ' 这两个方式都可以在后台启动一个appium的服务 cmd = "start /b
            # appium -p " + str(self.appium_port_list[i]) + " -a 127.0.0.1" + " -bp " + str(self.bootstrap_port_list[
            # i]) + " -U " + str(self.device_list[i]) + " >" + str(self.appium_log_path) + str(self.device_list[i]) +
            # ".txt"
            # cmd = "nohup appium -p " + str(self.appium_port_list[i]) + " -a 127.0.0.1" + " -bp " + str(
            #     self.bootstrap_port_list[i]) + " -U " + str(self.device_list[i]) + " >" + str(
            #     self.appium_log_path) + str(self.device_list[i]) + ".txt"
            # nohup appium -p {} -a 127.0.0.1 -bp {} -U {} > {}.txt 2>&1 &
            cmd = "nohup appium -p {} -a 127.0.0.1 > {}.txt 2>&1 &".format(
                str(self.appium_port_list[i]),
                # str(self.bootstrap_port_list[i]),
                # str(self.device_list[i]),
                str(self.appium_log_path) + str(self.device_list[i])
            )
            service_cmd[str(self.appium_port_list[i])] = cmd
        return service_cmd

    def stop_all_appium_server(self):
        """
        20170802
        @auther jayzhen
        @pm 将service_port中启动的service进行关闭
        """
        c = CreateConfigFile()
        server_list = c.get_all_appium_server_port()
        if len(server_list) <= 0:
            self.log4py.debug("请你确认是否有appium服务启动")
            return None
        for p in server_list:
            self.log4py.info("准备关闭端口 %s 的服务" % p)
            if Utils.is_live_service(p):
                Utils.kill_service_by_pid(self.tmp[p])

    def check_service(self, times=5):
        # 检查服务是否已经启动
        begin = time.time()
        flag = False
        for i in range(len(self.appium_port_list)):
            p = self.appium_port_list[i]
            while time.time() - begin <= times:
                flag = Utils.is_live_service(p)
                if flag:
                    self.log4py.info("appium server 端口为{}的服务已经启动,bootstrap监听的端口也已设置好".format(p))
                    # 服务启动正常，就写入配置文件
                    self.cfg.set_appium_uuid_port(self.device_list[i], self.appium_port_list[i], self.bootstrap_port_list[i])
                    break
            if not flag:
                self.log4py.info("appium server 端口为{}的服务未启动".format(p))

    def start_services(self):
        """
        根据appium端口、链接手机端口、手机serialno表示，创建一个服务器;启动有些延迟
        需要将appium和手机sno放到文件中供初始化driver使用，xml、ini、conf、json文件格式都行
        20171218 现在考虑一个问题：是否在没有设备连接的时候就把这个服务启动起来？
        如果启动了：写入配置的内容如何定义？后续有设备连接上了，如果刷新配置文件中的内容？
        最终还是没有设备就不启动了（或者给个开关也行）
        """
        self.device_list = self.android.get_device_list()
        if self.device_list is None or len(self.device_list) <= 0:
            self.log4py.debug("当前没有设备连接到pc，无法进行appium服务端口的映射，无法启动对应的服务")
            assert NoDeviceConnectionException()

        service_list = self.__generate_service_command()
        # 启动服务
        if len(service_list.keys()) > 0:
            for port, cmd in service_list.items():
                self.log4py.info("通过线程启动服务的命令：{}".format(cmd))
                # t1 = RunServer(cmd)
                # p = Process(target=t1.start())
                # p.start()
                # time.sleep(5)
        self.check_service()


if __name__ == '__main__':
    # 注意不要重复执行
    ServicePort().start_services()
