import sys

import HTMLTestRunner
import unittest
import time, os

from config.configEnv import ConfigEnv
from config.configHttp import basedata
from testFile.runAll import file
from BeautifulReport import BeautifulReport as bf

class TestRunner(object):

    def __init__(self, cases="./"):
        self.case = cases

    def get_all_cases(self, class_name):
        return unittest.defaultTestLoader.loadTestsFromTestCase(class_name)

    def run(self, suite, tittle_name='pywinauto test report', description_text=''):
        for filename in os.listdir(self.cases):
            if filename == 'report':
                break
            else:
                os.mkdir(self.cases + '\\report')
        new = time.strftime("%Y-%M-%D-%H_%M_%S")
        filename = self.cases + '\\report\\' + new + 'result.html'
        fp = file(filename, 'wb')

        runner = HTMLTestRunner.HTMLTestRunner(stream=fp, tittle=tittle_name, description=description_text)
        runner.run(suite)
        fp.close()


    # 运行测试用例，生成BeautifulReport
    def bfrun(self, testCaseClass):

        rootpath = ConfigEnv().getrootpath()

        # 报告路径
        reportpath = rootpath + '/result'
        reportname = sys.argv[0].replace(str(sys.path[0]),'').replace('/','').replace('.py','') + '_Result'
        filename = str(basedata.get_nowtimev2()) + '_' + reportname

        suite = unittest.TestSuite()  # 定义一个测试集合
        suite.addTest(unittest.makeSuite(testCaseClass))  # 把写的用例加进来（将TestCalc类）加进来
        run = bf(suite)  # 实例化BeautifulReport模块
        run.report(filename=filename, description=reportname,report_dir=reportpath)



if __name__ == '__main__':
    # test = TestRunner()
    # test.run()


    print(sys.path)
    print(sys.path[2])