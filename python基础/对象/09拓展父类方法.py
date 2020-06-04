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
    def bark(self):
        # 针对子类特有的需求编写代码
        print('神狗叫')
        # 使用super().调用原本在父类中封装的方法
        super().bark()
        # Dog.bark(self) 2.x版本 父类名.方法（self）
        # 增加其他子类的代码
        print('hahahaha')


wangcai = XiaoTianQuan()
# 继承的传递性
wangcai.bark()
