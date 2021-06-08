#!/usr/bin/env python
# -*- coding: utf-8 -*
# /**生成业务数据**/
from com.panli.op.service.Finance_SendCoupon_Service import FinanceSendCoupon_Service
from com.panli.op.service.Purchase_UpdateOrderStatus_Service import PurchaseUpdateOrderStatus_Service
from com.panli.op.service.Purchase_UpdateReceiver_Service import PurchaseUpdateReceiver_Service
from com.panli.op.service.Quality_SelfbuyReceivedUpdate_Service import QualitySelfbuyReceivedUpdate_Service
from com.panli.op.service.Warehouse_Register_Service import WarehouseRegister_Service
from com.panli.op.service.Warehouse_Registerlocation_Service import WarehouseRegisterlocation_Service
from com.panli.www.service.Coupon_GetList_Service import CouponGetList_Service
from com.panli.www.service.Order_GenerateOrderAndPay_Service import OrderGenerateOrderAndPay_Service
from com.panli.www.service.Order_GeneratePreOrderId_Service import OrderGeneratePreOrderId_Service
from com.panli.www.service.Order_GetList_Service import OrderGetList_Service
from com.panli.www.service.Order_PreorderModeify_Service import OrderPreorderModeify_Service
from com.panli.www.service.Pitem_GetProduct_Service import PitemGetProduct_Service
from com.panli.www.service.Shoppingcart_AddtoCart_Service import ShoppingcartAddtoCart_Service
from com.panli.www.service.Shoppingcart_GetList_Service import ShoppingcartGetList_Service
from config.testdata_properties import *
from common.get_token import *



class DataFactory():

    ########### 快速生成订单数据方法（使用优惠券）###########
    # 下单用户使用testdata_properties中配置用户
    def generatePurchaseOrder(self):
        # ---------------- 生成后台token ----------------
        get_tokenV3("op");

        # 发放优惠券
        usernamelist = [www_username];
        FinanceSendCoupon_Service().sendCoupon(usernamelist, order_CouponCode);

        # ---------------- 生成前台token ----------------
        get_tokenV3("www");

        # 获取商详
        ##----- productinfo['productId']\['skuId']\['title']\['linkUrl']\['skuprice']\['freightPrice']
        productinfo = PitemGetProduct_Service().getProductToBuy(shopping_ProductUrl);

        # 加入购物车
        ShoppingcartAddtoCart_Service().addtoCart(productinfo['productId'], productinfo['skuId'], productinfo['skuprice'],
                                        productinfo['title'], productinfo['linkUrl'], 2);  # 购买2个商品

        # 获取购物车列表
        ##----- cartinfo['cartId']\['totalAmount']
        cartinfo = ShoppingcartGetList_Service().getListToBuy();

        # 生成预订单
        ##----- ['preOrderId']
        preOrderId = OrderGeneratePreOrderId_Service().generatePreOrderIdToBuy(cartinfo['cartId']);

        # 获取优惠券列表计算需要支付费用
        ##----- couponinfo['couponCode']\['payAmount']
        couponinfo = CouponGetList_Service().getCouponNeedPayAmount(cartinfo['totalAmount']);

        # 生成预支付订单
        responseOPM = OrderPreorderModeify_Service().preorderModeify(preOrderId, couponinfo['couponCode'],
                                                           couponinfo['payAmount']);

        # 支付并生成正式订单
        responseOGO = OrderGenerateOrderAndPay_Service().generateOrderAndPay(preOrderId, couponinfo['couponCode'],
                                                                   www_paypassword);


    ########### 代购订单入库 ###########
    #
    def purchaseOrderWarehousing(self,productid,forbiddenInfo):
        """
        # 代购订单入库
        :param productid: 商品id（nproid）
        :param forbiddenInfo: 敏感品类型forbiddenInfo = [2, 3]
        :return:
        """

        # 获取后台登录token
        get_tokenV3("op")

        # 更换接单人(重试20次)
        attempts = 0
        success = False
        while attempts < 20 and not success:
            results = PurchaseUpdateReceiver_Service().updateReceiver(productid, '圆脸小猪')
            if results['message'] == 'success':
                success = True
            else:
                attempts += 1

        # 修改为已接单
        PurchaseUpdateOrderStatus_Service().updateOrderStatus(productid, '15')

        # 质检已到货
        QualitySelfbuyReceivedUpdate_Service().selfbuyReceivedUpdateForSensitive(productid, forbiddenInfo);

        # 仓管已到货处理
        WarehouseRegister_Service().warehouseregisterForId(productid, productid)

        # 仓管已入库处理
        WarehouseRegisterlocation_Service().registerlocationForId(productid, productid)



    ########### 从下单到入库完成流程 ###########
    # 默认敏感品食品药品，重抛
    def createPurchaseOrder(self):
        """
        # 从下单到入库完成流程
        :return: 商品id（nproid）
        """
        # 代购商品自动下单
        self.generatePurchaseOrder();

        # 获取第一个订单号
        get_tokenV3("www")
        productid = OrderGetList_Service().getFirstProductId(-1);
        print(productid)

        # 敏感品类型
        forbiddenInfo = [2, 3]
        # 代购商品自动入库
        self.purchaseOrderWarehousing(productid,forbiddenInfo)

        return productid









if __name__ == '__main__':

    # # 新建订单
    DataFactory().createPurchaseOrder();



