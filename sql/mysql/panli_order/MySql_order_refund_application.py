#!/usr/bin/env python
# -*- coding: utf-8 -*
from common.DataContrast import DataContrast
from common.DbHandle import DbHandle


class MySql_order_refund_application():

    # 根据订单号获取退款信息表
    def getOrderRefundApplication(self,product_id):

        dbHandle = DbHandle()
        sql = "select * from panli_order.order_refund_application where product_id = '{0}';"
        data = dbHandle.dbQuery('mysql', sql, product_id)
        return data



if __name__ == '__main__':

    sql = MySql_order_refund_application();
    row = sql.getOrderRefundApplication(6001901)

    print(row)