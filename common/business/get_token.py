#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys

import logging
from config.testdata_properties import *
# from config.testdata_properties import www_username as user
# from config.testdata_properties import www_loginpassword as user_pwd
# from config.testdata_properties import op_username as op
# from config.testdata_properties import op_password as op_pwd
from config import configHttp
import json
import urllib.parse

# 实例化对象
# readConfig = readConfig.ReadConfig()
Run_http = configHttp.Run_http()

# 定义header头
headers = {
    "Content-Type": "application/json; charset=utf-8",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36"
}


# Panli前端用户获取token（需要登录密码）
def get_token(username, password):
    global headers
    # 前台用户登录接口
    url_login = "http://www.panli.com/login/napi/user/LoginByUserName"
    loginrequest = {
        "UserName": "happycaoyan",
        "Password": "MTExMTEx",
        "CaptchId": "8e4600b0-2c5e-4a32-8387-3d2c47df91bc",
        "CaptchCode": "1111",
        "Terminal": "5",
        "IsPersitent": "true"
    }

    loginrequest['UserName'] = username
    loginrequest['Password'] = password

    try:
        results = Run_http.run_http('post', url_login, loginrequest, headers)
        cookievalue = json.loads(results)["Data"]["LoginResponseInfo"]['AspnetformValue'].strip()
        token = urllib.parse.quote(cookievalue) #encode编码token
        if cookievalue == '':
            print("token不存在")
        else:
            headers['Cookie'] = '.aspnetform=' + cookievalue
            headers['cookievalue'] = token  # 后端接口需要cookievalue
            headers['Token'] = token

    except:
        print("调用前台用户登录接口失败")
        sys.exit()

    return headers


# Panli后台用户登录接口
def get_tokenforop(username, password):
    global headers

    # 前台用户登录接口
    url_login = "http://op.panli.com/api/login/loginIn"
    loginrequest = {
                "userName": "Panlitest001",
                "userPwd": "111111",
                "vcode": "1111",
                "captchId": "fa9979eb-1777-4307-88fd-fb3b391c1276"
            }

    loginrequest['UserName'] = username
    loginrequest['userPwd'] = password

    results = json.loads(Run_http.run_http('post', url_login, loginrequest, headers))

    if results['message'] == 'success':
        cookievalue = results["data"]["ticket"].strip()
        token = urllib.parse.quote(cookievalue)  # encode编码token
        headers['Token'] = token #后台需要token
        headers['cookievalue'] = token #后端接口需要cookievalue
        # headers['Cookie'] = '.aspnetform=' + cookievalue
    else:
        raise Exception("token不存在")

    return headers



def get_tokenforfulu(username, password):
    global headers

    # 前台用户登录接口
    url_login = "http://app.yugyg.com/purchase-plus/v1/merchant/login"
    loginrequest = {
                    "userName": username,
                    "password": password
                }

    results = json.loads(Run_http.run_http('post', url_login, loginrequest, headers))

    if results['message'] == 'success':
        token = results["data"]["token"].strip()
        headers['token'] = token #后台需要token
    else:
        raise Exception("token不存在")

    return headers




# 根据登录平台，获取配置文件中账号自动登录获取
def get_tokenV3(platform, username = None, pwd = None):
    platform_msg = "【Panli主站:www, Panli后台:op, 愚公:yg, 福禄:fulu】"
    if username == None:
        # --- Panli主站 ---
        if platform == "www":
            headers = get_token(www_username,www_loginpassword)
            return headers
        # --- Panli后台 ---
        elif platform == "op":
            headers = get_tokenforop(op_username, op_password)
            return headers
        # --- 愚公为写死token ---
        elif platform == "yg":
            return get_headers_yg();
        # --- 福禄采购平台 ---
        elif platform == "fulu":
            return get_tokenforfulu(fulu_username,fulu_password);
        else:
            print(platform_msg)
            raise ValueError("get_tokenV3 - 登录平台不正确！！")
    else:
        if platform == "www":
            headers = get_token(username, pwd)
            return headers
        elif platform == "op":
            headers = get_tokenforop(username, pwd)
            return headers
        elif platform == "yg":
            return get_headers_yg();
        elif platform == "fulu":
            return get_tokenforfulu(username, pwd);
        else:
            print(platform_msg)
            raise ValueError("get_tokenV3 - 登录平台不正确！！")


# 获取headers
def get_headers(contentType = 'json'):
    global headers
    if contentType == "json":
        headers['Content-Type'] = 'application/json; charset=utf-8'
    else:
        headers['Content-Type'] = 'application/x-www-form-urlencoded; charset=UTF-8'
    return headers


def get_headers_yg():
    global headers
    headers = {
        "sid": "ygf_16362a631cc9491e8cc0d8b4aa5cf2a3",
        "userToken": "6159bf981a9349ea928077917297f126",
        "shopCode": "d4fefde35d3942bca126d68f60c818f6",
        "clientCode":"1234567890",
        "Content-Type": "application/json;charset=utf-8",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36"
    }
    return headers






if __name__ == '__main__':

    headers = get_tokenV3("www", "20210302001", "MTExMTEx")
    print(get_headers("json"))
    #
    # headers = get_tokenV3("op")
    # print(headers)
    # print(headers['cookievalue'])
    # print(headers['Cookie'])

    # headers = get_tokenV3("yg")
    # print(get_headers())

    # headers = get_tokenV3("fulu")
    # print(headers)


