#!/usr/bin/env python
# -*- coding: utf-8 -*
from common.DataContrast import DataContrast
from common.DbHandle import DbHandle


class Sql_aspnet_UsersInfo():

    # 根据用户名获取用户信息
    def getuserinfo(self,username):

        dbHandle = DbHandle()
        # sql = "select userid from panli.dbo.aspnet_UsersInfo where username = 'happycaoyan';"
        sql = "select * from panli.dbo.aspnet_UsersInfo where username = '{0}';"
        data = dbHandle.dbQuery('sqlserver', sql, username)
        return data


    # 根据用户获取userid
    def getuserid(self,username):
        res = self.getuserinfo(username);
        return res[0]['UserId']


if __name__ == '__main__':

    sql = Sql_aspnet_UsersInfo();
    row = sql.getuserinfo('happycaoyan')
    row2 = sql.getuserinfo('cc123.')
    print(row)
    aa = DataContrast().contrastjson(row, row2)
    print(aa)

    # dbHandle = DbHandle()
    # sql = "select * from panli.dbo.aspnet_UsersInfo where username = '{0}' and nLevel = '{1}';"
    # data = dbHandle.dbQuery('sqlserver', sql, "happycaoyan", "11")
    # print(data)