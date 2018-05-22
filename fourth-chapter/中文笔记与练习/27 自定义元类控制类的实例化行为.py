#__call__方法
'''
内建方法，每个类中必然存在这样的方法
因为类会被加上括号调用，当类被调用的时候就会执行__call__()方法进行实例化操作
__call__()方法分为三步执行
1.创建一个空的对象
2.调用__init__实例化一个对象
3.返回这个对象
'''
class Mymeta(type):
    def __init__(self,class_name,class_bases,class_dic):
        #自己控制类的创建行为
        if not class_name.istitle():
            raise TypeError("类名称首字母必须为大写")
        if '__doc__' not in class_dic or not class_dic['__doc__'].strip():
            raise TypeError("类必须要有注释，且注释不能为空")
        #继承父类type的初始化行为，三个基本的类名称，基类，类的名字空间
        super(Mymeta,self).__init__(class_name,class_bases,class_dic)
    #模拟元类，覆盖type类的__call__方法，制作创建对象的方法
    def __call__(self, *args, **kwargs):
        obj=object.__new__(self) #实例化Chinese为一个空对象
        self.__init__(obj,*args, **kwargs)#初始化为obj对象
        print(obj)
        return obj #返回obj



class Chinese(metaclass=Mymeta):
    '''我是注释'''
    country='china'
    # print(__doc__)
    def __init__(self,name,age):
        self._name=name
        self._age=age
    def talk(self):
        print("%s is talk" %self._name)
    def __call__(self, *args, **kwargs):
        print("我是Chinese的对象，已经被调用，所以我相当于也是一个类")
        print("那么Chinese能够被调用，必然造出Chinese这个类的类也包含这个方法，即type或者Mymeta默认包含__call__")

obj=Chinese('alex',22)
hehe=obj()