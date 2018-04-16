class People:
    def __init__(self,name): #构造函数，对象实例化就会执行
        self.name=name
    def __getitem__(self, item): #通过类名[key]的方式查询就会执行此函数
        # print("name")
        return self.__dict__.get(item)
    def __setitem__(self, key, value): #通过类名[key]赋值操作就会执行此函数
        self.__dict__[key]=value
    def __delitem__(self, key): #删除类名[key]就会执行此函数
        print('delitem....')
        self.__dict__.pop(key)
    def __str__(self):    # 对象的描述，当打印对象时就会返回此提示
        return "class:----str"
    def __del__(self): #析构函数，对象释放后，执行。
        print('del finished')
p=People('alex')
p['name']='chen'
print(p['name'])
del p['name']
print(p['name'])
print(p)
print("------main-----end")


# f=open('setttings.py') #f是变量，操作系统打开一个文件，然后映射到磁盘，应用停止不主动关闭，操作系统不会自动关闭
# f.close() #需要主动close，发送信号给操作系统让其关闭文件。

