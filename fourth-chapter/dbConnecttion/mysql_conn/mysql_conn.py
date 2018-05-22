#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author: chenshifei
# date: 2018-04-07
# discribe: mysql connection pool
# needed: pymysql,DBUtils
# installed: pip3 install pymysql,pip3 install DBUtils
import pymysql,os
from pymysql.cursors import DictCursor
from DBUtils.PooledDB import PooledDB
#MyPymysqlPool 基于pymysql模块和DButils的PooledDB
class Mymeta(type):
    def __init__(self, class_name, class_bases, class_dic):
        super(Mymeta, self).__init__(class_name, class_bases, class_dic)
        self.__instance=None
    def __call__(self, *args, **kwargs):
        if not self.__instance:
            #1.创建一个空对象
            self.__instance=object.__new__(self)
            #2.实例化对象
            self.__init__(self.__instance,*args,**kwargs)
        #3.返回一个对象
        return self.__instance

class MysqlConnPool():
    _pool = None #连接池对象,类数据属性，已经在类中定义好了的，所有对象使用同一个
    def __init__(self,host,port,user,password,db_name=None,mincached=1,maxcached=20,*args,**kwargs):

        """
        :param host:数据库地址
        :param port:数据库端口
        :param user:数据库用户
        :param password:数据库密码
        :param db_name:数据库名称
        :param mincached: initial number of idle connections in the pool(0 means no connections are made at startup)
        :param maxcached: maximum number of idle connections in the pool(0 or None means unlimited pool size)
        :param args:
        :param kwargs:
        """
        self._db_host = host
        self._db_port = port #port必须为int，这里不强制转换
        self._user = user
        self._password = str(password)
        self._db = db_name
        self._conn = None
        self._cursor = None
        self._mincached=mincached
        self._maxcached=maxcached
        self._args, self._kwargs = args, kwargs
        self._conn=self.__getConn() # #获得数据库对象的连接池，见下面__getConn，获取连接池的函数
        self._cursor=self._conn.cursor() #通过连接池对象获取游标

    def __getConn(self):
        """
        :summary: 静态方法，从连接池中取出连接
        :return:  MySQLdb.connection(PooledDB().connection)
        """
        if not MysqlConnPool._pool: #判断是否已经存在连接池，不存在就使用PooledDB类初始化创建
            _pool=PooledDB(creator=pymysql,
                            mincached=self._mincached,
                            maxcached=self._maxcached,
                            host=self._db_host,
                            port=self._db_port,
                            user=self._user,
                            passwd=self._password,
                            db=self._db,
                            use_unicode=False,
                            charset="utf8",
                            cursorclass=DictCursor,
                            setsession=None,
                            *self._args,
                            **self._kwargs,
                            ) #创建一个连接池的数据库对象，可以设置连接池的参数
            #setsession=['SET AUTOCOMMIT = 1'] 表示更新自动提交事务，而不用每次都去commit一下
            return _pool.connection()#返回一个数据库对象的连接池

    #以下方法供获取连接池后使用

    def __query(self,sql,param=None): #根据param参数是否为空选择执行语句，并返回影响行数，重复代码
        return self._cursor.execute(sql) if not param else self._cursor.execute(sql, param)

    def getAll(self,sql,param=None): #查询所有的结果
        """
        :summary:执行查询，并取出所有结果集
        :param sql: 查询sql语句,如果有查询条件，请指定条件列表，并将条件值使用参数param传递进来
        :param param: 可选参数，条件列表值(元组/列表)
        :return: result list/boolean查询到的结果集
        """
        return self._cursor.fetchall() if self.__query(sql,param) > 0 else False

    def getOne(self,sql,param=None):
        """
        :summary:执行查询，并取出第一条
        :param sql: 查询SQL，如果有查询条件，请指定条件列表，并将条件值使用参数param传递进来
        :param param: 可选参数，条件列表值(元组/列表)
        :return:  result list/boolean查询到的结果集
        """
        return self._cursor.fetchone() if self.__query(sql, param) > 0 else False

    def getMany(self,sql,num,param=None):
        """
        :summary:执行查询，并取出num条结果
        :param sql: 查询SQL，如果有查询条件，请指定条件列表，并将条件值使用参数[param]传递进来
        :param num: 获取的结果条数
        :param param: 可选参数，条件列表值(元组/列表)
        :return: result list/boolean查询到的结果集
        """
        return self._cursor.fetchmany(num) if self.__query(sql, param) > 0 else False
    def insertMany(self,sql,values): # 执行单条sql语句, 但是重复执行参数列表里的参数
        """
        :summary:向数据表插入多条记录
        :param sql: 要插入的sql
        :param values: 要插入的记录数据tuple(tuple)/list[list]
        :return: count受影响的行数
        """
        return self._cursor.executemany(sql,values)
    def update(self,sql,param=None):
        """
        :summary:更新数据表记录
        :param sql: sql格式及条件，使用(%s,%s)
        :param param: 要更新的值tuple/list
        :return: count受影响的行数
        """
        return self.__query(sql,param)
    def insert(self,sql,param=None):
        """
        :summary:插入数据表新记录
        :param sql: sql格式及条件，使用(%s,%s)
        :param param: 要更新的值，tuple/list
        :return: count 受影响的行数
        """
        return self.__query(sql,param)
    def delete(self,sql,param=None):
        """
        :summary:删除数据表记录
        :param sql: sql格式及条件，使用(%s,%s)
        :param param: 要删除的条件tuple/list
        :return: count 受影响的行数
        """
        return self.__query(sql,param)

    #关于事务或者释放连接池
    def begin(self):
        """
        :summary:开启事务,这条函数待验证是否存在，autocommit在初始化时候指定
        :return:
        """
        self._conn.autocommit(0)
    def end(self,option='commit'):
        """
        :summary:结束事务
        :param option: 默认结束
        :return:
        """
        if option == 'commit':
            self._conn.commit()
        else:
            self._conn.rollback()#回滚
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
        self._cursor.close() #释放游标
        self._conn.close() #释放数据库的连接池
#测试代码
if __name__ == '__main__':
    #初始化一个连接池的数据库对象，即初始化会通过对象PooledDB返回一个连接池的conn对象
    mysql_obj=MysqlConnPool(host='192.168.131.101', port=3306, user='root', password='Mysql_2018', db_name='test', mincached=0, maxcached=20)

    # mysql_obj.dispose()
    # print(mysql_obj)
    sqlAll = "select * from test.test;"
    mysql_obj.end()
    # print(mysql_obj)
    import time,hashlib,random

    #单条插入，不带参数的
    num=random.randrange(0,10000)
    num = 400
    data=[]
    for i in range(0,num):
        data.append(hashlib.md5(str(time.time()+random.randrange(0,100)).encode("utf-8")).hexdigest())
    old_time = time.time()
    # mysql_obj.insert("insert into test.test set value=(%s)",data)
    #使用带参数的函数插入单个字段，参数为元组和列表都可以
    mysql_obj.insertMany("insert into test.test (value) values (%s)",data)
    #使用带参数的函数插入多个字段
    # mysql_obj.insertMany("insert into test.test (id,value) values (%s,%s)", ((400,200),(401,201),(402,202)))
    #使用的参数也可以采用列表
    # mysql_obj.insertMany("insert into test.test (id,value) values (%s,%s)", [(400,200),(401,201),(402,202)])
    #更正操作update不带参数
    # mysql_obj.update("update test.test set value = 999 where id = 402")
    #更正操作update带参数,%s有几个都可以加入到元组里面
    # mysql_obj.update("update test.test set value = %s",(888))
    #删除操作
    # mysql_obj.delete("delete from test.test where id = 435")
    #提交更新操作
    mysql_obj.end()
    new_time=time.time()
    print("%ss" %(new_time-old_time))
    #获取所有结果
    # result = mysql_obj.getAll(sqlAll)
    #获取首行结果
    # result = mysql_obj.getOne(sqlAll)
    # print(result)