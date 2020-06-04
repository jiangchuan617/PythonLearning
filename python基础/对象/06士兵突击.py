class Gun:
    def __init__(self,model):
         self.model = model
         self.bullet_count = 0
    
    def add_bullet(self,count):
        self.bullet_count += count
    
    def shoot(self):
        # 判断子弹数量
        if self.bullet_count <=  0:
            print('没有子弹。')
            return 
        # 发射子弹
        while self.bullet_count:
            self.bullet_count -= 1
            print('[%s] 突突突。。。[%d]' % (self.model,self.bullet_count))
        # 发射提示信息
 
class Soldier:
    def __init__(self,name):
        self.name = name
        self.gun = None#新兵没有抢

    def fire(self):
        # 判断是否有枪
        if self.gun is None :
            print('[%s] 还没有枪' % self.name)
            return 
        print('冲啊。。。[%s]' % self.name)

        self.gun.add_bullet(50)

        self.gun.shoot()
ak47 = Gun('AK47')
# ak47.add_bullet(50)
# ak47.shoot()

xusanduo = Soldier('许三多')
xusanduo.gun = ak47
xusanduo.fire()
 