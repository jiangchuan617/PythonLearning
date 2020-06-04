class MusicPlayer(object):
    # 定义一个类属性记录第一个被创建对象的引用
    instance = None
    # 定义一个类属性 init_flag 标记是否执行过初始化动作，初始值为 False
    init_flag = False
    def __new__(cls,*args,**kwargs):
        # 判断类属性是否是空对象
        if cls.instance is None:
             # 调用父类的方法为第一个对象分配空间
             cls.instance = super().__new__(cls)

        # 返回类属性保存的对象引用
        return cls.instance
    
    def __init__(self):
        if MusicPlayer.init_flag:
            return 
        print('初始化播放器')
        MusicPlayer.init_flag = True



player1 = MusicPlayer() 
print(player1)
player2 = MusicPlayer()
print(player2)