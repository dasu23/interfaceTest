#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2018/11/8 16:25
# @Author : CT
# @Site : 
# @File : test11.py
# @Software: PyCharm

#读取配置文件的方法，并返回文件中内容
import os
import  configparser
from testFile import getpathInfo

##调用实例化，这个类返回的路径为C:\Users\ChenTing\PycharmProjects\interfaceTest\testFile:
path = getpathInfo.get_path()
config_path = os.path.join(path,'config.ini')
# print(config_path)

config = configparser.ConfigParser()#读取配置文件的方法实例化
config.read(config_path, encoding='utf-8') #读取config_path的文件

class ReadConfig():
    def get_http(self,name):
        http_value= config.get('HTTP',name)
        return http_value

    def get_email(self,name):
        email_value = config.get('EMAIL',name)
        return email_value

    def get_sql(self,name):
        sql_value = config.get('SQL',name)
        return sql_value


# print('HTTP中的baseurl值为：', ReadConfig().get_http('baseurl'))

if __name__ == '__main__':#测试一下，我们读取配置文件的方法是否可用
    A=ReadConfig()
    print('HTTP中的baseurl值为：', A.get_http('baseurl'))
    print("EMAIL中的开关on_off值为：", A.get_email('on_off'))

