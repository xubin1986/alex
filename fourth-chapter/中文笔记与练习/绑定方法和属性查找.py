class Student:

    def __init__(self,name,age,sex):
        self.name=name
        self.age=age
        self.sex=sex

    def eat(self):
        print("eat")

#绑定方法，类的方法是给对象用的，哪个对象调用方法就绑定到哪个对象，每个对象的绑定方法不同
stu1=Student('alex',24,'female')
stu2=Student('chenshifei','29','female')
print(stu1.eat,"和stu2地址不一样的")
print(stu2.eat,"和stu1地址不一样的")

#属性查找顺序，先查找属于对象的数据，如果不存在，再查找类的属性，不存在就不会再查找全局的了
x="global"
class Student:
    x="class data"
    def __init__(self,name,age,sex):
        self.name=name
        self.age=age
        self.sex=sex
    def eat(self):
        print("eat")
stu1=Student('alex',24,'female')
stu1.x="object data"
print(stu1.x)
del stu1.x
print(stu1.x)
#如果删除对象和类的x数据属性,将不会查找全局的数据属性，会报错
try:
    del Student.x
    print(stu1.x)
except AttributeError as e:
    print("x not exist!")

