#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@version: v1.0
@author: jayzhen
@license: Apache Licence 
@message: jayzhen_testing@163.com
@software: PyCharm
@file: csv_las_to_ermas.py
@time: 2017/12/27 23:05

ftp登陆连接
from ftplib import FTP            #加载ftp模块
ftp=FTP()                         #设置变量
ftp.set_debuglevel(2)             #打开调试级别2，显示详细信息
ftp.connect("IP","port")          #连接的ftp sever和端口
ftp.login("user","password")      #连接的用户名，密码
print ftp.getwelcome()            #打印出欢迎信息
ftp.cmd("xxx/xxx")                #进入远程目录
bufsize=1024                      #设置的缓冲区大小
filename="filename.txt"           #需要下载的文件
file_handle=open(filename,"wb").write #以写模式在本地打开文件
ftp.retrbinaly("RETR filename.txt",file_handle,bufsize) #接收服务器上文件并写入本地文件
ftp.set_debuglevel(0)             #关闭调试模式
ftp.quit()                        #退出ftp

ftp相关命令操作
ftp.cwd(pathname)                 #设置FTP当前操作的路径
ftp.dir()                         #显示目录下所有目录信息
ftp.nlst()                        #获取目录下的文件
ftp.mkd(pathname)                 #新建远程目录
ftp.pwd()                         #返回当前所在位置
ftp.rmd(dirname)                  #删除远程目录
ftp.delete(filename)              #删除远程文件
ftp.rename(fromname, toname)#将fromname修改名称为toname。
ftp.storbinaly("STOR filename.txt",file_handel,bufsize)  #上传目标文件
ftp.retrbinary("RETR filename.txt",file_handel,bufsize)  #下载FTP文件
"""
from ftplib import error_perm
from ftplib import FTP
import os
import socket
import getopt
import sys
import time

class FTPController:
    '''ftp自动下载、自动上传脚本，可以递归目录操作'''
    def __init__(self, hostaddr, username, password, remotedir, port=21):
        self.hostaddr = hostaddr
        self.username = username
        self.password = password
        self.remotedir = remotedir
        self.port = port
        self.ftp = FTP()
        self.file_list = []
        # self.ftp.set_debuglevel(2)

    def __del__(self):
        # self.ftp.close()
        self.ftp.quit()
        print "ftp连接已经关闭"
        # self.ftp.set_debuglevel(0)

    def login(self):
        ftp = self.ftp
        try:
            timeout = 300
            socket.setdefaulttimeout(timeout)
            ftp.set_pasv(True)
            print u'开始连接到 %s' % (self.hostaddr)
            ftp.connect(self.hostaddr, self.port)
            print u'成功连接到 %s' % (self.hostaddr)
            print u'开始登录到 %s' % (self.hostaddr)
            ftp.login(self.username, self.password)
            print u'成功登录到 %s' % (self.hostaddr)
            print ftp.getwelcome()
        except Exception:
            print u'连接或登录失败'
        try:
            ftp.cwd(self.remotedir)
            print "当前工作目录是：" + str(ftp.pwd())
            print "==============================================================="
        except(Exception):
            print u'切换目录失败'

    def is_same_size(self, localfile, remotefile):
        try:
            remotefile_size = self.ftp.size(remotefile)
        except:
            remotefile_size = -1
        try:
            localfile_size = os.path.getsize(localfile)
        except:
            localfile_size = -1
        print ('localfile_size:%d  remotefile_size:%d' % (localfile_size, remotefile_size))
        if remotefile_size == localfile_size:
            return 1
        else:
            return 0

    def is_exist_file(self, filename, remotedir='./'):
        """
        :param filename:
        :param remotedir:
        :return: 如果存在是文件返回1，是目录返回2，不存在返回0
        """
        self.file_list = []
        self.ftp.cwd(remotedir)
        self.ftp.dir(self.get_file_list)
        for tmp in self.file_list:
            if filename == tmp[1]:
                if tmp[0] == '-':
                    return 1
                elif tmp[0] == 'd':
                    return 2
        return 0

    def download_file(self, localfile, remotefile):
        if self.is_same_size(localfile, remotefile):
            print (u'%s 文件大小相同，无需下载' % localfile)
            return
        else:
            print (u'>>>>>>>>>>>>下载文件 %s ... ...' % localfile)
        # return
        file_handler = open(localfile, 'wb')
        self.ftp.retrbinary(u'RETR %s' % (remotefile), file_handler.write)
        file_handler.close()

    def download_files(self, localdir='./', remotedir='./'):
        try:
            self.ftp.cwd(remotedir)
        except:
            print (u'目录%s不存在，继续...' % remotedir)
            return
        if not os.path.isdir(localdir):
            os.makedirs(localdir)
        print (u'切换至目录 %s' % self.ftp.pwd())
        self.file_list = []
        # 将get_file_list
        self.ftp.dir(self.get_file_list)
        # remotenames 应该是一个二维数组，保存文件类型和文件名
        remotenames = self.file_list
        print remotenames
        # for item in remotenames:
        #     filetype = item[0]
        #     filename = item[1]
        #     local = os.path.join(localdir, filename)
        #     if filetype == 'd':
        #         self.download_files(local, filename)
        #     elif filetype == '-':
        #         self.download_file(local, filename)
        # self.ftp.cwd('..')
        # debug_print(u'返回上层目录 %s' % self.ftp.pwd())

    def upload_file(self, localfile, remotefile):
        if not os.path.isfile(localfile):
            return
        if self.is_same_size(localfile, remotefile):
            print (u'跳过[相等]: %s' % localfile)
            return
        file_handler = open(localfile, 'rb')
        self.ftp.storbinary('STOR %s' % remotefile, file_handler)
        file_handler.close()
        print (u'已传送: %s' % localfile)

    def upload_files(self, localdir='./', remotedir='./'):
        """批量上传文件"""
        if not os.path.isdir(localdir):
            return
        localnames = os.listdir(localdir)
        try:
            self.ftp.cwd(remotedir)
        except:
            print "远程没有该目录：" + remotedir + "准备创建"
            self.ftp.mkd(remotedir)
            self.ftp.cwd(remotedir)
        for item in localnames:
            src = os.path.join(localdir, item)
            src = unicode(src, 'utf8')       # 避免中文路径引发的灾难
            if os.path.isdir(src):
                try:
                    self.ftp.mkd(item)
                except:
                    print (u'目录已存在 %s' % item)
                self.upload_files(src, item)
            else:
                if self.delete_file(item):
                    self.upload_file(src, item)
        self.ftp.cwd('..')

    def get_file_list(self, line):
        """作为ftp.dir的回调方法"""
        ret_arr = []
        file_arr = [line[0], line.split(" ")[-1]]
        if file_arr[1] not in ['.', '..']:
            self.file_list.append(file_arr)

    def delete_file(self, filename, remotedir='./'):
        try:
            if self.is_exist_file(filename, remotedir) == 1:
                print "准备删除文件：" + filename
                print self.ftp.pwd()
                self.ftp.delete(filename)

            if self.is_exist_file(filename) == 0:
                return True
        except error_perm as e:
            print "删除文件报错"
            print str(e)

    def delete_dir(self, remotedir='./'):
        """谨慎使用，会删除当前工作目录下的文件夹"""
        if remotedir == './' or remotedir == '.' or remotedir == '..':
            return
        if self.is_exist_file(remotedir) == 2:
            # 暂时先不实现这个功能
            pass

    def check_file_num(self, remotedir='./'):
        """返回指定目录下的文件数和目录数"""
        self.file_list = []
        try:
            self.ftp.cwd(remotedir)
        except:
            print "远程没有该目录：" + remotedir
            return
        self.ftp.dir(self.get_file_list)
        file_num = 0
        dir_num = 0
        for i in self.file_list:
            if i[0] == 'd':
                dir_num += 1
            elif i[0] == '-':
                file_num += 1
        return file_num, dir_num


def script_help():
    print """上传文件到ermas使用的ftp上
    1.获取指定的csv文件夹
    2.获取到文件夹后，进行上传

    cmd:
    """.decode("utf-8")
    print "\t{} -t : 查询指定时间的文件，如：test.py -t 20170830 -> 包含日期的文件列表.".format(os.path.basename(__file__)).decode("utf-8")


if __name__ == '__main__':

    parttern, args = getopt.getopt(sys.argv[1:], "hp:")
    if len(parttern) < 0 or parttern == "":
        sys.exit(0)
    for option, value in parttern:
        if option == '-t':
            begin = time.time()
            if len(value) != 8:
                print ">>>请确认你输入的参数是否是8位数字格式的日期,如：20180808.".decode("utf-8")
                sys.exit(0)
            # 配置如下变量
            hostaddr = '192.168.13.27'  # ftp地址
            username = 'ftp'  # 用户名
            password = 'xB3ef8Rjx9a'  # 密码
            port = 21  # 端口号

            rootdir_remote = '/cuishou'  # 远程目录

            fc = FTPController(hostaddr, username, password, rootdir_remote, port)
            fc.login()

            workdir_local = os.path.join(os.getcwd(), value)  # 本地目录
            if os.path.exists(workdir_local) and os.path.isdir(workdir_local):
                workdir_remote = value  # 这个目录是基于 rootdir_remote
                fc.upload_files(workdir_local, workdir_remote)
                print fc.check_file_num(workdir_remote)
            print time.time() - begin, "s"
        elif option == '-h':
            script_help()
