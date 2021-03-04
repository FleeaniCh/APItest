#!/usr/bin/python
# -*- coding: utf-8 -*-

# Author: Renkai

import openpyxl
from common.initPath import *
from common.getConfig import myconf

class GetCase(object):
    def __init__(self, sheet_name=None):
        filename = eval(myconf.getValue('case', 'testCase'))    # str -->> python可执行对象
        self.caseFile = os.path.join(DATADIR, filename)  # 获取用例路径
        # print(self.caseFile)
        self.sheet_name = sheet_name

    def openexcel(self):
        '''获取指定name的excel表'''
        self.wb = openpyxl.open(self.caseFile)
        # print(self.wb)
        if self.sheet_name is not None:
            self.sh = self.wb[self.sheet_name]

    def read_excels(self):
        '''读取并组装用例数据'''
        self.openexcel()
        datas = list(self.sh.rows)  # 将sheet表中每行对象(tuple)转换成(list)元素 -->> 对象
        # [(<Cell 'case1'.A1>, <Cell 'case1'.B1>, <Cell 'case1'.C1>, <Cell 'case1'.D1>, <Cell 'case1'.E1>, <Cell 'case1'.F1>, <Cell 'case1'.G1>, <Cell 'case1'.H1>, <Cell 'case1'.I1>, <Cell 'case1'.J1>)]
        # print(datas)
        title = [i.value for i in datas[0]]  # 将sheet表中的标题行转换成列表元素
        # ['case_id', 'api', 'url', 'title', 'method', 'headers', 'data', 'checkey', 'expected', 'Test result']
        # print(title)
        # 用例数据组装
        cases = []
        for i in datas[1:]:
            data = [k.value for k in i] # 列表推导式：获取每一单元格内容
            # print(data)
            case = dict(zip(title,data))    # 将数据格式化成json串
            # print(case)
            cases.append(case)
        return cases

    def write_excels(self,rows,column,value):
        '''指定单元格写入数据'''
        self.openexcel()
        self.sh.cell(row=rows,column=column,value=value)
        self.wb.save(self.caseFile)


if __name__ == '__main__':
    gc = GetCase('case1')
    # gc.openexcel()
    # print(gc.read_excels())
    # gc.write_excels(4,1,'3')
    print(gc.read_excels())
