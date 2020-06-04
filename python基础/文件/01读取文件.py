file = open('readme') # 默认以只读方式打开
# 第一次打开，文件指针会指向文件的开始位置

text = file.read()

# read 方法读取之后文件指针会移动到末尾
print(text)

file.close()