#!/usr/bin/python
# -*- coding: utf-8 -*-

# Author: Renkai

import smtplib
from common.getConfig import myconf
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from common.initPath import REPORTDIR
import os

class SendMail(object):
    def __init__(self):
        self.host = myconf.getValue('email','host')
        self.port = myconf.getValue('email','port')
        self.user = myconf.getValue('email','user')
        self.pwd = myconf.getValue('email','pwd')
        self.from_addr = myconf.getValue('email','from_addr')
        self.to_addr = myconf.getValue('email','to_addr')

        self.filename = os.path.join(REPORTDIR,'reporter.html')

    def get_email_host_smpt(self):
        '''连接邮件服务器'''
        try:
            self.smtp = smtplib.SMTP_SSL(host=self.host,port=self.port)
            self.smtp.login(user=self.user,password=self.pwd)
            return True,'连接成功'
        except Exception as e:
            return False,'连接邮箱服务器失败，失败原因['+str(e)+']'

    def made_msg(self):
        '''构建一份邮件'''
        # 创建一个多组件邮件
        self.msg = MIMEMultipart()

        with open(self.filename) as f:
            content = f.read()
        # 创建文本内容
        text_msg = MIMEText(content,_subtype='html',_charset='utf-8')
        # 添加到多组件中
        self.msg.attach(text_msg)

        # 创建邮件的附件
        # report_file = MIMEApplication(content)
        # report_file.add_header('Content-Disposition','attachment',filename=str.split(self.filename,'\\').pop())
        # self.msg.attach(report_file)

        self.msg['subject'] = '自动化测试报告'
        self.msg['form'] = self.from_addr
        self.msg['to'] = self.to_addr

    def send_email(self):
        self.get_email_host_smpt()
        self.made_msg()
        self.smtp.send_message(self.msg,from_addr=self.from_addr,to_addrs=self.to_addr)

        