import configparser
import os
import sys



# def runtest(testCaseClass):
#     # 指定批量执行的模块
#     test_module = './'
#     discover = unittest.defaultTestLoader.discover(test_module, pattern="Coupon_GetList_Testcase.py")
#
#     # 报告存放的文件夹
#     dir_path = './'
#
#     # 报告绝对路径
#     report_path = './' + str(basedata.get_nowtime()) + ' result.html'
#     # 打开文件，写入测试结果
#     with open(report_path, 'wb') as f:
#         runner = HTMLTestRunner(stream=f, verbosity=2, title='Math测试报告', description='用例执行详细信息')
#         runner.run(discover)
#     f.close()

import unittest

import exifread
from BeautifulReport import BeautifulReport

from common.TestRunner import TestRunner
from config.configHttp import basedata


def test_path():
    print("sys.path = ", sys.path)
    print("sys.argv = ", sys.argv)
    print("sys.path[0] = ", sys.path[0])
    print("sys.path[1] = ", sys.path[3])
    print("sys.argv[0] = ", sys.argv[0])
    print("__file__ = ", __file__)
    print("os.path.abspath(__file__) = ", os.path.abspath(__file__))
    print("os.path.realpath(__file__) = ", os.path.realpath(__file__))
    print("os.path.dirname(os.path.realpath(__file__)) = ", os.path.dirname(os.path.realpath(__file__)))
    print("os.path.split(os.path.realpath(__file__)) = ", os.path.split(os.path.realpath(__file__)))
    print("os.path.split(os.path.realpath(__file__))[0] = ", os.path.split(os.path.realpath(__file__))[0])
    print("os.getcwd() = ", os.getcwd())







if __name__ == '__main__':

    case_dir = "/Users/xujiewei/dev/自动化/interfaceTest/com/panli/www/testcase"
    discover = unittest.defaultTestLoader.discover(case_dir, pattern='*_Testcase.py')

    print(discover)

    reportpath = "/Users/xujiewei/dev/自动化/interfaceTest/result"
    reportname = sys.argv[0].replace(str(sys.path[0]), '').replace('/', '').replace('.py', '') + '_Result'
    filename = str(basedata.get_nowtimev2()) + '_' + reportname

    run = BeautifulReport(discover)  # 实例化BeautifulReport模块
    run.report(filename=filename, description=reportname, report_dir=reportpath)


