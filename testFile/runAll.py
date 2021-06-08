#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019/11/8 16:25
# @Author : CT
# @Site : 
# @File : test11.py
# @Software: PyCharm

#开始执行接口自动化，项目工程部署完毕后直接运行该文件即可
#
import unittest

from testFile.Log import MyLog
from config.configEmail import SendEmail
from testFile import readConfig
from testFile import getpathInfo
from common import HTMLTestRunner_PY3
# from apscheduler.schedulers.blocking import BlockingScheduler
import os
import datetime


log =MyLog.get_log()
logger = log.get_logger()

A=readConfig.ReadConfig() #实例化对象，用来读取配置文件里的邮箱有关的内容

username=A.get_email("mail_user")
passwd=A.get_email("mail_pass")
recv=A.get_email("receiver")
print(recv)
title=A.get_email("subject")
content="测试发送邮件 " \
        "接口自动化测试"
email_host = A.get_email("mail_host")
port=A.get_email("mail_port")
ssl_port=A.get_email("ssl_port")
#获取输出的log文件的位置
path1=getpathInfo.get_path()#获取Testfile文件路径
path = os.path.dirname(getpathInfo.get_path()) #获取interfacetest文件路径
result_Path = os.path.join(path, "result")  #把得到的结果resultw文件放入interfacetest路径下report_path%Y%m%d%H%M%S
report_path = os.path.join(result_Path, str(datetime.datetime.now().strftime("%Y%m%d"))) ##获取interfacetest文件路径result/20200824
file1=report_path+"\output.log"
file2=report_path+"\\report.html"
file=[file1,file2]
# file=report_path
# print(file)
m= SendEmail(username,passwd,recv,title,content,email_host,port,ssl_port,file,ssl=True) #实例化邮箱发送

# path = getpathInfo.get_Path()
# report_path = os.path.join(path, 'result')
n_off = A.get_email('on_off')

class AllTest:# 定义一个类运行所有测试用例
    def __init__(self):#初始化一些参数和数据
        global result_reportPath
        result_reportPath =report_path+"\\report.html"#result/201865122258/report.html
        # print(result_reportPath)
        self.caseListFile = os.path.join(path1,'caselist.txt') #配置执行哪些测试文件的配置文件路径
        # print(caseListFile)
        self.caseFile=os.path.join(path,"testCase")#真正的测试断言文件路径
        self.caseList=[]

        # logger.info('result_reportPath',result_reportPath) #讲resultPath的值输入到日志，定位问题
        logger.info('result_reportPath')
        logger.info('caseListFile')
        logger.info('caseFile')

    def set_case_list(self):
        """
         读取caselist.txt文件中的用例名称，并添加到caselist元素组
         :return:
             """
        fb = open(self.caseListFile ,encoding='utf-8')
        for value in fb.readlines():
            data = str(value)
            if data != ''and not data.startswith('#'): # 如果data非空且不以#开头
                # self.caseList.append(data)
                self.caseList.append(data.replace("\n",""))#读取每行数据会将换行转换为\n，去掉每行数据中的\n
        fb.close()

    def set_case_suit(self): #从caselist.txt中读取的case数据用来做测试用例集

        self.set_case_list() #通过set_case_list()拿到caselist元素组,用例py
        test_suit = unittest.TestSuite()
        suit_module=[]

        for case in self.caseList:#从caselist元素组中循环取出case
            case_name = case.split("/")[-1]#通过split函数来将aaa/bbb分割字符串，-1取后面，0取前面
            print(case_name+".py")#打印出取出来的名称
            #批量加载用例，第一个参数为用例存放路径，第一个参数为路径文件名
            discover = unittest.defaultTestLoader.discover(self.caseFile,pattern=case_name+'.py',top_level_dir=None)
            suit_module.append(discover)#将discover存入suite_module元素组
            print('suit_module'+str(suit_module))
            # print("hhhhhhhhh")
        if len(suit_module)>0:
            for suite in suit_module: #如果存在，循环取出元素组内容，命名为suite
                for test_name in suite:#从discover中取出test_name,，使用addTest添加到测试集
                    test_suit.addTest(test_name)

        else:
            print("测试集为空，无测试case用例")
            return None
        return test_suit ##返回测试集

    def run(self):
        #运行测试用例生成报告
        try:
            suit = self.set_case_suit()#调用set_case_suite获取test_suite
            print("try")
            print(str(suit))
            if suit is not  None:#判断test_suite是否为空
                print('if-suit')
                # global fa
                # fa = open(result_reportPath, 'wb+',encoding='utf-8')  # 打开result/20181108/report.html测试报告文件，如果不存在就创建
                # print(fa)
                fp=open(result_reportPath,'wb')
                print(fp)
                # #调用HTMLTestRunner
                runner = HTMLTestRunner_PY3.HTMLTestRunner(stream=fp,title='Test Report',description='Test Description,FIRST TEST')
                runner.run(suit)
                # print("hhhhhhh")

            else:
                print(" no case to run!!!")

        except Exception as e:
            print(str(e))
            logger.info("The test fail.")

        finally:
            print("****************TEST END*****************")
            fp.close()

        #判断邮件发送的开关
        if n_off == 'on':
            # m= SendEmail.send_email()
            m.send_email()
        else:
         print("邮件发送开关配置关闭，请打开开关后可正常自动发送测试报告")


if __name__ == "__main__":
    AllTest().run()









































