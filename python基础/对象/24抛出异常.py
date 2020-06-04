# python提供了一个 exception de 异常类 
# 在开发的时候需哟啊满足特定的业务需求希望抛出异常可以使用 
# 创建一个Exception 的对象 
# 使用raise 关键字抛出异常

def input_password():
    # 提示用户输入密码
    pwd = input('请输入密码：')
    # 判断密码的长度
    if len(pwd)>=8:
        return pwd
    # < 8抛出异常
    print('主动抛出异常')
    # 创建异常对象 可以使用错误信息字符串作为参数 
    ex= Exception('密码长度不够')

    raise ex
try:
    print(input_password())
except Exception as result:

    print(result)