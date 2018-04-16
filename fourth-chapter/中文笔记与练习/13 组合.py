
class People:
    school='luffycity'
    def __init__(self,name,age,sex):
        self.name=name
        self.age=age
        self.sex=sex
class Teacher(People):
    def __init__(self,name,age,sex,level,salary):
        super().__init__(name,age,sex)
        self.level=level
        self.salary=salary
    def teacher(self):
        print("%s is teaching" %self.name)
class Student(People):
    def __init__(self,name,age,sex,class_time):
        super().__init__(name, age, sex)
        self.class_time=class_time
    def learn(self):
        print("%s is learning" %self.name)
class Course:
    def __init__(self,course_name,course_period):
        self.course_name=course_name
        self.course_period=course_period
    def tell_info(self):
        print("课程名称 <%s> 课程时间 <%s>" %(self.course_name,self.course_period))
class Date:
    def __init__(self,year,month,day):
        self.year=year
        self.month=month
        self.day=day
    def tell_info(self):
        print("%s-%s-%s" %(self.year,self.month,self.day))
t1=Teacher('alex',32,'female','high',90000)
s1=Student('chenshifei',28,'female','9:00')
course=Course('python','2mons')
t1.course=course
t1.course.tell_info()
date=Date('1989','04','02')
s1.date=date
s1.date.tell_info()

#当对象是某个类，或者属于某个类的时候使用继承
#当对象有某个特征的时候，使用组合的方式，让特征对象成为对象的数据属性
#是和有的关系