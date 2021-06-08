#!/usr/bin/env python
# -*- coding: utf-8 -*-

from common.get_token import *
import json



# 实例化对象
# readConfig = readConfig.ReadConfig()
Run_http = configHttp.Run_http()

url = "http://www.panli.com/shoppingcart/napi/order/GeneratePreOrderId"


data = '''{
	"CartIds": ["8fa64957-3f40-4d43-9c26-79c9489ff83a"],
	"IsAll": false
}'''


class OrderGeneratePreOrderId_Service():


    # 生产预订单
    def generatePreOrderId(self, cartId):

        try:
            request = json.loads(data)
            request['CartIds'][0] = cartId

            results = json.loads(Run_http.post(url, request, get_headers()))

            if results["Data"]["IsSuccess"] == True:
                return results
            else:
                print('接口错误，错误原因：',results["Msg"])

        except Exception as e:
            print('生成预订单接口失败:',e)



    def generatePreOrderIdToBuy(self, cartId):
        res = self.generatePreOrderId(cartId)
        preOrderId = res['Data']['PreOrderId']
        return preOrderId


if __name__ == '__main__':

    get_tokenV3("www")
    get_tokenV3("op")
