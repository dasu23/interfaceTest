#!/usr/bin/env python
# -*- coding: utf-8 -*
from com.panli.www.service.Shoppingcart_GetList_Service import ShoppingcartGetList
from common.DataContrast import DataContrast
from common.DbHandle import DbHandle
from common.get_token import get_tokenV3


class MySql_order_product():

    # 根据订单号获取订单支付信息
    def getorderproduct(self,product_id):

        dbHandle = DbHandle()
        sql = "select * from panli_order.order_product where product_id = '{0}';"
        data = dbHandle.dbQuery('mysql', sql, product_id)
        return data


    def checkOrderProduct(self,pathdict, expectedJson,product_id):

        actualJson = self.getorderproduct(product_id);
        DataContrast().contrastByJsonPath(pathdict, expectedJson, actualJson[0]);



if __name__ == '__main__':

    get_tokenV3("www")

    sql = MySql_order_product();
    # row = sql.getorderproduct(6001901)
    # print(row)


    jsonpathdict = {
                    "Data.Shoppingcarts.Sellers[0].Products[0].Title": "product_name",
                    "Data.Shoppingcarts.Sellers[0].Products[0].SkuPropertiesText":"product_name"
                }

    getList = ShoppingcartGetList().getList()
    sql.checkOrderProduct(jsonpathdict,getList,6001901)
