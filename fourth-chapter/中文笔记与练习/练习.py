#1.实例出一堆对象，并记录实例数目
class Student:
    school="luffycity"
    count=0
    def __init__(self,name,age,sex):
        self.name=name
        self.age=age
        self.sex=sex
        # self.count+=1
        Student.count+=1
    def learn(self):
        print("%s is studying " %self.name)

stu1=Student('alex',22,'female')
stu2=Student('chenshifei',23,'female')
stu3=Student('luosanpao',25,'female')
# print(stu1.__dict__)
# print(stu2.__dict__)
# print(stu3.__dict__)
# print(Student.__dict__)

#2.创建英雄，具有昵称，生命值，攻击力
#英雄A攻击了B，那么B的生命值会相应减少
#生命值减到0判定死亡
class Hero:
    def __init__(self,nick_name,life_value,aggressivity):
        self.nick_name=nick_name
        self.life_value=life_value
        self.aggressivity=aggressivity
    def attack(self,enemy):
        enemy.life_value-=self.aggressivity
class Gaven(Hero):
    # camp="Demacia"
    pass

class Calun(Hero):
    # camp="Noxus"
    pass
gaven=Gaven('caoconglun',100,30)
calun=Calun('caluncai',80,50)
print(calun.life_value)
gaven.attack(calun)
print(calun.life_value)

