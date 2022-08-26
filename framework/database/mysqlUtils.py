# -*- coding=utf-8 -*-
'''
Created on 2016年2月20日

@author: jayzhen
'''
import mysql.connector

# 建立链接
conn = mysql.connector.connect(
                       host='127.0.0.1',    #服务器地址
                       port=3306,           #端口号，默认是3306
                       user='root',         #要登陆的用户名
                       passwd='root',       #所要登录用户的秘密
                       db='hb_api',        #所要链接的数据库
                       charset='utf-8'       #设置链接的编码
                       )
cursor = conn.cursor()                      #获取中间人
sql = 'select * from hb_api_user'           #sql语句
cursor.execute(sql)                         #执行sql语句
alll = cursor.fetchall()                    #获取返回的结果集
for i in alll:                              #循环遍历
    print i

cursor.close()                              #关闭资源
conn.close()                                #关闭网络连接