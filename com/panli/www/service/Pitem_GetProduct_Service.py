#!/usr/bin/env python
# -*- coding: utf-8 -*-

from config import configHttp
import json



# ---- 前台抓取商品接口 ---- 



# 实例化对象
# readConfig = readConfig.ReadConfig()
Run_http = configHttp.Run_http()

# 定义header头
headers = {
    'content-type': 'application/json',
}

url = "http://www.panli.com/pitem/napi/GetProduct/?key="



class PitemGetProduct_Service():

    def getProduct(self, producturl):
        try:
            url_pitem = url + producturl;

            results = json.loads(Run_http.get(url_pitem, '', headers))

            product_data = results["Data"]

            if results["SubCode"] == 200:
                return product_data
            else:
                print('接口错误，错误原因：',results["Msg"])

        except Exception as e:
            print('抓取商品调用接口失败:',e)



    # 获取第一个sku的购买信息（用户添加购物车使用）
    def getProductToBuy(self, producturl):

        product_data = self.getProduct(producturl)

        productinfo = {}
        productinfo['productId'] = product_data['Id']
        productinfo['skuId'] = product_data['Skus'][0]['SkuId']
        productinfo['title'] = product_data['Title']
        productinfo['linkUrl'] = product_data['LinkUrl']
        productinfo['skuprice'] = product_data['Skus'][0]['Price']
        productinfo['freightPrice'] = product_data['FreightInfo'][0]['Price']

        return productinfo




if __name__ == '__main__':


    url_pitem =  "http://www.yugyg.com/goods/spu/1945";

    pitemGetProduct = PitemGetProduct_Service()
    aa = pitemGetProduct.getProductToBuy(url_pitem);
    print(aa)

