class HouseItem:
    def __init__(self,name,area):
         self.name = name
         self.area = area
        
    def __str__(self):
        return '[%s]占地面积：%.2f' % (self.name,self.area)


class House:
    def __init__(self,house_type,area):
        self.house_type = house_type
        self.area = area
        self.free_area = area
        self.itemlist = []
    
    def __str__(self):
        return ('户型：%s\n总面积：%.2f [剩余：%.2f]\n家具：%s' 
                 % (self.house_type,self.area,
                self.free_area,self.itemlist))
         
    def add_item(self,item):
        print('要添加 %s ' % item)
        if item.area > self.free_area:
            print('%s 的面积也太大了，无法添加。' % item.name)
            return 
        
        self.itemlist.append(item.name)
        self.free_area-=item.area 
        
# 创建家具
bed = HouseItem('席梦思',40)
chest = HouseItem('衣柜',2)
table = HouseItem('餐桌',20)
# print(bed)
# print(chest)
# print(table)

# 创建房子对象
my_home = House('两室一厅',60)
# my_home.add_item(bed)
# my_home.add_item(chest)
# my_home.add_item(table)
print(my_home)