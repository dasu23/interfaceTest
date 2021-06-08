#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2018/11/8 16:25
# @Author : CT
# @Site : 
# @File : test11.py
# @Software: PyCharm

##这个文件主要是配置发送邮件的主题、正文等，将测试报告发送并抄送到相关人邮箱的逻辑。
import smtplib
import base64
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from testFile.Log import MyLog
from testFile import readConfig

# from email.mime.application import MIMEApplication
# import threading
# import glob
# import zipfile
# from testFile.readConfig import ReadConfig
# import  configparser
# from testFile.getpathInfo import get_path

A=readConfig.ReadConfig() #实例化对象，用来读取配置文件里的邮箱有关的内容

class SendEmail(object):
    def __init__(self,username,passwd,recv,title,content,email_host,port,ssl_port,file=None,ssl=False):

        self.username = username    # 用户名
        self.passwd=passwd  # 密码
        self.recv=recv   # 收件人，多个要传list ['a@qq.com','b@qq.com]
        self.title=title    # 邮件标题
        self.content=content    # 邮件正文
        self.file=file  # 附件路径，如果不在当前目录下，要写绝对路径
        self.ssl=ssl    # 是否安全链接
        self.email_host = email_host
        self.port=port
        self.ssl_port=ssl_port

        self.log = MyLog.get_log()
        self.logger = self.log.get_logger()

    def send_email(self):

        msg = MIMEMultipart()
        #发送内容的对象
        # file_path=os.path.dirname()
        # path = os.path.dirname(getpathInfo.get_path())  # 获取interfacetest文件路径
        # file_path = os.path.join(path, "result")  # 把得到的结果resultw文件放入interfacetest路径下
        # for file in file_path:
        att=[]
        if self.file: #处理附件,
            # 通过循环统计附件个数，便于添加添加附件
            for j in range(len(self.file)):
                att.append(j)
            # 通过for循环添加附件，这里的xx表示附件路径，xx为list
            for i in range(len(self.file)):#多个附件发送
                # print(self.file[i-1].split('/')[-1])
                path_file=self.file[i-1] # #获取列表中的单个文件路径
                # print(path_file)
                file=self.file[i-1].split("/")[-1]#获取附件名称
                # print(file)
                try:
                    f=open(path_file,'rb').read()

                except Exception as e:
                        raise Exception('附件打不开！！！')

                else:
                    att[i]=MIMEText(open(path_file,'rb').read(),'base64','utf-8')
                    att[i]["Content-Type"] = 'application/octet-stream'
                    new_file_name = '=?utf-8?b?' + base64.b64encode(file.encode()).decode() + '?='
                    att[i]["Content-Disposition"] = 'attachment; filename="%s"' % (new_file_name)
                    # att[i]["Content-Type"] = 'application/octet-stream;name="%s"' % make_header([(file,'utf-8')]).encode('utf-8')  # 解决附件中文名乱码问题
                    # att[i]["Content-Disposition"] = 'attachment;filename="%s"'% make_header([(file,'utf-8')]).encode('utf-8')
                    msg.attach(att[i])


        msg.attach(MIMEText(self.content))  # 邮件正文的内容

        msg['Subject']=self.title   #邮件主题
        msg["From"] = self.username ## 发送者账号
        msg['To'] = ''.join(self.recv)  # 接收者账号列表,这里必须要把多个邮箱拼接为字符串

        if self.ssl:
            self.smtp=smtplib.SMTP_SSL(self.email_host,port=self.ssl_port)
        else:
            self.smtp=smtplib.SMTP(self.email_host,port=self.port)

        #  # 发送邮件服务器的对象
        self.smtp.login(self.username,self.passwd)
        try:
            # self.smtp.sendmail(self.username,self.recv,msg.as_string())
            self.smtp.sendmail(self.username, self.recv, msg.as_string())
            self.logger.info("The test report has send to developer by email.")
            pass
        except Exception as e:
            self.logger.error(str(e))
            print('邮件发送失败!!!',e)

        else:
            print("邮件发送成功！！！")

        self.smtp.quit()  #关闭邮箱服务


#

# # # print(file)
# #
# #          username = A.get_email("mail_user")
# #         passwd = A.get_email("mail_pass")
# #         recv = A.get_email("receiver")
# #         title = A.get_email("subject")
# #         content = "测试发送邮件"
# #         email_host = A.get_email("mail_host")
# #         port = A.get_email("mail_port")
# #         ssl_port = A.get_email("ssl_port")
# #         # 获取输出的log文件的位置
# #         proDir = readConfig.path  # 获取teseFile文件路径
# #         resultPath = os.path.join(proDir, "result")  # 把得到的结果resultw文件放入teseFile路径下
# #         logPath = os.path.join(resultPath, str(datetime.datetime.now().strftime("%Y%m%d%H%M%S")))
# #         file = logPath + "\output.log"
# # # m= SendEmail(username,passwd,recv,title,content,email_host,port,ssl_port,file,ssl=True)
# SendEmail().send_email()


