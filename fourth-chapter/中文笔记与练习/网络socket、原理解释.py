import socket
# 1.手机硬件,ipv4,tcp流
print("1.购买手机")
phone=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

# 2、手机卡绑定,手机卡是元组哈
print("2.电话卡绑定")
phone.bind(('127.0.0.1',8080))

# 3、开机
print("3.开机使用")
phone.listen()

# 4、等待电话
print("4.等待电话连接")
conn,addr=phone.accept()
print("打印套接字对象conn",type(conn))
print("打印地址的元组，电话号码addr",type(addr))

# 5、收发消息
while True:
    try:
        print("5.收发消息>>")
        # 应用程序请求操作系统将数据包拷贝到应用内存
        data=conn.recv(1024)
        #正常是不可能收到空的，除非客户端单方面断开连接，或者产生异常，以下适用于linux
        if not data:
            break
        print("收到的消息为：",data.decode())
        #send将应用内存中的数据发给操作系统的内存
        conn.send(data.upper())
    except ConnectionResetError: #适用于windows
        break
# 6、挂电话
print("6.挂电话")
conn.close()
phone.close()

