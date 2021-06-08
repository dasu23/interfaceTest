#!/usr/bin/env python
# -*- coding: utf-8 -*-

from common.get_token import *
import json



# 实例化对象
# readConfig = readConfig.ReadConfig()
Run_http = configHttp.Run_http()

url = "http://op.panli.com/api/quality/selfbuyReceivedUpdate"


data = {
    "weight": "1000",
    "isSensitive": 'false',
    "forbiddenType": 0,
    "forbiddenInfo": [
        0
    ],
    "productId": "5997301",
    "changeState": 'true'
}


class QualitySelfbuyReceivedUpdate_Service():


    def selfbuyReceivedUpdate(self, request):

        try:

            results = json.loads(Run_http.post(url, request, get_headers()))

            if results['message'] == 'success':
                return results
            else:
                print('接口错误，错误原因：',results["message"])

        except Exception as e:
            print('后台质检 - 商品管理 - 已订购保存接口失败:',e)



    # 质检已到货普品
    def selfbuyReceivedUpdateForGeneral(self, productId):

        data['productId'] = productId
        res = self.selfbuyReceivedUpdate(data)
        return res



    # 质检已到货敏感品
    def selfbuyReceivedUpdateForSensitive(self, productId, forbiddenInfo):

        data['productId'] = productId
        data['isSensitive'] = 'true'
        data['forbiddenType'] = 1
        data['forbiddenInfo'] = forbiddenInfo
        res = self.selfbuyReceivedUpdate(data)
        return res


if __name__ == '__main__':

    # get_tokenV3("www")
    get_tokenV3("op")

