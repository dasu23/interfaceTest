import pymssql
import pymysql
from config.configDB import *
from config.configEnv import ConfigEnv


class DbHandle():

    def connectdb(self, database):
        try:

            configEnv = ConfigEnv()
            env = configEnv.getEnv()

            if env == 'sit' or env == 'Sit' or env == 'SIT':
                mysqlhost = mysql
                sqlserverhost = sqlserver
            else:
                mysqlhost = mysql_pro
                sqlserverhost = sqlserver_pro

            if database == 'mysql':
                self.conn = pymysql.connect(host=mysqlhost['host'],
                                            port=mysqlhost['port'],
                                            user=mysqlhost['user'],
                                            password=mysqlhost['password'],
                                            # database=mysqlhost['database'],
                                            charset=mysqlhost['charset'])
                self.cur = self.conn.cursor(cursor=pymysql.cursors.DictCursor)

            elif database == 'sqlserver':
                self.conn = pymssql.connect(host=sqlserverhost['host'],
                                            port=sqlserverhost['port'],
                                            user=sqlserverhost['user'],
                                            password=sqlserverhost['password'],
                                            # database=sqlserverhost['database'],
                                            charset=sqlserverhost['charset'])
                self.cur = self.conn.cursor(as_dict=True)
        except:
            print("连接数据库失败")


    def dbClose(self):
        if self.conn and self.cur:
            self.cur.close()
            self.conn.close()

    def dbQuery(self, database, sql, *args):
        try:
            sql = sql.format(*args)
            self.connectdb(database)
            self.cur.execute(sql)
            data = self.cur.fetchall()
            return data
        except Exception as e:
            print(e)
            print('查询失败！！！')

    def dbInsert(self, database, sql, *args):
        try:
            sql = sql.format(*args)
            self.connectdb(database)
            self.cur.execute(sql)
            print("插入成功！！！")
            self.conn.commit()
        except Exception as e:
            print(e)
            print('插入失败！！！')

    def dbUpdate(self, database, sql, *args):
        try:
            sql = sql.format(*args)
            self.connectdb(database)
            self.cur.execute(sql)
            print("更新sql成功！！！")
            self.conn.commit()
        except Exception as e:
            print(e)
            print('更新sql失败！！！')




if __name__ == '__main__':

    dbHandle = DbHandle()
    # sqlserver测试
    dbHandle.connectdb('sqlserver')
    sql = "select top 11 * from panliuser..userphone order by CreateTime desc;"
    data=dbHandle.dbQuery('sqlserver',sql)
    print(data)


    # mysql测试
    sql = "select * from panli_game.order_redpackage where buyer_id ='111111';"
    data=dbHandle.dbQuery('mysql',sql)
    print(data)
    print(data[0]["is_get"])


    ## 传入参数测试
    sql = "select * from panli.dbo.aspnet_UsersInfo where username = '{0}';"
    data = dbHandle.dbQuery('sqlserver', sql, 'happycaoyan')
    print(data)
    print(data[0]["UserId"])