#!/usr/bin/env python
# -*- coding: utf-8 -*-


from common.get_token import *
import json



# 实例化对象
# readConfig = readConfig.ReadConfig()
Run_http = configHttp.Run_http()

url = "http://op.panli.com/api/purchase/UpdateOrderStatus"


data = {
    "productId": "OrderId",
    "status": "15"
}


class PurchaseUpdateOrderStatus_Service():


    def updateOrderStatus(self, productId, status):

        try:
            data['productId'] = productId
            data['status'] = status

            results = json.loads(Run_http.post(url, data, get_headers()))

            if results['message'] == 'success':
                return results
            else:
                print('接口错误，错误原因：',results["message"])

        except Exception as e:
            print('后台采购修改订单状态接口失败:',e)





if __name__ == '__main__':

    # get_tokenV3("www")
    get_tokenV3("op")

