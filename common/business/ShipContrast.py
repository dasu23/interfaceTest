from decimal import Decimal

from com.panli.www.service.My_GetAddressList_Service import My_GetAddressList_Service
from common.DataContrast import DataContrast
from common.DataProcess import DataProcess
from common.business.get_token import get_tokenV3
from sql.mysql.panli_order.MySql_ship_order_basic import MySql_ship_order_basic

dataContrast = DataContrast()
dataProcess = DataProcess()


class ShipContrast():

    def getMember_Address_info(self, addressinfo):
        member_address_info = {}
        member_address_info['Address'] = addressinfo['address']

        if dataProcess.isempty(addressinfo['citycode']):
            member_address_info['City'] = addressinfo['provincename']
        else:
            city = addressinfo['provincename'] + "/" + addressinfo['cityname']
            member_address_info['City'] = city

        member_address_info['Consignee'] = addressinfo['consignee']
        member_address_info['ContactPhone'] = addressinfo['telephone']
        member_address_info['Country'] = addressinfo['countryname']
        member_address_info['ZipCode'] = addressinfo['zipcode']

        return member_address_info



    def checkshipinfo(self, addressinfo, billinfo, couponinfo, deliveryInfo):
        # 对比路径
        pathjson = {
                    "Billinfo.Data.WaybillIds[0]": "ship_id",
                    "Billinfo.Data.WaybillIds[0]": "ship_code",
                    "Addressinfo.addressid": "member_address_id",
                    "Addressinfo.member_address_info": "member_address_info",
                    "DeliveryInfo.Data.WaybillDeliveryInfos[0].WaybillDeliveryDetails[0].PackageWeight": "estimate_package_weight",
                    "DeliveryInfo.Data.WaybillDeliveryInfos[0].WaybillDeliveryDetails[0].UnitWeight": "total_product_weight",
                    "DeliveryInfo.Data.WaybillDeliveryInfos[0].WaybillDeliveryDetails[0].Name": "ship_delivery_name",
                    "Billinfo.request.Memo": "memo",
                    "DeliveryInfo.Data.WaybillDeliveryInfos[0].TotalProductsAmount": "total_product_amount",
                    "DeliveryInfo.Data.Products[0].ProductId": "product_id",
                    "DeliveryInfo.Data.Products[0].ProductType": "product_type",
                    "DeliveryInfo.Data.WaybillDeliveryInfos[0].CustodyAmount": "custody_amount",
                    "Couponinfo.CouponCode": "coupon_id",
                    "Couponinfo.Amount": "coupon_amount",
                    "DeliveryInfo.Data.WaybillDeliveryInfos[0].ShipAmountAfterDiscount": "real_ship_amount",
                    "DeliveryInfo.Data.WaybillDeliveryInfos[0].EntryAmount": "real_entry_amount"
                }

        # 期待结果
        member_address_info = self.getMember_Address_info(addressinfo)
        straddress = dataProcess.replacejson(member_address_info)
        addressinfo['member_address_info'] = straddress
        expectedJson = {}
        expectedJson['Addressinfo'] = addressinfo
        expectedJson['Billinfo'] = billinfo
        expectedJson['Couponinfo'] = couponinfo
        expectedJson['DeliveryInfo'] = deliveryInfo

        billid = billinfo['Data']['WaybillIds'][0]

        # 实际落地mysql结果
        actualJson = MySql_ship_order_basic().getshipdetail(billid)[0];
        actualJson['member_address_info'] = actualJson['member_address_info'].replace(" ","")

        # 对比断言
        dataContrast.contrastByJsonPath(pathjson, expectedJson, actualJson)






if __name__ == '__main__':

    aa = ShipContrast()

    # get_tokenV3("www")
    # get_tokenV3("op")
    # addressid,addressinfo = My_GetAddressList_Service().returnAmericanAddress()
    # bb = aa.getMember_Address_info(addressinfo)
    # print(bb)

    bb = MySql_ship_order_basic().getshipdetail("Y2021090600003")[0];
    cc = bb['real_ship_amount']








