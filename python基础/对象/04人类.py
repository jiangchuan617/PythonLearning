class Person:
    def __init__(self,name,weight):
        self.name = name
        self.weight = weight

    def __str__(self):
        return '我的名字是 %s，体重是 %.2f 公斤' % (self.name,self.weight)
    
    def eat(self):
        print('%s 爱吃东西' % self.name)
        self.weight+=1
    
    def run(self):
        print('%s 爱跑步，跑步锻炼身体'%self.name)
        self.weight-=0.5
        
#小明爱跑步
xiaoming=Person('小明',75.0)
xiaoming.eat()
xiaoming.run()
print(xiaoming.weight)

#小美爱跑步
xiaomei = Person('小美',45)
xiaomei.eat()
xiaomei.run()
print(xiaomei.weight)