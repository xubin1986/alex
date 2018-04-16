#类的继承
class Foo:
    def __init__(self):
        pass
    def f1(self):
        print("f1 in Foo")
    def f2(self):
        print("f2 in Foo")
        self.f1()
class Bar(Foo):
    def f1(self):
        print("f1 in Bar")

b1=Bar()
b1.f1() #子类有属性，使用自己的属性
b1.f2()#子类没有从父类查找属性，找到f2，但是传入的self是自己，调用的f1自身有


