#!/usr/bin/env python
# -*- coding: utf-8 -*-

from common.get_token import *
import json



# 实例化对象
# readConfig = readConfig.ReadConfig()
Run_http = configHttp.Run_http()

url = "http://www.panli.com/shoppingcart/napi/order/PreorderModeify"


data = {
	"PreOrderId": "PreOrderId",
	"CouponCode": "CouponCode",
    "PayMoney":"123"
}


class OrderPreorderModeify_Service():


    # 生产预订单
    def preorderModeify(self, preOrderId, couponCode, payMoney):

        try:

            data['PreOrderId'] = preOrderId
            data['CouponCode'] = couponCode
            data['PayMoney'] = payMoney

            results = json.loads(Run_http.post(url, data, get_headers()))

            if results["Code"]== 200:
                return results
            else:
                print('接口错误，错误原因：',results["Msg"])

        except Exception as e:
            print('生成预支付订单接口失败:',e)



    # def generatePreOrderIdToBuy(self, cartId):
    #     res = self.generatePreOrderId(cartId)
    #     preOrderId = res['Data']['PreOrderId']
    #     return preOrderId


if __name__ == '__main__':

    get_tokenV3("www")
    get_tokenV3("op")
