# -*-coding=utf8 -*-
"""
@version: v1.0
@author: jayzhen
@software: PyCharm
"""
import os
import re

from device_info import DeviceController
from owl.api.mobile.adb.adb import AndroidDebugBridge


class ApkManager(object):

    """
    初始化就先确认存放apk文件的路径,通过config目录的中apk path文件来获取配置文件中path。
    """
    def __init__(self):
        self.sno_list = DeviceController().get_devices()
        self.android = AndroidDebugBridge()
        # absp = os.getcwd()
        absp = "C:\\"
        apkp = os.path.join(absp,"apks")
        if not os.path.exists(apkp):
            os.mkdir(apkp)
        self.result_dir = apkp

    '''
    获取当前文件夹下的最新apk文件，并返回该文件的绝对路径和文件名。
    '''
    def get_latest_apk(self,apklist):
        if apklist is None:
            return None
        st = apklist.sort(key=lambda fn: os.path.getmtime(self.result_dir+"\\"+fn) if not os.path.isdir(self.result_dir+"\\"+fn) else 0)
        # d=datetime.datetime.fromtimestamp(os.path.getmtime(result_dir+"\\"+apklist[-1]))
        # print d
        fname = apklist[-1]
        fpath = os.path.join(self.result_dir,fname)
        return fpath,fname

    '''
    获取当前文件夹下的所有apk文件，返回一个list。
    '''
    def apk_list(self):
        filelist = os.listdir(self.result_dir)
        apklist = []
        for fapk in filelist:
            if re.search(r'\.apk$',fapk):
                apklist.append(fapk)
        return apklist

    '''
    因为该模块会与apk在同一级文件夹下，所以知道文件名后，通过追加路径的方式，返回绝对路径。
    '''
    def apk_abs_path(self, apkName):
        try:
            abspath = os.path.join(self.result_dir,apkName)
            if not os.path.exists(abspath):
                return None
        except TypeError as e:
            return None
        return abspath

    '''
    参数apk是apk的绝对路径，使用aapt命令来获取apk的包名，当然需要配置好aapt的环境变量。
    '''
    def get_apk_package_name(self,apk):
        try:
            if apk is not None:
                res = os.popen("aapt dump badging %s"%apk).read()
                if res is None or len(res)<0:
                    return None
                # reg = "package\: name\=\'(.*?)'"
                reg = "package: name='(.*?)'"
                regc = re.compile(reg)
                res = re.findall(regc,res)
                if res is not None and len(res) >0:
                    pname = str(res[0])
                print(">>> the apk's package name is [%s]"%pname)
                return pname
            else:
                return None
        except Exception as e:
            print("An error occurred environment variable on aapt")
    '''
    使用python的os中的remove方法来删除指定路径的文件，删除之前先判断是否存在该文件。
    '''
    def delete_apk(self, apkpath):
        ap = apkpath
        if os.path.exists(ap):
            os.remove(ap)
            if not os.path.exists(ap):
                return True

    '''
    uninstall_All参数指定要卸载的包名，该方法会调用uninstall_One卸载所有链接在电脑上的手机中的应用
    '''
    def uninstall_all(self,package_name):
        devices = self.sno_list
        if devices is None:
            print (">>>No device is connected")
        else:
            for sno in devices:
                self.uninstall_one(sno,package_name)
    '''
    指定设备，并指定包名进行应用的卸载
    '''
    def uninstall_one(self,sno,package_name):
        uninstall_result = self.android.adb(sno,'uninstall %s'%package_name).stdout.read()
        if re.findall(r'Success',uninstall_result):
            print('>>>[%s] uninstall [%s] [SUCCESS]' %(sno,package_name))
        else:
            print('>>>no assign package')
    '''
    apk_name为apk的绝对路径，该方法会调用install_OneDevice方法，向所有设备安装该应用
    '''
    def install_all_devices(self,apk_name,apk_package_name):
        print(">>>Install all devices")
        device_list = self.sno_list
        if device_list is None:
            print(">>>No device is connected")
        else:
            for sno in device_list:
                self.install_one_device(sno,apk_name,apk_package_name)

    '''
    指定设备名，并指定apk进行安装，安装前会检测手机是否已经安装了该应用，如果有，先卸载
    '''
    def install_one_device(self,sno,apk_name,apk_package_name):
        had_package = self.android.shell(sno,'pm list packages |findstr "%s"'%apk_package_name).stdout.read()
        if re.search(apk_package_name,had_package):
            self.uninstall_one(sno,apk_package_name)
        install_result = self.android.adb(sno,'install %s'%apk_name).stdout.read()
        boolean = self.is_has_package(sno,apk_package_name)
        if re.findall(r'Success',install_result) or boolean:
            print('>>>[%s] adb install %s [SUCCESS]' %(sno,os.path.basename(apk_name)))
        else:
            print('>>>[%s] install %s [FALSE]'%(sno,os.path.basename(apk_name)))

    def cover_install(self,sno,apk_name,apk_package_name):
        install_result = self.android.adb(sno,'install -r %s'%apk_name).stdout.read()
        boolean = self.is_has_package(sno,apk_package_name)
        if re.findall(r'Success',install_result) or boolean:
            print('>>>[%s] adb install %s [SUCCESS]' %(sno,os.path.basename(apk_name)))
        else:
            print('>>>[%s] install %s [FALSE]'%(sno,os.path.basename(apk_name)))

    def is_has_package(self,sno,package_name):
        had_package = self.android.shell(sno,'pm list packages |findstr "%s"'%package_name).stdout.read()
        if re.search(package_name,had_package):
            return True
        else:
            return False

    def clear_app_data(self,sno,package_name):
        b = self.is_has_package(sno, package_name)
        if b:
            res = self.android.shell(sno, "pm clear %s"%package_name).stdout.read()
            if re.search(r'Success',res):
                print(">>> Clear data Success with [%s]"%package_name)
            else:
                print(">>> Clear work ERROR")
        else:
            print(">>> NO Package :",package_name)