#!/usr/bin/env python
# -*- coding: utf-8 -*
# /**生成业务数据**/
from com.fulu.app.Buyer_settle_trade_create_Service import Buyer_settle_trade_create_Service
from com.fulu.app.Buyer_voucher_create_Service import Buyer_voucher_create_Service
from common.business.get_token import *
from common.business.OrderContrast import OrderContrast


orderContrast = OrderContrast();


class DataFactory_fulu():

    # 创建支付收银台订单
    def create_buyer_order(self):
        orderCode = Buyer_settle_trade_create_Service().settle_trade_create();
        Buyer_voucher_create_Service().voucher_create(orderCode);





if __name__ == '__main__':

    get_tokenV3("fulu");
    aa = DataFactory_fulu();
    aa.create_buyer_order();
