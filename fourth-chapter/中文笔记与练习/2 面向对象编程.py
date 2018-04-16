# 上帝思维

# 姓名：小三
# 年龄：28
# 性别：男
#
# 技能：
#   1.吃饭
#   2.学习
#   3.睡觉

class Person:
    name=None
    age=0
    sex="female"
    def eat(self):
        pass
    def study(self):
        pass
    def sleep(self):
        pass
st1=Person()
st2=Person()
st3=Person()

class Student:
    def __init__(self,name,age,sex):
        self.name=name
        self.age=age
        self.sex=sex
    def eat(self):
        pass

stu1=Student('wangxiaoya',22,'male')
#1.产生stu1对象
#2.传递对象和其他参数self=stu1
#  __init__(stu1,'wangxiaoya',22,'male')
#stu1.name='wangxiaoya'
#stu1.age=22
#stu1.sex='male'



