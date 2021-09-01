from common.DataContrast import DataContrast
from sql.mysql.panli_order.MySql_order_discount import MySql_order_discount
from sql.mysql.panli_order.MySql_order_payment_record import MySql_order_payment_record
from sql.mysql.panli_order.MySql_order_product import MySql_order_product
from sql.mysql.panli_order.MySql_order_product_property import MySql_order_product_property
from sql.sqlserver.panli.Sql_CartProductDetail import Sql_CartProductDetail

dataContrast = DataContrast()


class OrderContrast():

    # 对比MySql_order_product
    def check_order_product(self, nproid):
        print("---对比MySql_order_product---")
        sqlOrderProduct = Sql_CartProductDetail().get_order_product(nproid)[0]
        mysqlOrderProduct = MySql_order_product().getorderproduct(nproid)[0]
        dataContrast.contrastbyexpected(sqlOrderProduct,mysqlOrderProduct)


    # 对比MySql_order_discount
    def check_order_discount(self, nproid):
        print("---对比MySql_order_discount---")
        sqlOrderProduct = Sql_CartProductDetail().get_order_discount(nproid)[0]
        mysqlOrderProduct = MySql_order_discount().getorderdiscount(nproid)[0]
        dataContrast.contrastbyexpected(sqlOrderProduct,mysqlOrderProduct)


    # 对比MySql_order_payment_record
    def check_order_payment_record(self, nproid):
        print("---对比MySql_order_payment_record---")
        sqlOrderProduct = Sql_CartProductDetail().get_order_payment_record(nproid)[0]
        mysqlOrderProduct = MySql_order_payment_record().getorderpaymentrecord(nproid)[0]
        dataContrast.contrastbyexpected(sqlOrderProduct,mysqlOrderProduct)


    #对比MySql_order_product_property
    def check_order_product_property(self, nproid):
        print("---对比MySql_order_product_property---")
        sqlOrderProduct = Sql_CartProductDetail().get_order_product_property(nproid)[0]
        mysqlOrderProduct = MySql_order_product_property().getorderproductproperty(nproid)[0]
        dataContrast.contrastbyexpected(sqlOrderProduct,mysqlOrderProduct)

    # 对比mysql订单4张表
    def checkmysqlOrder(self, nproid):
        self.check_order_product(nproid);
        self.check_order_discount(nproid);
        self.check_order_payment_record(nproid);
        self.check_order_product_property(nproid);



if __name__ == '__main__':
    OrderContrast().checkmysqlOrder(6019901);
