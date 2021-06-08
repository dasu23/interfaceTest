#!/usr/bin/env python
# -*- coding: utf-8 -*-

from config.testdata_properties import www_username as user
from config.testdata_properties import *
from common.get_token import *
import json



# 实例化对象
# readConfig = readConfig.ReadConfig()
Run_http = configHttp.Run_http()

url = "http://op.panli.com/api/page/SendCoupon"


data = {
    "UserNames": [],
    "CouponCode": "BillCouponCode"
}


class FinanceSendCoupon_Service():

    def sendCoupon(self, usernamelist, couponCode):

        try:
            data['UserNames'] = usernamelist
            data['CouponCode'] = couponCode

            results = json.loads(Run_http.post(url, data, get_headers()))

            if results["Data"]['SendHappening']["IsSuccess"]== True:
                return results
            else:
                print('接口错误，错误原因：',results["Msg"])

        except Exception as e:
            print('后台发送优惠券接口失败:',e)



    def sendCouponOne(self, coupontype):

        usernamelist = [user];
        if coupontype == 'bill':

            res = self.sendCoupon(usernamelist, bill_CouponCode)
            return res
        else:
            res = self.sendCoupon(usernamelist, order_CouponCode)
            return res


if __name__ == '__main__':

    # get_tokenV3("www")
    get_tokenV3("op")

    usernamelist = ['happycaoyan','20210302001']

    financeSendCoupon = FinanceSendCoupon_Service();
    res = financeSendCoupon.sendCoupon(usernamelist, order_CouponCode)
    print(res)