try:
    num = int(input('请输入整数：'))
    result = 8/num
    print(result)

except Exception as result:
    print('未知错误 %s ' % result)

else:
    # 没有异常才会执行
    print('尝试成功')

finally:
    # 无论是否有异常，都会执行的代码
    print('无论是否有异常都会执行')

print('-'*50)