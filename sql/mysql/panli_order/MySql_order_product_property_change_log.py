#!/usr/bin/env python
# -*- coding: utf-8 -*
from common.DataContrast import DataContrast
from common.DbHandle import DbHandle


class MySql_order_product_property_change_log():

    # 根据订单号获取订单商品质管属性变更记录表
    def getorderproductpropertychangelog(self,product_id):

        dbHandle = DbHandle()
        sql = "select * from panli_order.order_product_property_change_log where order_product_id = '{0}';"
        data = dbHandle.dbQuery('mysql', sql, product_id)
        return data



if __name__ == '__main__':

    sql = MySql_order_product_property_change_log();
    row = sql.getorderproductpropertychangelog(6001901)

    print(row)