import unittest
import configparser
import os
# -------命令行执行报错必加-------
import sys
# 项目根目录地址
rootpath = os.getcwd()[0:os.getcwd().rfind('interfaceTest')] + 'interfaceTest'
sys.path.append(str(rootpath))
# ------------------------------
from BeautifulReport import BeautifulReport
from config.configHttp import basedata



class Main():

    # 获取配置文件内casa详细地址
    def getcastpath(self, pathname):

        # 读取测试用例路径配置文件
        cf = configparser.ConfigParser()
        propertiespath = rootpath + "/config/casepath_properties.ini"
        cf.read(propertiespath)

        # 根据传入pathname获取对应测试用例路径
        castpath = rootpath + cf.get("path", str(pathname))
        return str(castpath)

    # ----------------------------- 主入口 -----------------------------
    # 测试用例必须以【_Testcase】结尾
    # 供Jenkins运行使用
    # pathname对应哪部分需要运行的测试用例（读取配置文件）
    def main(self, pathname):
        # 需要运行的测试用例地址
        case_dir = self.getcastpath(pathname)
        # 加载测试用例
        discover = unittest.defaultTestLoader.discover(case_dir, pattern='*_Testcase.py')
        # 输入测试报告地址
        reportpath = rootpath + '/result'
        # 测试报告文件名
        filename = str(basedata.get_nowtimev2()) + '_' + 'Result'
        # 实例化BeautifulReport模块
        run = BeautifulReport(discover)
        run.report(filename=filename, description=filename, report_dir=reportpath)

if __name__ == '__main__':
    # sys.argv[1] = pathname
    Main().main(str(sys.argv[1]))

