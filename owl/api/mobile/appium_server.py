# -*-coding: utf8 -*-

"""
@author: jayzhen
@time: 2024/4/1
"""

import subprocess
import threading
import time
from multiprocessing import Process

from owl.configs.appium_cfg import AppiumServiceConfiger
from owl.api.mobile.adb.adb import AndroidDebugBridge
from owl.exception.device_type import NoDeviceConnectionException
from owl.lib.common import Utils
from owl.lib.reporter.logging_porter import LoggingPorter


class ServerRunner(threading.Thread):

    def __init__(self, cmd):
        threading.Thread.__init__(self)
        self.cmd = cmd

    def run(self):
        """
        尽可能使用 subprocess 代替 os.system 执行命令，避免一些错误
        """
        p = subprocess.Popen(self.cmd, shell=True, stderr=subprocess.PIPE, stdout=subprocess.PIPE)
        p.wait()
        time.sleep(5)


class AppiumServerRunner(object):

    def __init__(self):
        self.log4py = LoggingPorter()
        self.cfg = AppiumServiceConfiger()
        self.adb = AndroidDebugBridge()
        self.appium_log_path = self.cfg.get_appium_log_path()
        self.appium_server_port_list = []
        self.mobile_list = []

    def __gen_port_list(self, start):
        """
        只用传送一个开始值，就行了
        """
        if self.mobile_list is not None:
            device_num = self.mobile_list
        else:
            device_num = self.adb.get_device_list()
        port_list = Utils.generate_port_list(start, len(device_num))
        return port_list

    def __gen_server_command(self):
        """
        generate_port_list (service_port, conn_port, udid)->command
        :return {} 是一个以端口号为 key 的 dict
        """
        self.appium_server_port_list = self.__gen_port_list(4490)
        # 将 server_cmd_map dict --> {port:cmd,port1:cmd2} ,port 留作执行 cmd 后的端口校验
        server_cmd_map = {}
        for i in range(len(self.mobile_list)):
            server_cmd_map[str(self.appium_server_port_list[i])] = self.__server_command(
                self.appium_server_port_list[i],
                str(self.appium_log_path) + str(self.mobile_list[i]))
        return server_cmd_map

    @classmethod
    def __server_command(cls, port, log_path):
        # 命令中如果带有路径尽量使用斜杠，不使用反斜杠（win环境中是单个），如使用记得变成双斜杠 appium_path = 'start /b node
        # D:/Android/Appium/node_modules/appium/lib/server/main.js -p ' 这两个方式都可以在后台启动一个appium的服务 cmd = "start /b
        # appium -p " + str(self.appium_port_list[i]) + " -a 127.0.0.1" + " -bp " + str(self.bootstrap_port_list[
        # i]) + " -U " + str(self.device_list[i]) + " >" + str(self.appium_log_path) + str(self.device_list[i]) +
        # ".txt"
        # cmd = "nohup appium -p " + str(self.appium_port_list[i]) + " -a 127.0.0.1" + " -bp " + str(
        #     self.bootstrap_port_list[i]) + " -U " + str(self.device_list[i]) + " >" + str(
        #     self.appium_log_path) + str(self.device_list[i]) + ".txt"
        # nohup appium -p {} -a 127.0.0.1 -bp {} -U {} > {}.txt 2>&1 &
        return "nohup appium server -p {} -a 127.0.0.1 --base-path=/wd/hub > {}.txt 2>&1 &".format(port, log_path)

    def stop_all_appium_server(self):
        """
        因为当前服务执行后，一定会有端口写入配置文档，所以直接读取配置文档来关闭服务
        """
        asc = AppiumServiceConfiger()
        server_list = asc.get_all_appium_server_port()
        if len(server_list) <= 0:
            self.log4py.debug("请你确认是否有 appium 服务启动")
            return None
        for p in server_list:
            self.log4py.info("准备关闭端口 %s 的服务" % p)
            if Utils.is_live_service(p):
                Utils.kill_service_by_pid(p)

    @classmethod
    def reset_appium_server(cls):
        Utils.find_and_kill_processes("appium")

    def check_services(self, times=10):
        # 检查服务是否已经启动
        begin = time.time()
        flag = False
        for i in range(len(self.appium_server_port_list)):
            p = self.appium_server_port_list[i]
            while time.time() - begin <= times:
                flag = Utils.is_live_service(p)
                if flag:
                    self.log4py.info("appium server 端口为 {} 的服务已经启动".format(p))
                    # 服务启动正常，就写入配置文件
                    self.cfg.set_appium_uuid_port(self.mobile_list[i], self.appium_server_port_list[i])
                    break
            if not flag:
                self.log4py.info("appium server 端口为 {} 的服务未启动".format(p))

    def start_servers(self):
        """
        根据 appium 端口、链接手机端口、手机 serialno 表示，创建一个服务器; 启动有些延迟
        需要将appium和手机sno放到文件中供初始化driver使用，xml、ini、conf、json文件格式都行
        如果启动了：写入配置的内容如何定义？后续有设备连接上了，如果刷新配置文件中的内容？
        最终还是没有设备就不启动了（或者给个开关也行）
        """
        self.reset_appium_server()
        self.mobile_list = self.adb.get_device_list()
        if self.mobile_list is None or len(self.mobile_list) <= 0:
            self.log4py.debug("当前没有设备连接到pc，无法进行appium服务端口的映射，无法启动对应的服务")
            assert NoDeviceConnectionException()
        service_list = self.__gen_server_command()
        for port, cmd in service_list.items():
            self.log4py.info("通过线程启动服务的命令：{}".format(cmd))
            t1 = ServerRunner(cmd)
            p = Process(target=t1.start())
            p.start()
            time.sleep(5)
        self.check_services()

    def start_server(self, sno):
        self.mobile_list = [sno]
        self.appium_server_port_list = self.__gen_port_list(4824)
        port = self.appium_server_port_list[0]
        appium_cmd = self.__server_command(port, str(self.appium_log_path) + str(sno))
        self.log4py.info("通过线程启动服务的命令：{}".format(appium_cmd))
        t1 = ServerRunner(appium_cmd)
        p = Process(target=t1.start())
        p.start()
        time.sleep(5)
        self.check_services()
        return port


if __name__ == '__main__':
    # 注意不要重复执行
    AppiumServerRunner().start_servers()
