## 一、字符串的基本操作

### 1. 单引号和双引号

`'string'`,`"string"`

### 2. 取字符

`string[i:j]`, `string[i:j:step]` 例如 `string[1:8:2]`

### 3. 长字符串

```python
string1 = "jjjjj"\
				"jjjjjj"\
  			"jjjjjstringstr2 = """ahhsishi
				nianaho
				hian
				"""
```

### 4. **转义字符和取消转义**（r或者R都可以)

```python
string = "abcd\n\tefg"
string = r"D:\abc\123. txt"
```

### 5. 字符串的长度

```python
string = "abcdefg"
string = "中文也可以"
len(string)
print("字符串的长度: %d" % len(string))
```

### 6. 去除空格

 `strip`（去除前后的空格）`rstrip`(去除右边的空格)`lstrip`(去除左边的空格)

```python
string = " 我 的 世界   "
string. strip()
string. rstrip()
string. lstrip()
```

### 7. 字符串的大小写

```python
string="AbCdEf"
string. upper()
string. lower()
```

### 8. 大小写互换功能

```python
string= "AbCdEf"
# 大小写互换
string. swapcase()
# 转小写，首字母大写
string. capitalize()
# 保证首字母大写,其他的都小写
string. title()
```

### 9. 判断字符串为空

```python
string = ""
len(string)==0
# 或者
string. strip()==""
```

### 10. 字符串的运算符 `+`和 `*`

```python
str1 = "abcd"
str2 = "1234"
print(str1+str2)
print(str1*10) # str1输出10遍
```

## 二、字符串的反转

### 1. 利用循环

```python
for i in range(-1,-len(string)-1,-1):
  print(string[i],end="")
# 或者
for i in range(1,len(string)+1):
  print(string[-i],end="")
```

### 2. 利用list

```python
lyst = []
for i in string:
  lyst. append(i)
lyst. reverse()
for i in lyst:
  print(i,end="")
```

### 3. 第三种 `string[::-1]`

```python
string[::-1]
# 等效于
string[-1:-len(string)-1:-1]
```



## 三、字符串的基本判断

### 1. 基本判断

```python
str.isalnum()  # 是否全是字母或者数字
str.isalpha()  # 是否全是字母
str.isdight()  # 是否全是数字
str.islower()  # 是否全是小写字母
str.isupper()  # 是否全是大写字母
str.istitle()  # 是否是标题形式的字符串
str.isspace()  # 所有字符都是空白字符
```

### 2. 汉字

```python
char>="\u4e00" and char<="\u9fa5 "
```



## 四、判断字符串相等

### 1. `==`和 `is`

```python
str1 = "abc"
str2 = "abc"
print(str1==str2)  # 两个字符串的内容一样
print(str1 is str2)  #两个字符串是否是同一个对象（内存地址是否是同一个  ） 

# id()
id(str1)==id(str2)

```

## 五、查找字符串 

### 1. find 

```python
string = "www.google.com"
string.find("google")  # 如果能查到，返回的包含字符串的起始位置
string.find("abc")  # 如果差不到，返回-1 

string.find("o")  # 返回第一个结果索引
string.rfind("o")  # 返回最后一个结果索引
string.find("o",6)  # 返回从index==6开始的第一个结果索引 
string.find("o",6,10)  # 返回从index==6到index==10开始的第一个结果索引 
```

### 2. index

```python
string = "www.google.com"
string.find("google")  # 如果能查到，返回的包含字符串的起始位置
try:
  string.find("abc")  # 如果差不到，就报错 
except ValueError as e:
  print(" 无法查到")
  
```

### 3. count

```python
string = "www.google.com"
string.count("c")  # 统计查询出结果的个数
```



## 六、判断包含字符串 

### 1. 使用`in`

```python
string = "www.google.com"
print('字符串中是否包含google',('google' in string))
```

### 2. 使用`find`

```python
string = "www.google.com"
print('字符串中是否包含google',string.find('google')>=0)
```

### 3. 判断以什么开头 `startswith`

```python
string = "https://www.google.com"
if string.startswith('https'):
  print('这是一个安全加密的域名')
if string.endswith('com'):
  print('这是一个公司域名')
```

### 4. 判断以什么结尾 `endswith`

```python
string = "https://www.google.com"
if string.endswith('com'):
  print('这是一个公司域名')
```

## 七、替换字符串 `replace`

```python
string = "https://www.google.com"
print(string.replace('com','cn'))
# 去除空格
str2 = "  我 是    中国  人 "
print(str2.replace(" ",''))
# 多处匹配，选择替换
str3 = "abcabcabcabc"
print(str3.replace('ab','12'))  # 默认全部替换
print(str3.replace('ab','12',2))  # 替换前两个匹配
```

## 八、拼接字符串

### 1. `+`

```python
lyst = ['abc','def','ghi']
name = ""
for i in lyst:
  name+=i+','
print(name)
```

### 2. `%s`

```python
lyst = ['abc','def','ghi']
name = "%s,%s,%s"%(lyst[0],lyst[1],lyst[2])
print(name)
```

### 3. `join`

```python
str1 ="abcd"
str2 = "123"
print(str1.join(str2))  # '1abcd2abcd3'

# 基本功能展示
lyst = ['abc','def','ghi']
sep = ','
name = sep.join(lyst)
print(name)
```

## 九、分割字符串

把大的字符串分割成多个小的字符串，与拼接对应

```python
string = 'abc,def,ghi'
print(string.split(','))
```

## 十、字符串的格式化输出

### 1. `center`

```python
print('1234'.center(10))  # 在10个字符空间内显示'1234'
print('1234'.center(10,'*'))  # 在10个字符空间内显示'1234',用'*'填充
print('123'.center(10,'*'))  # 在10个字符空间内显示'1234'，,用'*'填充，不对称，右边比左边多一个
```

### 2. `%s`

```python
name  = "Alice"
mobile = '12345678910'
email = "Alice@gmail.com"
print('姓名:%s  手机号码:%s  邮箱地址:%s'%(name,mobile,email))
```

`%-8s` 左对齐，`%10s` 右对齐，`%.2s`截取两位字符串，`%10.2s`10位占位符，截取两位字符串

