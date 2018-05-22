import abc
class School:
    def __init__(self,city):
        #北京，上海
        self.city=city
        # 通过学校创建课程
        self.courses=[]
        # 通过学校创建班级
        self.grades={}
class Course:
    #名称、周期、价格
    def __init__(self,name,period,price):
        self.name=name
        self.period=period
        self.price=price
class People:
    def __init__(self,name):
        self.name=name
class Student(People):
    # 选择学校，关联班级
    def __init__(self,name=None,school_obj=None,grade_obj=None):
        super(Student,self).__init__(name)
        #组合
        self.school_obj=school_obj
        self.grade_obj=grade_obj
    def choose_school(self,school_obj):
        self.school_obj=school_obj


class Teacher(People):
    def __init__(self,name,school_obj):
        #继承
        super(Teacher,self).__init__(name)
        # 关联学校
        self.school_obj=school_obj











