#!/usr/bin/env python
# -*- coding: utf-8 -*-

from common.get_token import *
import json



# 实例化对象
# readConfig = readConfig.ReadConfig()
Run_http = configHttp.Run_http()

url = "http://op.panli.com/api/warehouse/cartproduct/register"


data = {
    "NProID": "5997401",
    "SzTagsID": "5997401",
    "NForbiddenType": 0,
    "NLightType": 0
}

class WarehouseRegister_Service():


    def warehouseregister(self, request):

        try:

            results = json.loads(Run_http.post(url, request, get_headers()))

            if results['Data']['IsSuccess'] == True:
                return results
            else:
                print('接口错误，错误原因：',results["Msg"])

        except Exception as e:
            print('后台仓管 - 已到商品管理 - 已到货保存接口失败:',e)




    def warehouseregisterForId(self, nProID, szTagsID):

        data['NProID'] = nProID
        data['SzTagsID'] = szTagsID
        res = self.warehouseregister(data)
        return res

if __name__ == '__main__':

    # get_tokenV3("www")
    get_tokenV3("op")

