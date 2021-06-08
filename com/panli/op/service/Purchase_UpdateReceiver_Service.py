#!/usr/bin/env python
# -*- coding: utf-8 -*-

from common.get_token import *
import json



# 实例化对象
# readConfig = readConfig.ReadConfig()
Run_http = configHttp.Run_http()

url = "http://op.panli.com/api/purchase/UpdateReceiver"


data = {
    "productId": "OrderId",
    "acceptUserName": "圆脸小猪"
}


class PurchaseUpdateReceiver_Service():


    def updateReceiver(self, productId, acceptUserName):

        try:
            data['productId'] = productId
            data['acceptUserName'] = acceptUserName

            results = json.loads(Run_http.post(url, data, get_headers()))

            if results['message'] == 'success':
                return results;
            else:
                print('接口错误，错误原因：',results["message"]);
                return results;

        except Exception as e:
            print('后台更换接单人接口失败:',e);



if __name__ == '__main__':

    # get_tokenV3("www")
    get_tokenV3("op")


    attempts = 0
    success = False
    while attempts < 3 and not success:

        results = PurchaseUpdateReceiver_Service().updateReceiver('6001301', '圆脸小猪')
        if results['message'] == 'success':
            success = True
        else:
            attempts += 1

        # if attempts == 3:
        #     break