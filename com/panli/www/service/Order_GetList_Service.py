#!/usr/bin/env python
# -*- coding: utf-8 -*-

from common.get_token import *
import json




# 实例化对象
# readConfig = readConfig.ReadConfig()
Run_http = configHttp.Run_http()

url = "http://www.panli.com/my/napi/order/GetList"



class OrderGetList_Service():

    # 获取订单列表
    def getOrderList(self, OrderStatus):

        params = {
            "page": 1,
            "pagesize": 20,
            "OrderStatus": OrderStatus
        }

        try:
            results = json.loads(Run_http.get(url, params, get_headers()))
            return results
        except Exception as e:
            print('获取订单列表接口失败:',e)


    # 获取订单列表第一个商品id
    def getFirstProductId(self, OrderStatus):
        res = self.getOrderList(OrderStatus)
        productId = res['Data']['OrderList'][0]['OrderProductInfo']['ProductInfos'][0]['ProductId']

        return productId



if __name__ == '__main__':

    # get_tokenV3("op")
    get_tokenV3("www")

    getList = OrderGetList()
    res = getList.getOrderList(-1);
    print(res)