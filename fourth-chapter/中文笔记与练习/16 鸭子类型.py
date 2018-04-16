#python崇尚鸭子类型
#类型像鸭子就行了，不需要继承，只要做得像

class Yazi:
    def talk(self):
        print("gaga")
class Peple:
    def talk(self):
        print("gege")

peple=Peple()
yazi=Yazi()
# yazi.talk()
# peple.talk()

def func(lei_yazi):
    lei_yazi.talk()
func(peple)
func(yazi)
#看到没有，我提供了一个统一得接口func，我不管你是不是鸭子，不管，我只需要把你传进去，你就按自己的叫
#不管是gege还是gaga
#类提供的多态就是 不同类也可以有相似的特征行为，供统一使用
#python提供了一个内置方法len,无论是list或者tuple或者str，无论它是什么都可以使用
#因为python崇尚鸭子类型，各种类型类提前做好了。虽然没有继承关系

