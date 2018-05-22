import abc
class School:
    def __init__(self,name,city):
        #学校的名称luffycity
        self.name=name
        #学校的城市校区，北京，上海
        self.city=city
        # 通过学校创建课程
        self.__courses=[]
        # 通过学校创建班级
        self.__grades=[]
    # 通过学校创建课程
    def add_course(self,course_obj):
        self.__courses.append(course_obj)
    @property
    def courses(self):
        return self.__courses

    # 通过学校创建班级
    def add_grade(self,grade_obj):
        self.__grades.append(grade_obj)
    @property
    def grades(self):
        return self.__grades

# 通过学校创建班级， 班级关联课程、讲师

class Course:
    #名称、周期、价格
    def __init__(self,name,period,price):
        self.name=name
        self.period=period
        self.price=price
    def getinfo(self):
        print("course_name:<%s> period:<%s months> price:<￥%s>" %(self.name,self.period,self.price))

class Grade:

    # 班级关联课程、讲师
    # python 16期
    def __init__(self,course_obj,teache_obj=None):
        self.course_obj=course_obj
        self.teache_obj=teache_obj

#元类和抽象类
class People(metaclass=abc.ABCMeta):
    def __init__(self,name,age,sex):
        self.name=name
        self.age=age
        self.sex=sex
    def playinfo(self):
        print("name:<%s> age:<%s> sex:<%s>" %(self.name,self.age,self.sex))
    #抽象类，子类必须实现,否者调用子类进行实例化会报错
    # Can't instantiate abstract class Teacher with abstract methods register
    @abc.abstractmethod
    def register(self):
        pass

class Student(People):
    # 选择学校，关联班级
    def __init__(self,name=None,age=None,sex=None,school_obj=None,grade_obj=None):
        super(Student,self).__init__(name,age,sex)
        #组合
        self.school_obj=school_obj
        self.grade_obj=grade_obj
    #学员视图， 可以注册， 交学费， 选择班级
    def playinfo(self):
        print("name:<%s> age:<%s> sex:<%s> schoolname:<%s> grade:<%s>"
              %(self.name,self.age,self.sex,self.school_obj.name,self.grade_obj.course_obj.name))
    def register(self):
        self.name=input("username>:").strip()
        self.age=input("age>:").strip()
        self.sex=input("sex>:").strip()
        self.passwd=input("passwd>:").strip()


class Teacher(People):
    def __init__(self,name,age,sex,school_obj):
        #继承
        super(Teacher,self).__init__(name,age,sex)
        # 关联学校
        self.school_obj=school_obj
    #派生
    def playinfo(self):
        def playinfo(self):
            print("name:<%s> age:<%s> sex:<%s> schoolname:<%s> "
                  % (self.name, self.age, self.sex, self.school_obj.name))

    def register(self):
        pass
class Authentication:
    def __init__(self,user,passwd,role):
        #封装
        self.__user=user
        self.__password=passwd
        self.__role=role
    def authenticate(self):
        pass

class Register:
    def __init__(self,role):
        self.role=role
    def register(self):
        if self.role == "student":
            pass


class Manager:
    def __init__(self):
        pass
    def create_school(self):
        pass
    def create_grade(self):
        pass


class Inner:
    #半封装
    _school_list=[]

    @classmethod
    def myinit(cls):
        school_bj = School("luffy", "北京")
        school_sh = School("luffy", "上海")

        linux = Course('linux', 6, 5000)
        python = Course('python', 8, 8000)
        go = Course('go', 7, 7500)

        school_bj.add_course(linux)
        school_bj.add_course(python)
        school_sh.add_course(go)

        cls._school_list.append(school_bj)
        cls._school_list.append(school_sh)
    def __str__(self):
        return "this is a inner interface to enter"










