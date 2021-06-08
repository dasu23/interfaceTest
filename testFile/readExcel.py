#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2018/11/8 16:25
# @Author : CT
# @Site : 
# @File : test11.py
# @Software: PyCharm

#https://www.cnblogs.com/yizhipanghu/p/10936855.html
#读取Excel的方法
import xlrd
import os
import json
import csv
from testFile import getpathInfo


#读取表格数据，返回的是一个列表，通过索引得到单元格的值
path = getpathInfo.get_path()

class readExcel():
    # xls_name填写用例的Excel名称 sheet_name该Excel的sheet名称
    def get_xls(self,xls_name,sheet_name):#获取Excel数据

        #获取用例的文件路径,C:\Users\ChenTing\PycharmProjects\interfaceTest\testFile/caselist.xlsx
        xlspath = os.path.join(path,xls_name)
        # print("xlspath值为：",xlspath)
        file = xlrd.open_workbook(xlspath) #打开用例的excel
        sheet = file.sheet_by_name(sheet_name)#获得打开Excel的sheet
        nrows=sheet.nrows #获取sheet的行数
        # 定义存入接口用例
        cls = []

        for i in range(nrows):#根据行数来循环获取Excel的数据并存入cls
            if sheet.row_values(i)[0] != 'case_name': #如果cls中不存在case_name（用例），那么我们把这行的数据添加到cls[]中，row_values(i)[0]取值是第一列的case_name下的值
                cls.append(sheet.row_values(i))

        return cls


if __name__ == '__main__':#测试一下看看是否通过
    x=readExcel()
    # print(x.get_xls("caselist.xlsx","Flash"))#输出sheet(Flash)表格中的内容
    print(x.get_xls('/Users/xujiewei/Downloads/5月入库.xlsx', 'Sheet1')[0][0])#输出第0行第1个数据，列表从0开始的




#
# print(readExcel.get_xls())




# #打开Excel文件，实例化为readbook
# readbook = xlrd.open_workbook(r"C:\Users\ChenTing\PycharmProjects\interfaceTest\testFile\caselist.xlsx")
#
# # #通过sheet名称获取sheet表
# sheet = readbook.sheet_by_name('Sheet1')
#
# #获取表的行数
# nrows = sheet.nrows
# print(nrows)
# #获取表的列数
# ncols = sheet.ncols
#
# #  #获取整行的值
# nrows_value = sheet.row_values(0,ncols)
# # #获取整列的值
# ncols_value = sheet.row_values(0,nrows)
#
#
# #循环读取每一行单元格数据
# def read_data(nrows_value,nrows,ncols):
#     for i in range(nrows):#用行数来循坏读取
#
# #获取i行第一列的数据（0就是第一列）,sheet.row(i)[j]行索引取值，j代表列数
#             # cell_casename = sheet.row(i)[0]
#             j=0
#             cell_casename = sheet.row(i)[j].value
#             cell_menthod = sheet.row(i)[j+1].value
#             cell_url = sheet.row(i)[j+2].value
#             cell_data = sheet.row(i)[j+3].value
#             # print(cell_data)
#
#     return cell_casename,cell_menthod,cell_url,cell_data
#
#
#
# print(read_data(nrows_value,nrows,ncols))
#













