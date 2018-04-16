#当子类调用一个方法，如果自己一无所有，就使用父类的，如果方法自己存在，就使用自己的方法，不使用父类的方法啦
#优先以子类派生的方法为准
class Hero:
    def __init__(self,nickname,life_value,aggresivity):
        self.nickname=nickname
        self.life_value=life_value
        self.aggresivity=aggresivity
    def attack(self,enemy):
        enemy.life_value-=self.aggresivity
class Gaven(Hero):
    camp="Demacia"
    def attack(self,enemy):
        print("from Gaven Class")
class Riven(Hero):
    camp="Noxus"

g=Gaven("草丛伦",100,30)
r=Riven("锐雯雯",80,50)

#g会优先使用自己类Gaven的方法属性attack,Gaven派生覆盖了父类Hero的方法




