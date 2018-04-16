#当有多个类有共同特征的方法时，为了避免各自取自己的名称，通过继承的方法
#事先定义一个共同的方法，然后各自实现这个方法
#但是还是不能避免各自按自己的想法定义方法名称，不能形成统一的规范
#难道都要通过言语去沟通，沟通之后或许也不一定起到效果
#所以诞生了抽象类，抽象类中规定的抽象方法，子类必须得实现，不实现就无法实例化
#抽象类本身无法实例化

import abc
class Animal(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def run(self):
        pass

class People(Animal):
    # def walk(self):
    #     print("people is running")
    def run(self):
        print("people is running")
class Pig(Animal):
    def run(self):
        print("pig is running")
class Dog(Animal):
    def run(self):
        print("dog is running")
# people=Animal() #抽象类不能直接实例化
people=People() #如果People继承了Animal并且没有实现run方法，则会出错


