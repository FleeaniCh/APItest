#!/usr/bin/python
# -*- coding: utf-8 -*-

# Author: Renkai

import os
import logging
from common.getConfig import myconf
from common.initPath import *
from logging.handlers import TimedRotatingFileHandler

class Log(object):
    @staticmethod
    def getMylog():
        level = myconf.getValue('log','level')
        format = '%(asctime)s - %(name)s-%(levelname)s: %(message)s'
        logging.basicConfig(level=level,format=format)
        # 初始化日志对象
        mylog = logging.getLogger('Kr.r')

        # 拼接日志目录
        log_path = os.path.join(LOGDIR,'report')
        # 生成文件句柄，按天生成日志文件
        fh = TimedRotatingFileHandler(filename=log_path,when='D',backupCount=15,encoding='utf-8')
        # 设置历史日志文件名称的格式，会自动按照某天生成对应的日志
        fh.suffix = "%Y-%m-%d.log"
        fh.setLevel(level)
        fh.setFormatter(logging.Formatter('%(asctime)s - %(name)s-%(levelname)s: %(message)s'))
        # 将文件句柄加入日志对象
        mylog.addHandler(fh)
        return mylog

mylog = Log.getMylog()
mylog.info('测试-info')