import mysql_conn

if __name__ == '__main__':
    # 初始化一个连接池的数据库对象，即初始化会通过对象PooledDB返回一个连接池的conn对象
    mysql_obj = mysql_conn.MysqlConnPool(host='192.168.131.101', port=3306, user='root', password='Mysql_2018', db_name='test',
                              mincached=0, maxcached=20)

    # mysql_obj.dispose()
    # print(mysql_obj)
    sqlAll = "select * from test;"
    mysql_obj.end()
    print(mysql_obj)

    # 单条插入，不带参数的
    mysql_obj.insert("insert into test.test set value=14")
    # 使用带参数的函数插入单个字段，参数为元组和列表都可以
    mysql_obj.insertMany("insert into test.test (value) values (%s)", [22, 33, 44, 55, 66])
    # 使用带参数的函数插入多个字段
    # mysql_obj.insertMany("insert into test.test (id,value) values (%s,%s)", ((400,200),(401,201),(402,202)))
    # 使用的参数也可以采用列表
    # mysql_obj.insertMany("insert into test.test (id,value) values (%s,%s)", [(400,200),(401,201),(402,202)])
    # 更正操作update不带参数
    mysql_obj.update("update test.test set value = 999 where id = 402")
    # 更正操作update带参数,%s有几个都可以加入到元组里面
    mysql_obj.update("update test.test set value = %s", (888))
    # 删除操作
    mysql_obj.delete("delete from test.test where id = 435")
    # 提交更新操作
    mysql_obj.end()
    # 获取所有结果
    result = mysql_obj.getAll(sqlAll)
    # 获取首行结果
    # result = mysql_obj.getOne(sqlAll)
    print(result)
