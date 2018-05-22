#
#  exec()的用法
# globals() 全局名字空间
# locals() 局部名字空间
# exec()执行字符串命令
'''
g={'x':1,'y':2}
l={}
exec("""
global x,y
x=10
z=1
""",g,l)
print(l)
print(g)
glocals()使用g作为全局，locals()使用l
'''


# 一切皆对象
'''
可以作为参数
可以作为返回值
可以调用
可以作为容器的元素
'''
# 追根溯源 class机制
'''
类的三要素：
1.类名称
2.类体，名字空间
3.类的基类元组
'''
'''
类的定义方法：
1.class关键字
class A:
    x=1
    def run(self):
        print("run...")
2.元类定义

'''
class_name="People"
class_bases=(object,)
class_dicts={}
class_bodys="""
name="alex"
def run(self):
    print("%s is running...." %self.name)
"""
#默认创建也会调用这个过程，只是类标准创建会修改__name为相应的东西。
exec(class_bodys,globals(),class_dicts)
# 调用元类type（也可以自定义）来产生类
People=type(class_name,class_bases,class_dicts)

p=People()
p.run()

# 默认元类都是type这个类
class B(metaclass=type):
    name='B'
    def __init__(self):
        print(self.name)

#一切皆对象，类也是对象，类是元类type的对象


