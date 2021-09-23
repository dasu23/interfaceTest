#!/usr/bin/env python
# -*- coding: utf-8 -*
# /**生成基础数据**/

import time
import datetime
from common.DataProcess import DataProcess



class Basedata():

    # 格式化成2016-03-20 11:45:39形式
    def get_nowtime(self):
        return time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

    def get_nowtimev2(self):
        nowtime = str(self.get_nowtime())
        return nowtime.replace('-','').replace(':','').replace(' ','')

    # 获取n天前的日期
    def get_beforeTime(self, n):
        # 先获得时间数组格式的日期
        nDayAgo = (datetime.datetime.now() - datetime.timedelta(days=n))
        # 转换为时间戳:
        timeStamp = int(time.mktime(nDayAgo.timetuple()))
        # 转换为其他字符串格式:
        strTime = nDayAgo.strftime("%Y-%m-%d %H:%M:%S")
        return strTime

    # 获取n天后的日期
    def get_afterTime(self, n):
        # 先获得时间数组格式的日期
        nDayAfter = (datetime.timedelta(days=n) - datetime.datetime.now())
        # 转换为时间戳:
        timeStamp = int(time.mktime(nDayAfter.timetuple()))
        # 转换为其他字符串格式:
        strTime = nDayAfter.strftime("%Y-%m-%d %H:%M:%S")
        return strTime

    # 将时间转换为时间戳
    def changeTimeStamp(self,date):
        # 将其转换为时间数组
        timeStruct = time.strptime(date, "%Y-%m-%d %H:%M:%S")
        # 转换为时间戳:
        timeStamp = int(time.mktime(timeStruct))
        return timeStamp

    # 将时间戳转换为日期格式
    def changeStrTime(self,date):
        localTime = time.localtime(date)
        strTime = time.strftime("%Y-%m-%d %H:%M:%S", localTime)
        return strTime

    # 转换时间格式为
    # 2017-11-24 17:30:00 转换为 2017/11/24 17:30:00
    def formatTime(self,date):
        timeStruct = time.strptime(date, "%Y-%m-%d %H:%M:%S")
        strTime = time.strftime("%Y/%m/%d %H:%M:%S", timeStruct)
        return strTime

    # 判断字符串是否是时间
    # 如果不是时间则报错返回False
    def isVaildDate(self, date):
        try:
            if ":" in str(date):
                if DataProcess().hasinstr(["."], date):
                    time.strptime(str(date), "%Y-%m-%d %H:%M:%S.%f")
                else:
                    time.strptime(str(date), "%Y-%m-%d %H:%M:%S")
            else:
                time.strptime(str(date), "%Y-%m-%d")
            return True
        except Exception as e:
            return False

if __name__ == "__main__":
    b = Basedata();
    strdate2 = '123'
    # strdate3 = '2021-04-30'
    # print(strdate2[0:19])

    print(b.isVaildDate(strdate2))