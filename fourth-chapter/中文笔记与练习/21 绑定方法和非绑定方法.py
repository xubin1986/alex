import settings
import time,hashlib
class Foo:
    def __init__(self,name):
        self.name=name
    def tell(self):  #绑定对象方法，没有任何装饰器修饰，谁调用自动传谁进入
        print(self.name)
    @classmethod  #绑定类方法，类调用传类进入
    def tell_class(cls):
        print(cls)
    @staticmethod  #非绑定方法，类和对象都可以调用。不会传递类和对象
    def tell_static(x,y):
        print(x+y)

class People:
    def __init__(self,name,age,sex):
        self.name=name
        self.age=age
        self.sex=sex
        self.id=self.get_id()
    def tell_info(self):
        print(self.name,self.age,self.sex)
    @classmethod
    def from_conf(cls): #根据配置文件生成一个obj
        obj=cls(settings.name,settings.age,settings.sex)
        return obj
    @staticmethod
    def get_id():
        m=hashlib.md5(str(time.time()).encode('utf-8'))
        return m.hexdigest()
p=People.from_conf()
print(p.id)
