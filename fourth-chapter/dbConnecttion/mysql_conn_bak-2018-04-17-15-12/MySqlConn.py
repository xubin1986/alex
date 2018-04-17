#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author: chenshifei
# date: 2018-04-07
# discribe: mysql connection pool
import pymysql,os,configparser
from pymysql.cursors import DictCursor
from DBUtils.PooledDB import PooledDB

class MyPymysqlPool():
    #数据库对象，产生数据库连接，此类中的连接采用连接池实现获取连接对象，例如conn= Mysql.getConn()
    # 连接池对象,类属性，已经在类中定义好了的，所有对象使用同一个
    _pool = None
    def __init__(self,host,port,user,password,db_name=None,mincached=1,maxcached=20,*args,**kwargs):

        """
        :param host:
        :param port:
        :param user:
        :param password:
        :param db_name:
        :param mincached: initial number of idle connections in the pool(0 means no connections are made at startup)
        :param maxcached: maximum number of idle connections in the pool(0 or None means unlimited pool size)
        :param args:
        :param kwargs:
        """
        self._db_host = host
        #port必须为int，这里不强制转换
        self._db_port = port
        self._user = user
        self._password = str(password)
        self._db = db_name
        self._conn = None
        self._cursor = None
        self.mincached=mincached
        self.maxcached=maxcached
        self._args, self._kwargs = args, kwargs
        #接下来先准备好获取连接的函数，以便调用，见下面__getConn
        #获得数据库对象的连接池
        self._conn=self.__getConn()
        #通过连接池获取游标
        self._cursor=self._conn.cursor()

    def __getConn(self):
        """
        :summary:摘要，静态方法，从连接池中取出连接
        :return: MySQLdb.connection(PooledDB().connection)
        """
        #判断是否已经存在一个连接池，已经存在就不创建,不存在就使用PooledDB类初始化创建
        #PooledDB包含连接池参数请查看readme，也可以将其写入到配置文件中
        #PooledDB内有这个self.__args, self.__kwargs = args, kwargs，所以可以写入任意的字典参数
        if not MyPymysqlPool._pool:
            #创建一个连接池的数据库对象，可以设置连接池的参数
            _pool=PooledDB(creator=pymysql,
                            mincached=self.mincached,
                            maxcached=self.maxcached,
                            host=self._db_host,
                            port=self._db_port,
                            user=self._user,
                            passwd=self._password,
                            db=self._db,
                            use_unicode=False,
                            charset="utf8",
                            cursorclass=DictCursor,
                            *self._args,
                            **self._kwargs)
            #,setsession=['SET AUTOCOMMIT = 1']
            #返回一个数据库对象的连接池
            return _pool.connection()
        #以下方法供获取连接池后使用

    #简单执行语句，并返回行数，提取重复代码
    def __query(self,sql,param=None):
        if not param:
            count = self._cursor.execute(sql)
        else:
            count = self._cursor.execute(sql, param)
        return count

    #查询所有的结果
    def getAll(self,sql,param=None):
        """
        :summary:执行查询，并取出所有结果集
        :param sql: 查询sql语句,如果有查询条件，请指定条件列表，并将条件值使用参数param传递进来
        :param param: 可选参数，条件列表值(元组/列表)
        :return: result list/boolean查询到的结果集
        """
        #判断参数是否存在，按对应方式执行语句，返回影响条数

        # count=self.__query(sql,param)
        # if not param:
        #     count= self._cursor.execute(sql)
        # else:
        #     count = self._cursor.execute(sql, param)
        #判断影响条数是否大于0，如果大于0就会有返回，将所有返回的信息存入变量
        #否者结果为False
        # if count >0:
        #     result = self._cursor.fetchall()
        # else:
        #     result = False
        # #返回结果
        # return result
        return self._cursor.fetchall() if self.__query(sql,param) > 0 else False

    def getOne(self,sql,param=None):
        """
        :summary:执行查询，并取出第一条
        :param sql: 查询SQL，如果有查询条件，请指定条件列表，并将条件值使用参数param传递进来
        :param param: 可选参数，条件列表值(元组/列表)
        :return:  result list/boolean查询到的结果集
        """
        # count = self.__query(sql, param)
        # if not param:
        #     count = self._cursor.execute(sql)
        # else:
        #     count = self._cursor.execute(sql, param)

        # if count > 0 :
        #     result = self._cursor.fetchone()
        # else:
        #     result = False
        # return result

        return self._cursor.fetchone() if self.__query(sql, param) > 0 else False

    def getMany(self,sql,num,param=None):
        """
        :summary:执行查询，并取出num条结果
        :param sql: 查询SQL，如果有查询条件，请指定条件列表，并将条件值使用参数[param]传递进来
        :param num: 获取的结果条数
        :param param: 可选参数，条件列表值(元组/列表)
        :return: result list/boolean查询到的结果集
        """
        # count = self.__query(sql, param)
        return self._cursor.fetchmany(num) if self.__query(sql, param) > 0 else False

        # if not param:
        #     count = self._cursor.execute(sql)
        # else:
        #     count = self._cursor.execute(sql, param)
        # if count > 0 :
        #     result = self._cursor.fetchmany(num)
        # else:
        #     result = False
        # return result
    def insertMany(self,sql,values):
        """
        @summary:向数据表插入多条记录
        :param sql: 要插入的sql
        :param values: 要插入的记录数据tuple(tuple)/list[list]
        :return: count受影响的行数
        """
        # count = self._cursor.executemany(sql, values)
        # return count
        return self._cursor.executemany(sql,values)

    def update(self,sql,param=None):
        """
        @summary:更新数据表记录
        :param sql: sql格式及条件，使用(%s,%s)
        :param param: 要更新的值tuple/list
        :return: count受影响的行数
        """
        return self.__query(sql,param)
    def insert(self,sql,param=None):
        """
        @summary:插入数据表新记录
        :param sql: sql格式及条件，使用(%s,%s)
        :param param: 要更新的值，tuple/list
        :return: count 受影响的行数
        """
        return self.__query(sql,param)
    def delete(self,sql,param=None):
        """
        @summary:删除数据表记录
        :param sql: sql格式及条件，使用(%s,%s)
        :param param: 要删除的条件tuple/list
        :return: count 受影响的行数
        """
        #复用上面的函数query执行
        return self.__query(sql,param)
    def begin(self):
        """
        @summary:开启事务
        :return:
        """
        # dir(self._conn)
        # print("------")
        # self._conn.autocommit(0)
        pass
    def end(self,option='commit'):
        """
        :summary:结束事务
        :param option: 默认结束
        :return:
        """
        if option == 'commit':
            self._conn.commit()
        else:
            #回滚
            self._conn.rollback()
    def dispose(self,isEnd=1):
        """
        :summary:释放连接池资源
        :param isEnd: 默认释放
        :return:
        """
        if isEnd == 1:
            self.end('commit')
        else:
            self.end('rollback')
        #释放游标
        self._cursor.close()
        #释放数据库的连接池
        self._conn.close()
#测试代码
if __name__ == '__main__':
    #初始化一个连接池的数据库对象，即初始化会通过对象PooledDB返回一个连接池的conn对象
    mysql_obj=MyPymysqlPool(host='192.168.131.101',port=3306,user='root',password='Mysql_2018',db_name='test',mincached=0,maxcached=20)
    sqlAll = "select * from test;"
    result = mysql_obj.getAll(sqlAll)
    print(result)
    # mysql_obj.begin()
    mysql_obj.insert("insert into test.test set value=13")
    #调用end()

    # mysql_obj.dispose()
    # print(mysql_obj)
    mysql_obj.insert("insert into test.test set value=14")
    mysql_obj.end()