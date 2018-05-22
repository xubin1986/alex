#入参：连接数
#操作mysql数据库每次都需要连接、读写、关闭
#操作比较频繁会降低数据库的性能
#mysql连接池可以设置连接数的最大预留数目，一开始就将所有连接数准备好
#然后进行读写操作。
# 主要存在四种命名：
# 1.object #公共方法或变量
# 2.__object__ # 内建方法
# 3.__object #全私有,全保护,只有类对象自己能访问，连子类对象也不能访问到这个数据。
# 4._object #半保护,只有类对象和子类对象自己能访问到这些变量

# pip3 install DBUtils pymysql

import pymysql
import warnings
import queue
import logging
import threading

class Connection(pymysql.connections.Connection):
    __pool = None
    __reusable_exection = (pymysql.err.ProgrammingError,pymysql.err.IntegrityError,pymysql.err.NotSupportedError)
    def __init__(self,*args,**kwargs):
        # pymysql.connections.Connection.__init__()
        super(Connection,self).__init__(*args,**kwargs)
        self.args = args
        self.kwargs = kwargs
    def __exit__(self, exc_type, exc_val, exc_tb):
        super(Connection,self).__exit__(exc_type,exc_val,exc_tb)
        if self.__pool:
            if not exc_type or exc_type in self.__reusable_exection:
                self.__pool.put_connection(self)
            else:
                self.__pool.put_connection(self.__recreate())

# p=Connection()