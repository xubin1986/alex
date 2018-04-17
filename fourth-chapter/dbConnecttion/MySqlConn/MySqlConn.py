#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author: chenshifei
# date: 2018-04-07
# discribe: mysql connection pool
import pymysql,os,configparser
from pymysql.cursors import DictCursor
from DBUtils.PooledDB import PooledDB

#获取配置文件中的信息的类，包含sections，options，content，可以返回一个字典，存放了配置选项
class Config(object):
    #Config_file='notdbMysql'
    def __init__(self, conf_name="mysql_conn_pool.cnf"):
        file_path = os.path.join(os.path.dirname(__file__), conf_name)
        self.cf = configparser.ConfigParser()
        self.cf.read(file_path)
    def get_sections(self):
        return self.cf.sections()
    def get_options(self,section):
        return self.cf.options(section)
    def get_content(self,section):
        result={}
        for option in self.get_options(section):
            value = self.cf.get(section,option)
            result[option] = int(value) if value.isdigit() else value
        return result
#连接池类的基类，初始化连接池需要的连接参数
class BasePymysqlPool(object):
    def __init__(self,host,port,user,password,db_name=None):
        self.db_host=host
        self.db_port=port
        self.user=user
        self.password=str(password)
        self.db = db_name
        self.conn = None
        self.cursor = None
#继承连接池基类
class MyPymysqlPool(BasePymysqlPool):
    #数据库对象，产生数据库连接，此类中的连接采用连接池实现获取连接对象，例如conn= Mysql.getConn()
    #连接池对象
    __pool = None
    #子类不写其他参数的原因，是因为不需要显示录入其他连接参数，直接从配置文件中获取
    def __init__(self,conf_name=None,section_name=None):
        #需要传递的参数为配置文件的名称，然后调用父类构造方法传递参数,这里获取到的是一个配置信息的字典
        self.conf=Config(conf_name).get_content(section_name)
        #将配置信息字典传入父类构造方法，实现初始化在内存的配置
        super(MyPymysqlPool,self).__init__(**self.conf)
        #接下来先准备好获取连接的函数，以便调用，见下面__getConn
        #获得数据库对象的连接池
        self._conn=self.__getConn()
        #通过连接池获取游标
        self._cursor=self._conn.cursor()
    def __getConn(self):
        """
        @summary:摘要，静态方法，从连接池中取出连接
        :return: MySQLdb.connection
        """
        #判断是否已经存在一个连接池，已经存在就不创建,不存在就使用PooledDB类初始化创建
        #PooledDB包含连接池参数请查看readme，也可以将其写入到配置文件中
        #PooledDB内有这个self._args, self._kwargs = args, kwargs，所以可以写入任意的字典参数
        if not MyPymysqlPool.__pool:
            #创建一个连接池的数据库对象，可以设置连接池的参数
            __pool=PooledDB(creator=pymysql,
                            mincached=1,
                            maxcached=20,
                            host=self.db_host,
                            port=self.db_port,
                            user=self.user,
                            passwd=self.password,
                            db=self.db,
                            use_unicode=False,
                            charset="utf8",
                            cursorclass=DictCursor)#,setsession=['SET AUTOCOMMIT = 1']
            #返回一个数据库对象的连接池
            return __pool.connection()
        #以下方法供获取连接池后使用

    #查询所有的结果
    def getAll(self,sql,param=None):
        """
        :summary:执行查询，并取出所有结果集
        :param sql: 查询sql语句,如果有查询条件，请指定条件列表，并将条件值使用参数param传递进来
        :param param: 可选参数，条件列表值(元组/列表)
        :return: result list/boolean查询到的结果集
        """
        #判断参数是否存在，按对应方式执行语句，返回影响条数
        if not param:
            count= self._cursor.execute(sql)
        else:
            count = self._cursor.execute(sql,param)
        #判断影响条数是否大于0，如果大于0就会有返回，将所有返回的信息存入变量
        #否者结果为False
        if count >0:
            result = self._cursor.fetchall()
        else:
            result = False
        #返回结果
        return result
    def getOne(self,sql,param=None):
        """
        :summary:执行查询，并取出第一条
        :param sql: 查询SQL，如果有查询条件，请指定条件列表，并将条件值使用参数param传递进来
        :param param: 可选参数，条件列表值(元组/列表)
        :return:  result list/boolean查询到的结果集
        """
        if not param:
            count = self._cursor.execute(sql)
        else:
            count = self._cursor.execute(sql,param)
        if count > 0 :
            result = self._cursor.fetchone()
        else:
            result = False
        return result

    def getMany(self,sql,num,param=None):
        """
        :summary:执行查询，并取出num条结果
        :param sql: 查询SQL，如果有查询条件，请指定条件列表，并将条件值使用参数[param]传递进来
        :param num: 获取的结果条数
        :param param: 可选参数，条件列表值(元组/列表)
        :return: result list/boolean查询到的结果集
        """
        if not param:
            count = self._cursor.execute(sql)
        else:
            count = self._cursor.execute(sql,param)
        if count > 0 :
            result = self._cursor.fetchmany(num)
        else:
            result = False
        return result
    def insertMany(self,sql,values):
        """
        @summary:向数据表插入多条记录
        :param sql: 要插入的sql
        :param values: 要插入的记录数据tuple(tuple)/list[list]
        :return: count受影响的行数
        """
        count = self._cursor.executemany(sql,values)
        return count
    #简单执行语句，并返回行数，去重代码
    def __query(self,sql,param=None):
        if not param:
            count = self._cursor.execute(sql)
        else:
            count = self._cursor.execute(sql,param)
        return count
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
        self._conn.autocommit(0)
    def end(self,option='commit'):
        """
        @summary:结束事务
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
        @summary:释放连接池资源
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
    #初始化一个连接池的数据库对象，即初始化会返回一个连接池PooledDB的conn
    # MysqlConnPool(conf_name,section_name) #传入配置文件名称和[section]名称
    mysql_obj=MyPymysqlPool('notdbMysql','notdbMysql')
    sqlAll = "select * from test;"
    result = mysql_obj.getAll(sqlAll)
    print(result)
    # mysql_obj.begin()
    mysql_obj.insert("insert into test.test set value=13")
    #调用end()

    # mysql_obj.dispose()
    # print(mysql_obj)
    mysql_obj.insert("insert into test.test set value=14")
