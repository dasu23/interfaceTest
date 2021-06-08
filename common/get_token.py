#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys

import logging

from config.testdata_properties import www_username as user
from config.testdata_properties import www_loginpassword as user_pwd
from config.testdata_properties import op_username as op
from config.testdata_properties import op_password as op_pwd
from config import configHttp
import json
import urllib.parse

# 实例化对象
# readConfig = readConfig.ReadConfig()
Run_http = configHttp.Run_http()

# 定义header头
headers = {
    "Content-Type": "application/json;charset=utf-8",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36"
}


# 前端用户获取token（需要登录密码）
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
            headers['Token'] = '' #（将Token置空，否则前台接口会出错）

    except:
        print("调用前台用户登录接口失败")
        sys.exit()

    return headers


# # 前端用户获取token（不需要登录密码）（接口失效）
# def get_tokenV2(username):
#     try:
#         url_login = "http://oldauth.api.panli.com/register/GetUserCookieByUserName.ashx?username=" + username
#
#         results = Run_http.run_http('get', url_login, '', headers)
#         cookievalue = json.loads(results)["CookieValue"].strip()
#
#         if cookievalue == '':
#             print("token不存在")
#         else:
#             # headers['cookievalue'] = cookievalue
#             headers['Cookie'] = '.aspnetform=' + cookievalue
#
#     except:
#         print("调用用户Cookie接口失败")
#
#     return headers


# 后台用户登录接口
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


# 根据登录平台，获取配置文件中账号自动登录获取
def get_tokenV3(platform):

    if platform == "www":
        headers = get_token(user,user_pwd)
        return headers
    else:
        headers = get_tokenforop(op, op_pwd)
        return headers



# 获取headers
def get_headers():
    global headers
    return headers


if __name__ == '__main__':
    # loginrequest = json.loads(data)
    # loginrequest['UserName'] = '番丽001'
    # loginrequest['Password'] = 'MTExMTEx'
    # loginrequest = json.dumps(loginrequest)
    #
    # results = Run_http.run_http('post', url_login, loginrequest, headers)

    # headers = get_token("happycaoyan","MTExMTEx")
    headers = get_tokenV3("www")
    headers = get_tokenV3("op")

    print(headers)
    print(headers['cookievalue'])
    print(headers['Cookie'])

