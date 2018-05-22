import socket
# 1、买手机
phone=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# 2、拨号，客户端只有一个套接字对象，phone
phone.connect(('127.0.0.1',8080))
# 3、发售消息
while True:
    mydata=input("输入发送的信息：").strip()
    if not len(mydata):
        continue
    if mydata=="exit":
        break
    # send将应用内存中的数据发给操作系统的内存；
    phone.send(mydata.encode('utf-8'))
    # 操作系统参照TCP / IP协议，调用网卡，发送数据包，操作系统发现为空就不会发送
    data=phone.recv(1024)
    print(data.decode())
# 4、挂电话
phone.close()