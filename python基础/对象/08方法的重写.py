class Animal:
    def eat(self):
        print('吃')

    def drink(self):
        print('喝')
    
    def run(self):
        print('跑')
    
    def sleep(self):
        print('睡')
# 继承
class Dog(Animal):
    def bark(self):
        print('汪汪叫')
class XiaoTianQuan(Dog):
    def fly(self):
        print('我会飞')

    def bark(self):# 方法重写
        print('神狗叫')

wangcai = XiaoTianQuan()
# 继承的传递性
wangcai.bark()
