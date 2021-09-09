#!/usr/bin/env python
# -*- coding: utf-8 -*
# /**生成业务数据**/
from com.panli.op.service.Finance_SendCoupon_Service import FinanceSendCoupon_Service
from com.panli.op.service.Purchase_UpdateOrderStatus_Service import PurchaseUpdateOrderStatus_Service
from com.panli.op.service.Purchase_UpdateReceiver_Service import PurchaseUpdateReceiver_Service
from com.panli.op.service.Quality_SelfbuyReceivedUpdate_Service import QualitySelfbuyReceivedUpdate_Service
from com.panli.op.service.Risk_UpdateUserVentureStatus_Service import Risk_UpdateUserVentureStatus_Service
from com.panli.op.service.Warehouse_Register_Service import WarehouseRegister_Service
from com.panli.op.service.Warehouse_Registerlocation_Service import WarehouseRegisterlocation_Service
from com.panli.op.service.Warehouse_ship_BatchChangeStatus_Service import Warehouse_ship_BatchChangeStatus_Service
from com.panli.op.service.Warehouse_ship_Update_Service import Warehouse_ship_Update_Service
from com.panli.www.service.Coupon_GetFreightList_Service import Coupon_GetFreightList_Service
from com.panli.www.service.Coupon_GetList_Service import CouponGetList_Service
from com.panli.www.service.Logistics_GetWaybillDeliveryList_Service import Logistics_GetWaybillDeliveryList_Service
from com.panli.www.service.My_ConfirmReceipt_Service import My_ConfirmReceipt_Service
from com.panli.www.service.My_GetAddressList_Service import My_GetAddressList_Service
from com.panli.www.service.Order_GenerateOrderAndPay_Service import OrderGenerateOrderAndPay_Service
from com.panli.www.service.Order_GeneratePreOrderId_Service import OrderGeneratePreOrderId_Service
from com.panli.www.service.Order_GetList_Service import OrderGetList_Service
from com.panli.www.service.Order_PayWaybill_Service import Order_PayWaybill_Service
from com.panli.www.service.Order_PreorderModeify_Service import OrderPreorderModeify_Service
from com.panli.www.service.Pitem_GetProduct_Service import PitemGetProduct_Service
from com.panli.www.service.Shoppingcart_AddtoCart_Service import ShoppingcartAddtoCart_Service
from com.panli.www.service.Shoppingcart_GetList_Service import ShoppingcartGetList_Service
from common.business.OrderContrast import OrderContrast
from common.business.ShipContrast import ShipContrast
from config.testdata_properties import *
from common.business.get_token import *

orderContrast = OrderContrast();

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
        responseOPM = OrderPreorderModeify_Service().preorderModeify(preOrderId, couponinfo['couponCode'], couponinfo['payAmount']);

        # 支付并生成正式订单
        responseOGO = OrderGenerateOrderAndPay_Service().generateOrderAndPay(preOrderId, couponinfo['couponCode'], www_paypassword);



    ########### 代购订单入库 ###########
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



    ###########----- 从下单到入库完成流程（有断言） ------###########
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
        # 下单后校验订单数据库
        orderContrast.checkmysqlOrder(productid);

        # 敏感品类型
        forbiddenInfo = [2, 3]
        # 代购商品自动入库
        self.purchaseOrderWarehousing(productid,forbiddenInfo)
        # 入库后校验订单数据库
        orderContrast.checkmysqlOrder(productid);

        return productid




    ########### 生成运单 ###########
    def generateBillOrder(self, productid):

        # ---------------- 生成后台token(发运费券) ----------------
        get_tokenV3("op");
        FinanceSendCoupon_Service().sendCoupon([www_username], bill_CouponCode)


        # ---------------- 生成前台token(创建运单)----------------
        get_tokenV3("www");
        addressId,addressInfo = My_GetAddressList_Service().returnAmericanAddress()

        billTotalAmount,billSolutionId,deliveryList = Logistics_GetWaybillDeliveryList_Service().getWaybillDeliveryList(addressId, productid)

        userBillCouponCode,couponinfo = Coupon_GetFreightList_Service().getUserBillCouponCode(billTotalAmount)

        billId,billinfo = Order_PayWaybill_Service().payWaybill(billSolutionId, userBillCouponCode, www_paypassword)

        # 断言
        ShipContrast().checkshipinfo(addressInfo, billinfo, couponinfo, deliveryList);

        # ---------------- 生成后台token(仓管发货) ----------------
        get_tokenV3("op");
        # 审核通过用户，防止用户被风控无法建运单
        Risk_UpdateUserVentureStatus_Service().updateUserVentureStatus(www_username)

        batchChangeStatus = Warehouse_ship_BatchChangeStatus_Service();
        # 设置运单为处理中
        batchChangeStatus.batchChangeStatus(11, [billId])
        # 设置运单为已接单
        batchChangeStatus.batchChangeStatus(1, [billId])

        ship_Update = Warehouse_ship_Update_Service();
        # 设置运单为发货中
        ship_Update.shipUpdate(billId, 2, 1000)
        # 设置运单为已发货
        ship_Update.shipUpdate(billId, 3, 1000)


        # ---------------- 生成前台token(用户确认收货) ----------------
        get_tokenV3("www");
        My_ConfirmReceipt_Service().confirmReceipt(billId)

        return billId





if __name__ == '__main__':

    dataFactory = DataFactory();
    # # 新建订单˙
    productid = dataFactory.createPurchaseOrder();

    billId = dataFactory.generateBillOrder(productid);




    # dataFactory.generatePurchaseOrder()
