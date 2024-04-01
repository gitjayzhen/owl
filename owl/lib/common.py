# -*- coding: utf-8 -*-

"""
@author: jayzhen
@license:  Apache Licence
@file: common.py
@time: 2023/8/18 16:10
"""
import os
import platform
import re
import subprocess
import time
from enum import EnumMeta

import psutil


class Utils(object):

    @staticmethod
    def is_port_used(port_num):
        """
        检查端口是否被占用
        """
        flag = False
        if port_num is None:
            return flag
        try:
            # 能够获得到内容证明端口被占用
            cmd = 'netstat -ano | findstr %s | findstr LISTENING' % port_num
            if platform.system() != "Windows":
                cmd = 'netstat -an | grep %s | grep LISTEN' % port_num
            port_res = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE,
                                        stderr=subprocess.PIPE).stdout.readlines()
            reg = re.compile(str(port_num))
            for i in port_res:
                i = i.decode()
                if re.search(reg, i):
                    flag = True
        except Exception as e:
            print(str(port_num) + " port get occupied status failure: " + str(e))
        return flag

    @staticmethod
    def is_live_service(port):
        """
        检查这个端口是否存在一个活动的service，就返回这个端口service的pid
        :param port: 这个port来自appiumservice.ini文件
        """
        return Utils.is_port_used(port)

    @staticmethod
    def generate_port_list(port_start, num):
        """
        根据链接电脑的设备来创建num个端口号（整形） 电脑有0-65535个端口
        """
        new_port_list = []
        while len(new_port_list) != num:
            if 0 <= port_start <= 65535:
                if not Utils.is_port_used(port_start):
                    new_port_list.append(port_start)
                port_start = port_start + 1
        return new_port_list

    @staticmethod
    def kill_service_by_pid(pid):
        if pid is not None:
            if platform.system() != "Windows":
                os.system("kill -9 " + str(pid))
                time.sleep(3)
            else:
                os.system("taskkill -F -PID" + str(pid))
            print("进程PID：%s 关闭端口服务成功" % pid)

    @staticmethod
    def find_and_kill_processes(process_name):
        # 遍历所有运行的进程
        for p in psutil.process_iter(['pid', 'name']):
            # 检查进程名是否包含指定的字符串
            if process_name.lower() in p.info['name'].lower():
                print(f"Found process with PID: {p.info['pid']} and name: {p.info['name']}")
                try:
                    # 尝试关闭进程
                    p.kill()
                    print(f"Killed process with PID: {p.info['pid']}")
                except (psutil.NoSuchProcess, PermissionError):
                    print(f"Failed to kill process with PID: {p.info['pid']}")

    @staticmethod
    def get_system_symbal():
        system = platform.system()
        if system == "Windows":
            print("The system is Windows.")
        elif system == "Linux":
            print("The system is Linux.")
        elif system == "Darwin":
            print("The system is macOS.")
        else:
            print("Unknown system.")


class EnumDirectValueMeta(EnumMeta):
    """
    可以解决调用枚举属性时，由类型 enum 变成 string
    需要枚举类继承: Enum, metaclass=EnumDirectValueMeta
    """

    def __getattribute__(cls, name):
        value = super().__getattribute__(name)
        if isinstance(value, cls):
            value = value.value
        return value
