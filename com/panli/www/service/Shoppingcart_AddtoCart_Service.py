#!/usr/bin/env python
# -*- coding: utf-8 -*-

from common.get_token import *
import json




# 实例化对象
# readConfig = readConfig.ReadConfig()


Run_http = configHttp.Run_http()

url = "http://www.panli.com/shoppingcart/napi/Add/"

data = '''{
    "IsManual": false,
    "ProductId": "533084014444",
    "SkuId": "3180020075073",
    "ProductTitle": "桌面上下双屏电脑液晶显示器支架万向伸缩屏幕挂架",
    "ProductLinkUrl": "https://item.taobao.com/item.htm?id=533084014444",
    "Price": "79",
    "Quantity": "2",
    "Source": 2,
    "Memo": "自动化购物车订单备注",
    "LocalShoppingcarts": null
}'''


class ShoppingcartAddtoCart_Service():

    def addtoCart(self, productId, skuId, skuprice, title, linkUrl, quantity):

        try:

            request = json.loads(data)
            request['ProductId'] = productId
            request['SkuId'] = skuId
            request['ProductTitle'] = title
            request['ProductLinkUrl'] = linkUrl
            request['Price'] = skuprice
            request['Quantity'] = quantity

            results = json.loads(Run_http.post(url, request, get_headers()))

            if results["Data"]["IsSuccess"] == True:
                return results
            else:
                print('接口错误，错误原因：',results["Msg"])

        except Exception as e:
            print('加入购物车调用接口失败:',e)


if __name__ == '__main__':
    productId = 'YGF-SPU-1945';
    skuId = '3137';
    skuprice = '449';
    title = 'JBL JR300BT 学生耳机 无线蓝牙耳机 低分贝学习耳机';
    linkUrl = 'http://www.yugyg.com/goods/spu/1945';
    quantity = '2';


    get_tokenV3("op")
    get_tokenV3("www")
    addtocart = ShoppingcartAddtoCart_Service()
    addtocart.addtoCart(productId, skuId, skuprice, title, linkUrl, quantity);
