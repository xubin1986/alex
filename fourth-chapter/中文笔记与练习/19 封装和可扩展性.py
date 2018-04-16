class Room:
    def __init__(self,name,owner,weight,length,height):
        self.name=name
        self.owner=owner

        self.__weight=weight
        self.__length=length
        self.__height=height
    def tell_area(self):
        return self.__weight*self.__length*self.__height
r=Room('xiangxieguoji','alex',19,19,19)
#内部实现逻辑的隐藏，增强可扩展性，内部无论修改什么，不影响外部调用。
print(r.tell_area())

