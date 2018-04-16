# property是一个装饰器
# 可以将方法转换为属性，直接调用属性，就可以执行方法
# 让看起来是数据属性的就转换方法为数据属性
# 让使用者感知不到是方法，而是让使用者觉得是变量或者属性，但是这个属性无法赋值
class People:
    def __init__(self,name):
        self.__name=name
    #转换为属性
    @property
    def name(self):
        return self.__name
    #方法必须有一个返回值，作为name的结果
    @name.setter
    def name(self,val):
        if not isinstance(val,str):
            print("必须为字符串")
            return
        self.__name=val
    @name.deleter
    def name(self):
        print("不允许删除")

p=People('chenshifei')
p.name="alex"
del p.name
print(p.name)

#特性
