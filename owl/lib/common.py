# -*- coding: utf-8 -*-

"""
@author: jayzhen <jayzhen_testing@163.com>
@site: https://github.com/gitjayzhen
@version: 1.0.0
@license:  Apache Licence
@software: PyCharm & Python 3.7+
@file: common.py
@time: 2023/8/18 16:10
"""
import os
import platform
import re
import subprocess


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
    def kill_service_by_pid(self, pid):
        if pid is not None:
            if platform.system() != "Windows":
                os.system("kill -9 " + str(pid))
            else:
                os.system("taskkill -F -PID" + str(pid))
            print("进程PID：%s 关闭端口服务成功" % pid)
