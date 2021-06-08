#!/usr/bin/env python
# -*- coding: utf-8 -*
from common.DbHandle import DbHandle


class MySql_order_discount():

    # 根据订单号获取优惠券信息
    def getorderdiscount(self,product_id):

        dbHandle = DbHandle()
        sql = "select * from panli_order.order_discount where product_id = '{0}';"
        data = dbHandle.dbQuery('mysql', sql, product_id)
        return data



if __name__ == '__main__':

    sql = MySql_order_discount();
    row = sql.getorderdiscount(6001901)
    row2 = sql.getorderdiscount(6001901)
    print(row)
