class Dog:
    def __init__(self,name):
        self.name = name 
    
    def game(self):
        print('%s 蹦蹦跳跳的玩耍。。。' % self.name)
    
class XiaoTianDog(Dog):
    def game(self):
        print('%s 飞到天上去玩耍。。。' % self.name)

class Person:
    def __init__(self,name):
        self.name = name 
    
    def game_with_dog(self,dog):
        print('%s 和 %s 快乐的玩耍。。。' % (self.name,dog.name))
        dog.game()

# 创建一个狗对象
# wangcai = Dog('旺财')
wangcai = XiaoTianDog('飞天旺财')
# 创建小明对象
xiaoming = Person('小明')
# 小明和狗玩耍
xiaoming.game_with_dog(wangcai)

