class A:
    def test(self):
        print('A --- test方法')
    
    def demo(self):
        print('A --- demo方法')

class B:
    def test(self):
        print('B --- test方法')
    
    def demo(self):
        print('B --- demo方法')

class C(B,A):
    '''多继承,子类拥有多个父类的属性和方法'''
    pass

c = C()
c.test()
c.demo()
# 确定C类对象调用方法的顺序
print(C.__mro__)
