#一切类都是对象，都基于一个元类来进行实例化
#可以手动模拟类的创建过程，通过exec翻译和元类的实例化来进行类的创建
#默认的元类是type,即默认类的类型是type类型。
#我们自己修改一个元类，必须继承自元类，在元类基础的基础上进行扩展修改功能，通过修改__init__构造方法，达到控制类的创建行为

class Mymeta(type):
    def __init__(self,class_name,class_bases,class_dic):
        #自己控制类的创建行为
        if not class_name.istitle():
            raise TypeError("类名称首字母必须为大写")
        if '__doc__' not in class_dic or not class_dic['__doc__'].strip():
            raise TypeError("类必须要有注释，且注释不能为空")
        #继承父类type的初始化行为，三个基本的类名称，基类，类的名字空间
        super(Mymeta,self).__init__(class_name,class_bases,class_dic)
class Chinese(metaclass=Mymeta):
    '''我是注释'''
    country='china'
    # print(__doc__)
    def __init__(self,name,age):
        self._name=name
        self._age=age
    def talk(self):
        print("%s is talk" %self._name)
