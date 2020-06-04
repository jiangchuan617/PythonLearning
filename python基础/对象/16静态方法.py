class Dog(object):

    # 既没访问类属性，也没访问对象属性 可能是静态方法
    # def run(self):
    #     print('小狗跑')

    @staticmethod
    def run():
        # 既没访问类属性，也没访问对象属性
        print('小狗跑')
    
#通过类名.调用静态方法， 不需要创建狗对象
Dog.run()