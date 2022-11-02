# -*- coding:UTF-8 -*-

"""
@version: python2.7
@author: ‘jayzhen‘
@contact: jayzhen_testing@163.com
@site: https://github.com/gitjayzhen
@software: PyCharm Community Edition
@time: 2017/3/29  13:12
"""

import os
import smtplib
from email.mime.text import MIMEText
from email.header import Header
from email.mime.multipart import MIMEMultipart

from framework.utils.file.file_inspector import FileInspector
from framework.utils.file.ConfigReader import ConfigReader
from framework.utils.reporter.logging_porter import LoggingPorter


class EmailController(object):

    def __init__(self):
        self.fc = FileInspector()
        bools = self.fc.is_has_file("owl-framework.ini")
        if bools:
            fp = self.fc.get_file_abspath()
            conf = ConfigReader(fp)
            self.smtp_host = conf.get_value("message", "smtp_host")
            self.pop3_host = conf.get_value("message", "pop3_host")
            self.receiver = conf.get_value("message", "receiver").split(",")
            self.receiver_pa = conf.get_value("message", "receiver_pa")
            self.sender = conf.get_value("message", "sender")
            self.sender_pa = conf.get_value("message", "sender_pa")
            self.report_path = os.path.join(self.fc.get_project_path(), conf.get_value("ResultPath", "htmlreportPath"))
        self.log4py = LoggingPorter()

    def send_email_is_html(self):
        latestfpath, fname, currentfolder = self.fc.get_latest_file(self.report_path)
        msgRoot = MIMEMultipart('related')
        ff = open(latestfpath, 'rb')
        message = MIMEText(str(ff.read()), 'html', 'utf-8')
        ff.close()
        message['From'] = self.sender
        # message['To'] = self.receiver
        subject = '实验室数字化平台-自动化测试报告'
        message['Subject'] = Header(subject, 'utf-8')
        msgRoot.attach(message)
        try:
            smtpObj = smtplib.SMTP()
            smtpObj.connect(self.smtp_host)
            smtpObj.login(self.sender, self.sender_pa)
            smtpObj.sendmail(self.sender, self.receiver, msgRoot.as_string())
            self.log4py.debug("SendEmail_withFile邮件发送成功")
            smtpObj.close()
        except Exception as e:
            self.log4py.error("Error: 无法发送邮件::" + str(e))

    def send_email_with_file(self):
        # 创建一个带附件的实例 related   alternative
        message = MIMEMultipart("related")
        # message['from'] = Header("QA jayzhen <%s>" %self.sender, 'utf-8')
        message['from'] = self.sender
        # message['To'] =  Header("Leader <%s>" %self.receiver, 'utf-8')
        # message['To'] = self.receiver   #群发邮件不能使用
        subject = '实验室数字化平台-自动化测试报告'
        message['Subject'] = Header(subject, 'utf-8')
        # 邮件正文内容
        message.attach(MIMEText('<html><br/><h1>基于Spring MVC的实验室数字化平台-自动化测试 V1.0版本 '
                                '-自动化测试报告</h1><br/><h3>附件报告，请下载！（邮件为自动发送勿回）</h3></html>', 'html', 'utf-8'))

        latestfpath, fname, currentfolder = self.fc.get_latest_file(self.report_path)
        # 构造附件1，传送当前目录下的 test.txt 文件
        with open(latestfpath, 'rb') as f:
            att1 = MIMEText(str(f.read()), 'base64', 'utf-8')
        att1["Content-Type"] = 'application/octet-stream'
        # 这里的filename可以任意写，写什么名字，邮件中显示什么名字
        att1["Content-Disposition"] = 'attachment; filename=%s' % fname
        message.attach(att1)
        try:
            smtpObj = smtplib.SMTP()
            smtpObj.connect(self.smtp_host)
            smtpObj.login(self.sender, self.sender_pa)
            smtpObj.sendmail(self.sender, self.receiver, message.as_string())
            self.log4py.debug("SendEmail_withFile邮件发送成功")
            smtpObj.close()
        except Exception as e:
            self.log4py.error("Error: 无法发送邮件::" + str(e))
