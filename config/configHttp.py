#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2018/11/8 16:25
# @Author : CT
# @Site : 
# @File : test11.py
# @Software: PyCharm

# 这个文件主要来通过get、post等方法来进行http请求，并拿到请求响应。


from common.Basedate import Basedata
from requests import exceptions
import requests
import json

#
# headers = {
#         'content-type': 'application/x-www-form-urlencoded',
#         'User-Agent': 'okhttp/3.8.1'
#     }

# ,headers=headers

# 实例化对象
basedata = Basedata()



class Run_http():

    # 定义post请求方法.参数url和data
    def post(self, url, data, headers):
        print(basedata.get_nowtime(), ':', url)
        print(basedata.get_nowtime(), ':', json.dumps(headers))
        print(basedata.get_nowtime(), ':', json.dumps(data))
        response = requests.post(url=url, json=data, headers=headers).json()
        response['request'] = data
        resandreq = json.dumps(response, ensure_ascii=False, sort_keys=True)
        print(basedata.get_nowtime(), ':', resandreq)
        return resandreq

    def get(self, url, data, headers):
        print(basedata.get_nowtime(), ':', url)
        print(basedata.get_nowtime(), ':', json.dumps(headers))
        print(basedata.get_nowtime(), ':', json.dumps(data))
        response = requests.get(url=url, params=data, headers=headers).json()
        response['request'] = data
        resandreq = json.dumps(response, ensure_ascii=False, sort_keys=True)
        print(basedata.get_nowtime(), ':', resandreq)
        return resandreq

    def run_http(self, method, url, data, headers):
        try:
            # 打印请求
            result = None
            if method == "post":
                result = self.post(url, data, headers)
            elif method == "get":
                result = self.get(url, data, headers)
            else:
                print(basedata.get_nowtime(), "method值错误")
            return result
        except exceptions.Timeout:
            return {"请求超时"}
        except exceptions.InvalidURL:
            return {"非法url"}
        except exceptions.HTTPError:
            return {"http请求错误"}
        except Exception as e:
            return {"错误原因:%s" % e}