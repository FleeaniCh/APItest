#!/usr/bin/python
# -*- coding: utf-8 -*-

# Author: Renkai
"""
    获取各模块路径
"""
import os

BASEDIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# print(BASEDIR)  # D:\Git\APItest
COMMONDIR = os.path.join(BASEDIR, 'common')
CONFDIR = os.path.join(BASEDIR, 'config')
DATADIR = os.path.join(BASEDIR, 'data')
LIBDIR = os.path.join(BASEDIR, 'library')
LOGDIR = os.path.join(BASEDIR, 'log')
REPORTDIR = os.path.join(BASEDIR, 'report')
CASEDIR = os.path.join(BASEDIR, 'testcase')
# print(CASEDIR)
