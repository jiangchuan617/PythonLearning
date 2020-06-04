class Tool:
    # 使用赋值语句定义类属性，记录所有工具对象的数量
    count = 0
    def __init__(self,name):
        self.name = name 
        Tool.count += 1
    
tool1 = Tool('斧子')
tool2 = Tool('锤子')
tool3 = Tool('水桶')
print(Tool.count)
# 变量名.count访问类属性 
# 先寻找对象属性，找不到就向上寻找类属性
print(tool1.count)