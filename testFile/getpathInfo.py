#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2018/11/8 16:25
# @Author : CT
# @Site : 
# @File : test11.py
# @Software: PyCharm

#获取项目绝对路径

import os

def get_path():
    path = os.path.abspath(os.path.dirname(__file__))#获取当前目录绝对路径
    # path= os.path.abspath(os.path.dirname(os.path.dirname(__file__)))##获取上一级目录绝对路径
    return path

if __name__ =="__main__":# 执行该文件，测试是否正常
    print("测试路径为  %s:"%get_path())

