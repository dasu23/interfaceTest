#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2018/11/8 16:25
# @Author : xx
# @Site : 
# @File : test11.py
# @Software: PyCharm

#获取接口的URL
from testFile  import readConfig
from testFile import readExcel

readConfig = readConfig.ReadConfig()#实例化readConfig类,用于读取配置文件config.ini文件

class geturl_Now():#定义一个方法，读取配置文件中的协议和host，组合成url
    def get_url(self):

        now_url = readConfig.get_http('scheme')+'://'+readConfig.get_http('baseurl')  #从config.ini文件获取协议和host
        return now_url


# print(geturl_Now().get_url()) #Geturl_Now()就是实例化类。不带参数会默认self
#读取表格数据作为请求的参数





