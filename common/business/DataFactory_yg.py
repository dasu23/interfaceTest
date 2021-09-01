#!/usr/bin/env python
# -*- coding: utf-8 -*
# /**生成业务数据**/
from com.yugyg.api.shopkeeper.Shop_After_Sale_Refund_Apply_Service import Shop_After_Sale_Refund_Apply_Service
from com.yugyg.api.shopkeeper.Shop_Goods_Query_Service import Shop_Goods_Query_Service
from com.yugyg.api.shopkeeper.Shop_Order_Created_Service import Shop_Order_Created_Service
from com.yugyg.api.shopkeeper.Shop_Order_Payment_Service import Shop_Order_Payment_Service
from com.yugyg.api.shopkeeper.Transaction_Flow_Info_Query_Service import Transaction_Flow_Info_Query_Service
from com.yugyg.api.shopkeeper.Transaction_Flow_Page_Query_Service import Transaction_Flow_Page_Query_Service
from common.business.OrderContrast import OrderContrast


orderContrast = OrderContrast();


class DataFactory_yg():

    # 创建支付收银台订单
    def shopOrderCreateandPayment(self,quantity):

        # 获取收银台商品skuid & 价格
        skuid, price = Shop_Goods_Query_Service().shopgoodsQuerySkuPrice()

        # 创建订单
        orderCode = Shop_Order_Created_Service().shopOrderCreated(skuid, quantity)

        # 支付订单
        Shop_Order_Payment_Service().shopOrderPayment(orderCode, price)

        return orderCode,price


    # 创建售后申请
    def shopOrderRefund(self, orderCode, amount):

        transactionid = Transaction_Flow_Page_Query_Service().getTransactionId(1)

        orderGoodsId = Transaction_Flow_Info_Query_Service().getOrderGoodsId(transactionid)

        Shop_After_Sale_Refund_Apply_Service().transactionflowpageQuery(amount,orderCode,1,orderGoodsId)

        businessCode = Transaction_Flow_Page_Query_Service().getRefundbusinessCode()

        return businessCode











if __name__ == '__main__':


    aa = DataFactory_yg();

    orderCode,price = aa.shopOrderCreateandPayment(1)
    refundtransactionid = aa.shopOrderRefund(orderCode, price)
    print(orderCode)
    print(refundtransactionid)
