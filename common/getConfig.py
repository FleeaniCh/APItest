#!/usr/bin/python
# -*- coding: utf-8 -*-

# Author: Renkai

from common.initPath import *
from configparser import ConfigParser


class Config(ConfigParser):
    def __init__(self):
        super().__init__()
        self.conf_file = os.path.join(CONFDIR, 'baseCon.ini')
        super().read(self.conf_file, encoding='utf-8')  # 读取配置文件

    def getAllsection(self):
        '''返回配置文件的所有节点名称'''
        return super().sections()

    def getOptions(self, sectionName):
        '''返回指定节点的key'''
        return super().options(sectionName)

    def getItems(self, sectionName):
        '''返回指定节点的key-value'''
        return super().items(sectionName)

    def getValue(self, sectionName, key):
        '''返回指定节点指定key的值'''
        return super().get(sectionName, key)

    def saveData(self,sectionName,key,value):
        """
            添加配置
        :param sectionName:节点名称section
        :param key:option
        :param value:
        :return:
        """
        super().set(section=sectionName,option=key,value=value)
        super().write(open(self.conf_file,'w'))


if __name__ == '__main__':
    conf = Config()
    # print(conf.getAllsection())
    # print(conf.getOptions('db'))
    # print(conf.getItems('db'))
    # print(conf.get('test_data', 'pwd'))
    conf.saveData('db','newKey','newVlue')
    print(conf.getItems('db'))
