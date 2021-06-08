#!/usr/bin/env python
# -*- coding: utf-8 -*
from common.DataContrast import DataContrast
from common.DbHandle import DbHandle


class MySql_order_payment_record():

    # 根据订单号获取订单支付信息
    def getorderpaymentrecord(self,product_id):

        dbHandle = DbHandle()
        sql = "select * from panli_order.order_payment_record where order_product_id =  '{0}';"
        data = dbHandle.dbQuery('mysql', sql, product_id)
        return data



if __name__ == '__main__':

    sql = MySql_order_payment_record();
    row = sql.getorderpaymentrecord(6001901)

    print(row)