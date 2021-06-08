#!/usr/bin/env python
# -*- coding: utf-8 -*-

from common.get_token import *
import json




# 实例化对象
# readConfig = readConfig.ReadConfig()
Run_http = configHttp.Run_http()

url = "http://www.panli.com/shoppingcart/napi/GetList"

data = '''{
	"OnlyCalcCheckedItem": true,
	"LocalShoppingcarts": null
}'''


class ShoppingcartGetList_Service():

    # 获取购物车列表
    def getList(self):

        try:
            request = json.loads(data)
            results = json.loads(Run_http.post(url, request, get_headers()))
            return results
        except Exception as e:
            print('获取购物车列表接口失败:',e)

    # 获取购物车只返回第一个CartId 和金额
    def getListToBuy(self):
        res = self.getList();

        cartinfo = {}
        cartinfo['cartId'] = res['Data']['Shoppingcarts']['Sellers'][0]['Products'][0]['CartId']
        cartinfo['totalAmount'] = res['Data']['Shoppingcarts']['TotalFee']

        return cartinfo



if __name__ == '__main__':

    get_tokenV3("www")
    getList = ShoppingcartGetList_Service()
    res = getList.getListToBuy();
    print(res)