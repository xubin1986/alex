class A:
    __name="name"
    def __func(self):
        self.__name="2"
        print(self.__name)
# print(A.__name) #直接访问隐藏属性是访问不了的
# print(A.__dict__) #发现没有__name属性，只有_A__name，那么就是类将__name改成了_A__name
# print(A._A__name)#发现确实能够直接通过修改后的名称访问到，并且是在类定义的时候就修改了的
# print(A._A__func(A))#在内定义期间__name被改成了_A__name,代码都修改了
# 隐藏只是一种规范，并未限制

#继承不能覆盖隐藏属性，因为每一个隐藏属性都会被修改名称


#内部可以调用隐藏属性
#外部不可以直接调用
#变形过程只在类定义后发生一次，之后添加或赋值的都不会被修改
# A.__x=1
# print(A.__x)



