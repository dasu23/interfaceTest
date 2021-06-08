import os
from testFile import readConfig
import logging
from datetime import datetime
import threading
from testFile import  getpathInfo

localReadConfig = readConfig.ReadConfig()


class Log:
    def __init__(self):
        global logPath, resultPath, proDir
        path = getpathInfo.get_path()#获取teseFile文件路径
        proDir=os.path.dirname(path)#获取interface路径，也就是项目路径

        # print(proDir)
        resultPath = os.path.join(proDir, "result")  #把得到的结果result文件放入interface路径下
        # print(resultPath)
        if not os.path.exists(resultPath):
            os.mkdir(resultPath)
        logPath = os.path.join(resultPath, str(datetime.now().strftime("%Y%m%d")))  #%Y%m%d%H%M%S
        # print(logPath)
        if not os.path.exists(logPath):
            os.mkdir(logPath)
        self.logger = logging.getLogger()
        #设置日志级别info以上的
        self.logger.setLevel(logging.INFO)

        # defined handler，输出日志文件名为output.log，FileHandler用于写入日志文件
        handler = logging.FileHandler(os.path.join(logPath, "output.log"))
        # defined formatter，按照年月日时分秒输出格式，formatter格式器
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        #给handler添加formatter
        handler.setFormatter(formatter)
        # 给logger添加handler，也就是handler这个规则， 把文件日志对象添加到日志处理器logger中
        self.logger.addHandler(handler)

    def get_logger(self):
        """
        get logger
        :return:
        """
        return self.logger

    def build_start_line(self, case_no):
        """
        write start line
        :return:
        """
        self.logger.info("--------" + case_no + " START--------")

    def build_end_line(self, case_no):
        """
        write end line
        :return:
        """
        self.logger.info("--------" + case_no + " END--------")

    def build_case_line(self, case_name, code, msg):
        """
        write test case line
        :param case_name:
        :param code:
        :param msg:
        :return:
        """
        self.logger.info(case_name+" - Code:"+code+" - msg:"+msg)

    def get_report_path(self):
        """
        get report file path
        :return:
        """
        report_path = os.path.join(logPath, "report.html")
        return report_path

    def get_result_path(self):
        """
        get test result path
        :return:
        """
        return logPath

    def write_result(self, result):
        """

        :param result:
        :return:
        """
        result_path = os.path.join(logPath, "report.txt")
        fb = open(result_path, "wb")
        try:
            fb.write(result)
        except FileNotFoundError as ex:
            logger.error(str(ex))


class MyLog:
    log = None
    mutex = threading.Lock()

    def __init__(self):
        pass

    @staticmethod
    def get_log():

        if MyLog.log is None:
            MyLog.mutex.acquire()
            MyLog.log = Log()
            MyLog.mutex.release()

        return MyLog.log

if __name__ == "__main__":
    log = MyLog.get_log()
    logger = log.get_logger()
    logger.debug("test debug")
    logger.info("test info")

