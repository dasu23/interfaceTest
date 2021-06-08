#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest

from com.panli.op.service.Finance_SendCoupon_Service import FinanceSendCoupon_Service
from common.TestRunner import TestRunner
from common.get_token import *
from com.panli.www.service.Coupon_GetList_Service import CouponGetList_Service
from common.DataContrast import DataContrast
from sql.sqlserver.panli_coupon.Sql_UserCoupon import Sql_UserCoupon


class Testcase_Coupon_GetList(unittest.TestCase):

    couponGetList_Service = CouponGetList_Service()

    def setUp(self):
        # global suite
        # suite = unittest.TestSuite()
        print("----------测试开始前准备----------")

    def tearDown(self):
        # test = TestRunner()
        # test.run(suite)
        print("----------测试结束，输出log完结----------\n\n")



    def testcase_Coupon_GetList_01(self):

        get_tokenV3("op")
        FinanceSendCoupon_Service().sendCouponOne("order")

        get_tokenV3("www")
        # 获取订单优惠券列表
        response = self.couponGetList_Service.getList(0.01)
        sql = Sql_UserCoupon().getUserCouponInfo(1,"20210302001")
        self.checkResult(sql[0], response)


    def testcase_Coupon_GetList_02(self):
        self.assertEqual(1,1)


    # 断言
    def checkResult(self, expectedJson, actualJson):

        jsonPathDict = {
            "name": "Data.CouponInfos[0].ActivityTitle",
            "amount": "Data.CouponInfos[0].Amount",
            "UserCouponCode": "Data.CouponInfos[0].CouponCode",
            "BeginTime": "Data.CouponInfos[0].ValidBeginTime",
            "EndTime": "Data.CouponInfos[0].ValidEndTime",
            "IsUsed": "Data.CouponInfos[0].IsUsed"
            # "BeginTime": "Data.CouponInfos[0].ValidEndTime",
            # "IsUsed2": "Data.CouponInfos[0].IsUsed"
        }

        DataContrast().contrastByJsonPathRaise(jsonPathDict, expectedJson, actualJson)



if __name__ == '__main__':
    # unittest.main();


    TestRunner().bfrun(Testcase_Coupon_GetList);