#!/usr/bin/env python
# -*- coding: utf-8 -*-

from common.get_token import *
import json




# 实例化对象
Run_http = configHttp.Run_http()

url = "http://www.panli.com/shoppingcart/napi/coupon/GetList"



class CouponGetList_Service():

    # 获取优惠券列表
    def getList(self, totalAmount):

        params = {
            "Amount":totalAmount
        }

        try:
            results = json.loads(Run_http.get(url, params, get_headers()))
            return results
        except Exception as e:
            print('获取优惠券列表接口失败:',e)


    # 获取优惠券列表(返回UserCouponCode & needPayAmount)
    # needPayAmount = 计算扣除第一张可用优惠券金额后的需要支付订单的金额
    def getCouponNeedPayAmount(self,totalAmount):
        res = self.getList(totalAmount);
        couponAmount = res['Data']['CouponInfos'][0]['Amount']
        needPayAmount = totalAmount - couponAmount

        couponinfo = {}
        couponinfo['couponCode'] = res['Data']['CouponInfos'][0]['CouponCode']
        couponinfo['payAmount'] = needPayAmount

        return couponinfo



if __name__ == '__main__':


    get_tokenV3("www")
    # get_tokenV3("op")
    getList = CouponGetList_Service()
    res = getList.getList(0.1);
