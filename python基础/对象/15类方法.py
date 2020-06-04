class Tool:
    # 使用赋值语句定义类属性，记录所有工具对象的数量
    count = 0
    # 类方法
    @classmethod
    def show_tool_count(cls):

        print('工具对象的数量：%d ' % cls.count)

    def __init__(self,name):
        self.name = name  # 对象属性
        Tool.count += 1 # 类属性
    
tool1 = Tool('斧子')
tool2 = Tool('锤子')
tool3 = Tool('水桶')
Tool.show_tool_count()