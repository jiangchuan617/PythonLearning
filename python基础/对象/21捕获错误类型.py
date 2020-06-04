try:
    num = int(input('请输入一个整数：'))
    result = 8/num
    print(result)
except ValueError:
    print('值错误')
except ZeroDivisionError:
    print('除0错误')
