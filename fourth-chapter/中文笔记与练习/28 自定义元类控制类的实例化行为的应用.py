#1.单例模式，实现对象实例化只有一个
'''
class Mysql:
    __instance=None
    def __init__(self,host='127.0.0.1',port='3306'):
        self.host=host
        self.port=port

    @classmethod
    def sington(cls,*args,**kwargs):
        if not cls.__instance:
            cls.__instance=cls(*args,**kwargs)
        return cls.__instance
obj1=Mysql.sington()
obj2=Mysql.sington()

print(obj1 is obj2)

'''

#2.元类实现单例模式

class Mymeta(type):
    def __init__(self,class_name,class_bases,class_dic):
        self.__instance=None
        super(Mymeta,self).__init__(class_name,class_bases,class_dic)
    def __call__(self, *args, **kwargs):
        if not self.__instance:
            #1.创建一个空的对象,将self=Mysql传入,用Mysql的对象名称obj
            self.__instance=object.__new__(self)
            #2.初始化,调用Mysql类的__init__()初始化，传入obj对象本身使用Mysql类的初始化方法初始化
            self.__init__(self.__instance,*args,**kwargs)
        #返回
        return self.__instance
class Mysql(metaclass=Mymeta):
    def __init__(self,host='127.0.0.1',port='3306'):
        self.host=host
        self.port=port
obj1=Mysql()
obj2=Mysql()
print(obj1 is obj2)