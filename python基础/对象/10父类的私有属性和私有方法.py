class A:
    def __init__(self):
        self.num1 = 100
        self.__num2 = 200
    
    def __test(self):
        print('私有方法 %d %d ' % (self.num1,self.__num2))
    
    # 子类对象可以通过父类的公有方法间接访问到私有属性和私有方法
    def test(self):
        print('父类的公有方法 % d' % self.__num2)
        self.__test()

class B(A):
    def demo(self):
        # 在子类的对象方法中不能访问父类的私有属性,私有方法
        # print('访问父类的私有属性 %d ' % self.__num2)
        # self.__test()

        # 访问父类的公有属性
        print('子类属性：%d ' % self.num1)
        # 调用父类中的公有方法
        self.test()

b = B()
print (b.num1)
b.demo()
