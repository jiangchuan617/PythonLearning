class A:
    def test(self):
        print('test方法')

class B:
    def demo(self):
        print('demo方法')

class C(A,B):
    '''多继承,子类拥有多个父类的属性和方法'''
    pass

c = C()
c.test()
c.demo()
