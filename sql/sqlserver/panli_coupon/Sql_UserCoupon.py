#!/usr/bin/env python
# -*- coding: utf-8 -*
from common.DbHandle import DbHandle


class Sql_UserCoupon():

    # 查询用户优惠券信息
    # coupontype = 1 订单优惠券； coupontype = 2 运单优惠券；
    def getUserCouponInfo(self, coupontype, username):

        dbHandle = DbHandle()
        sql = "SELECT uc.*, cp.name, cp.amount " \
              "FROM panlicoupon..UserCoupon AS uc " \
              "LEFT JOIN panlicoupon..[rule] AS r ON uc.CouponCode=r.CouponCode " \
              "LEFT JOIN panlicoupon..coupon AS cp ON uc.CouponCode=cp.CouponCode " \
              "WHERE uc.isused=0 AND r.DeleteFlag=0 AND cp.IsEnable=1 AND cp.DeleteFlag=0 AND getdate()> uc.begintime AND getdate()<=uc.EndTime " \
              "AND couponType='{0}' " \
              "AND uc.userId=(SELECT userid FROM panli..aspnet_UsersInfo WHERE username='{1}') ORDER BY uc.id DESC;"

        data = dbHandle.dbQuery('sqlserver', sql, coupontype, username)
        return data



if __name__ == '__main__':

    sql = Sql_UserCoupon();
    row = sql.getUserCouponInfo(1,'20210302001')
    print(row)

