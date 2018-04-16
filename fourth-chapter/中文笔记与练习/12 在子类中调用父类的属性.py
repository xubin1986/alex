#子类派生的方法中，重用父类的属性的方式有两种
#1.直接调用类方法，这种不依赖于继承
#2.依赖继承重用父类属性
class Hero:
    def __init__(self,nickname,life_value,aggresivity):
        self.nickname=nickname
        self.life_value=life_value
        self.aggresivity=aggresivity
    def attack(self,enemy):
        enemy.life_value-=self.aggresivity
class Gaven(Hero):
    camp="Demacia"
    def __init__(self,nickname,life_value,aggresivity,wepon):
        Hero.__init__(self,nickname,life_value,aggresivity) #指名道姓,使用类方法，而不是绑定方法，需要如实传递参数
        # super(Gaven, self).__init__(nickname,life_value,aggresivity)
        super().__init__(nickname,life_value,aggresivity)#简写，通过继承重用父类方法
        self.wepon=wepon
    def attack(self,enemy):
        Hero.attack(self,enemy) #指名道姓，调用父类的方法，实现子类重用父类的属性
        print("from Gaven Class")

class Riven(Hero):
    camp="Noxus"
g=Gaven("草丛伦",100,30,"金箍棒")
# print(g.__dict__)
r=Riven("锐雯雯",80,50)


class X(object):
    def f1(self):
        print("from X")
class A(X):
    def f1(self):
        print("from A")
class B(X):
    def f1(self):
        print("from B")
        super().f1() #本来B的父类是X，照理说是调用X的f1，但是是C调用的，必须按照C的mro顺序来调用，所以super指的是A
        #如果A中没有f1，则才是在X中去查找
class C(B,A):
    pass

print(C.mro())
c=C()
c.f1() #找到B，这时mro停在B的位置，super是继续查找下一个位置A，所以调用A的f1方法
#所以基于继承的重用是依赖于继承的，依赖于mro继承列表

