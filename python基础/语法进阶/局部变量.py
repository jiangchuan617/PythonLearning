def demo(*args,**kwargs):
    print(args)
    print(kwargs)


gl_nums=(1,2,3)#元组
gl_dict={'name':'lqq',"age":18}
demo(*gl_nums,**gl_dict) #拆包
