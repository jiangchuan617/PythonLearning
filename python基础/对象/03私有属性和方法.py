class Woman:
    def __init__(self,name,age):
        self.name = name 
        self.__age = age
    def __secret(self):
        print('%s 的年龄是：%d' % (self.name,self.__age))
    
lqq = Woman('郦倩倩',24)
print(lqq._Woman__age)
lqq._Woman__secret()