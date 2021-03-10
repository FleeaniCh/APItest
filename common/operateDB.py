#!/usr/bin/python
# -*- coding: utf-8 -*-

# Author: Renkai

import pymysql
from common.getConfig import myconf

class OperateDB(object):
    """数据库操作类"""
    def __init__(self):
        self.host = myconf.getValue('db', 'host')
        self.port = myconf.getValue('db', 'port')
        self.user = myconf.getValue('db', 'user')
        self.passwd = myconf.getValue('db', 'pwd')
        self.database = myconf.getValue('db', 'database')
        self.charset = myconf.getValue('db', 'charset')

    def connectDB(self):
        try:
            self.db = pymysql.connect(host=self.host, port=self.port, user=self.user,
                                      password=self.passwd, database=self.database, charset=self.charset)
            return True, '数据库连接成功'
        except Exception as e:
            return False, '连接数据库[' + str(e) + ']失败'

    def closeDB(self):
        self.db.close()

    def execSql(self, sql):
        isOk, result = self.connectDB()
        if isOk is False:
            return isOk, result
        try:
            cursor = self.db.cursor()  # 创建游标，用于执行sql语句
            cursor.execute(sql)
            res = cursor.fetchone()  # 获取返回数据
            if res is not None and 'select' in sql.lower(): # 判断是否为读取数据
                des = cursor.description[0]  # 取第一列
                result = dict(zip(des, res))  # 将返回数据格式化成json串
            elif res is None and ('insert' in sql.lower() or 'update' in sql.lower()):  # 判断是否为插入数据
                self.db.commit()
                result = ''  # 插入数据不需要返回
            cursor.close()
            self.closeDB()
            return True, result
        except Exception as e:
            return False, 'SQL执行失败，原因[' + str(e) + ']'

