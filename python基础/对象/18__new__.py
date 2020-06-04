# __new__ object 基类提供的内置的静态方法 
# 在内存中为对象分配分配空间 
# 返回对象的引用 
# python解释器将引用作为第一参数传递给__init__

# 重写__new__ 一定要 return super().__new__(cls) 
# 否则python解释器得不到分配空间的对象引用，就不会调用对象的初始化方法

class MusicPlayer(object):
    def __new__(cls,*args,**kwargs):  # 静态方法 需要传入cls实例类 第一个参数cls是当前正在实例化的类。
        # 创建对象，自动调用
        print('创建对象，分配空间')
        # 为对象分配空间
        instance = super().__new__(cls)  # 调用父类的__new__
        # 返回对象的引用
        return instance
    def __init__(self):
        print('播放器初始化')

    
# 创建一个对象
player = MusicPlayer()
# print(player)
