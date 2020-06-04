class Cat():
    '''这是一个猫类'''
    def __init__(self,new_name):

        self.name = new_name
        print("%s lalee" % self.name)
    def eat(self):
        print('%s 爱吃鱼' % self.name)
    
    def __str__(self):
        #必须返回字符串
        return '我是小猫 %s' % self.name

    def __del__(self):
        print('%s 走了' % self.name)

tom = Cat("tom")
print(tom)