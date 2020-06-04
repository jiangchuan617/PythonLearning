##  一、定义

正则表达式是一种特殊的字符串模式，用于匹配一组字符串。

### 1. re模块

正则表达式通过 `re`模块实现

```python
import re
phone_number = input("请输入一个手机号码")
if re.match(r"1[3578]\d{9}",phone_number):
  print('手机号码有效')
else:
  print('无效的手机号码')
```

### 2. 应用场景

1. 验证
2. 查找
3. 替换

### 3. 元字符

```python
.
\
|
^
$
*
+
?
[]
{}
()
```

## 二、基本方法

### 1. match()

首字母开始匹配，string中如果包含pattern,就匹配成功，返回match的对象，失败就返回None,若要完全匹配，pattern要以$结尾。

```python
# 从头开始匹配
print(re.match("\d{3}","123abc"))  # 以三个数字开始，能匹配
# <_sre.SRE_Match object; span=(0, 3), match='123'>
print(re.match("\d{3}","abc123abc"))  # 不是以三个数字开始，不能匹配
# None
```

### 2. search()

若string中如果包含pattern,返回match的对象，否则返回None，如果string中包含多个pattern子串，只返回第一个。

```python
# 从任意位置匹配
print(re.search("\d{3}","123abc"))  # 能匹配
# <_sre.SRE_Match object; span=(0, 3), match='123'>

print(re.search("\d{3}","abc123abc123"))  # 能匹配,返回第一个匹配
# <_sre.SRE_Match object; span=(3, 6), match='123'>
```

### 3. findall()

返回string中所有与pattern相匹配的全部子串，返回形式为集合

```python
print(re.findall("\d{3}","abc123abc459,999,# 357"))  # 能匹配
# ['123', '459', '999', '357']
print(re.findall("\d{3}","abc123abc4598,999,# 357"))  # 能匹配
# ['123', '459', '999', '357']
print(re.findall("\d{3}","abc123abc459873,999,# 357"))  # 能匹配
['123', '459', '873', '999', '357']
```

## 三、正则表达式的两种写法

### 1. 简单的写法

`re.match`(正则的语法，要匹配的文本)

```python
print(re.match("\d{3}","123abc"))  
```

### 2. 标准的写法

1. 实例化正则的对象

1. 用正则对象匹配字符串

```python
pattern = re.compile("\d{3}")
match_result = pattern.match("123abc")
if match_result is None:
  print("不匹配")
else:
  print('匹配')
```

## 四、转义字符和通配字符

### 1. 转义字符: `\` 

```python
import re
print(re.findall("\^\d{3}","^123ahsn^888Hhid"))
```

### 2. 通配字符 : `.` 

能够匹配除 `\n`外的任意字符

```python
print(re.findall('a.{3}','afdfbcoiea fsisaij joaos'))
```

## 五、反斜杠的问题

### 1. 要匹配 `\`这个字符

案例：匹配\+一个数字

```python
print(re.findall("\\\\X","\assh\Xa13\Xhid"))
# ['\\X', '\\X']
```

说明：需要四个`\\\\`才能匹配一个，字符串本身的转义+正则的转义

### 2. `\`+字母：在转义字符中和正则中功能冲突

```python
print(re.findall("\\b","\assh\Xa13\Xhid"))
```

`\b`转义中是退格，正则中是字符的边界

**为了避免困扰，建议写正则的时候涉及到`\`,一律取消转义(R或者r)**

```python
print(re.findall(r"\\","\assh\Xa13\Xhid"))
# ['\\', '\\']
print(re.findall(R"\b","\assh\Xa13\Xhid"))
```

## 六、字符集合

### 1. 基本语法

| 语法 | 描述                                                   |
| :--- | ------------------------------------------------------ |
| \d   | 匹配一个0-9之间的数字，和[0-9]一样                     |
| \w   | 匹配一个字母、数字、下划线（典型的邮箱地址和网址）     |
| \s   | 匹配一个所有的空白字符（空格、制表、回车、换页、换行） |
| \D   | 匹配一个非数字字符，和\d相反                           |
| \W   | 匹配一个非单词字符，和\w相反                           |
| \S   | 匹配一个非空白字符，和\s相反                           |

案例：非数字开头+两个空格+数字/字母/下划线结尾

```python
import re
print(re.findall(r"\D\s{2}\w","a  4hidhij  _f"))
# ['a  4', 'j  _']
```

### 2. 自定义字符集合[]

| 语法      | 描述                       |
| --------- | -------------------------- |
| [0-9]     | 匹配0-9数字，和\d一样      |
| [a-zA-Z]  | 匹配所有大小写字母         |
| [abc]     | 匹配abc中的任意一个        |
| [^abc]    | 匹配除abc外的任意一个      |
| [ab5@]    | 匹配a、b、5、@中的任意一个 |
| [^a-f0-3] | 匹配除a-f,0-3中的任意一个  |

案例：匹配a-f开头（不区分大小写）+三个小写字母+以偶数结尾

```python
print(re.findall(r"[a-fA-F][a-z]{3}[02468]","Ffff6hiuu7hishie4usdy83k2022jncskd8"))
# ['Ffff6', 'cskd  8']
```

### 3. 特别注意

正则表达式中的特殊字符被包含在中括号中就失去了特殊的意义，除 `^`和 `-`

## 七、量词

### 1. `*`---重复0次或者更多次

```python
print(re.findall(r"na[a-z]*e","my name is Alice,nae,naucgoduwyedh"))
# ['name', 'nae', 'naucgoduwye']
```

### 2. `+`---重复一次或者更多次

```python
print(re.findall(r"na[a-z]+e","my name is Alice,nae,naucgoduwyedh"))
# ['name', 'naucgoduwye']
```

### 3. `?`---重复0次或者一次

```python
print(re.findall(r"na[a-z]?e","my name is Alice,nae,naucgoduwyedh"))
# ['name', 'nae']
```

### 4. `{m}`---重复m次

```python
print(re.findall(r"na[a-z]{5}e","my name is Alice,nae,nauruwyedh"))
# ['nauruwye']
```

### 5. `{m,n}`---重复m~n次

```python
print(re.findall(r"na[a-z]{1,5}e","my name is Alice,nae,nauruwyedh"))
# ['name', 'nauruwye']
```

### 6. `{m,}`重复m次到无限次

```python
print(re.findall(r"na[a-z]{3,}e","my name is Alice,nae,nauruwyedh，nahisowuowouwouowuowwe"))
# ['nauruwye', 'nahisowuowouwouowuowwe']
```

### 7. 贪婪模式和非贪婪模式

`贪婪模式` 默认情况下，尽可能多的匹配

```python
# 尽可能多的匹配
print(re.findall(r"\d+","12374793791abc"))
# ['12374793791']
print(re.findall(r"\d*","12374793791abc"))
# ['12374793791', '', '', '', '']
print(re.findall(r"\d{3,8}","12374793791abc"))
# ['12374793', '791']
```

`非贪婪模式` `?`默认情况下，尽可能少的匹配

```python
print(re.findall(r"\d+?","12374793791abc"))
# ['1', '2', '3', '7', '4', '7', '9', '3', '7', '9', '1']
print(re.findall(r"\d{3,8}?","12374793791abc"))
# ['123', '747', '937']
```

## 八、字符边界

### 1. `^`---开始位置

```python
# 以95开头的数字
print(re.findall(r"^95\d*","95268289abc"))
# ['95268289']
```

### 2. `$`---结束位置

```python
# 以95结尾
print(re.findall(r"[a-z]{3}95$","95268289abcyiwn95"))
#  ['iwn95']
```

###  3. `\b`---单词的边界---位置---零宽度

`\b`某一个位置的前后不都是`\w`(字母、数字、下划线)

```python
# 求以字母abc开头的单次
str01 = "To judge from the reaction of the studio audience, the answer to the question of who won last night’s debate between Boris Johnson and Jeremy Corbyn was neither of the above."
print(re.findall(r"\b[abcABC][a-z]*\b",str01))
# ['audience', 'answer', 'between', 'Boris', 'and', 'Corbyn', 'above']
```

### 4. `\B`---与`\b`相反

## 九、其他

### 1. 逻辑或

```python
import re
print(re.match(r"\d{14}[0-9x]|\d{17}[0-9x]","12345678912345x"))
# <_sre.SRE_Match object; span=(0, 15), match='12345678912345x'>

```

### 2. 分组

1. 非捕获组 `?:`

   ```python
   str01 = "To judge from the reaction of the studio audience, the answer to the question of who won last night’s debate between Boris Johnson and Jeremy Corbyn was neither of the above."
   pattern = re.compile(r"\b[a-z]*(?:er|ing|ous|ons)\b")
   print(pattern.findall(str01))
   
   # ['answer', 'neither']
   ```

2. 捕获组---使用迭代函数

   ```python
   match_result = re.finditer(r'\b([a-z])([a-z])[a-z]\2\1\b',"frarf abcba usuwh iuyui")
   for i in match_result:
   	  print(i)
   # <_sre.SRE_Match object; span=(0, 5), match='frarf'>
   # <_sre.SRE_Match object; span=(6, 11), match='abcba'>
   # <_sre.SRE_Match object; span=(18, 23), match='iuyui'>
   
   for i in match_result:
   	  print(i.group(0))
       
   # frarf
   # abcba
   # iuyui
   
   ```

   ![image-20191125225605944](https://tva1.sinaimg.cn/large/006y8mN6ly1g9aofnjaqdj315g0i64hk.jpg)

![image-20191125225910075](https://tva1.sinaimg.cn/large/006y8mN6ly1g9aok1fy4pj31t604i3z7.jpg)

### 3.  零宽断言

做位置的匹配，不占用位置

主要用于判断某个位置的前后字符

|   格式   |               意义                |
| :------: | :-------------------------------: |
| (?=exp)  |  断言自身出现的位置后面能匹配exp  |
| (?<=exp) |  断言自身出现的位置前面能匹配exp  |
| (?!exp)  | 断言自身出现的位置后面不能匹配exp |
| (?<!exp) | 断言自身出现的位置后面不能匹配exp |

```python
print(re.findall(r'\b(?<=name=)[a-z]+\b','abcd name=alice name=bob name=stcik'))
# ['alice', 'bob', 'stcik']
str01 = "www.iLink.com www.google.com www.apple.cn"
print(re.findall(r'(?<=www[.])[a-zA-Z]+(?=[.])',str01))
# ['iLink', 'google', 'apple']
```

## 十、python正则表达式应用

### 1. 判断是否符合要求

1. match() 完全匹配
2. search() 包含

### 2. 获取捕获的内容

1. findall()
2. finaiter()

### 3. 正则匹配修饰符

1. re.I ---忽略大小写

   ```python
   print(re.findall(r'\bilync\b',str01,re.I))
   ```

2. re.M --- 多行模式

   ```python
   str01 = "ilync\nilync\nilync\nilync"
   print(re.findall(r'^ilync',str01,re.M))  # 每一行就是一个匹配的字符串
   ```

3. 其他总结

   ![image-20191128173613976](https://tva1.sinaimg.cn/large/006y8mN6ly1g9dw18beyaj31wk0oakie.jpg)

### 4. match对象

| 常见方法 | 含义                                                         |
| -------- | ------------------------------------------------------------ |
| group()  | 获取一个或者多个分组的截获的字符串，不填写参数时，返回group(0) |
| groups() | 以元组形式返回所有截获的字符串，default表示没有截获字符串的时，以这个值代替，默认为None |
| start()  | 返回截获子串的起始索引                                       |
| end()    | 返回截获子串的结束索引                                       |
| span()   | （start,end）                                                |

### 5. split函数

`re.split()`

标准版的split()只能按照一个字符来切割

```python
str01 = "abc:syw,hiyie|dyow\twhhosj\newojo"
lyst = re.split(":|,|\||\t|\n",str01)
# ['abc', 'syw', 'hiyie', 'dyow', 'whhosj', 'ewojo']
```

如何去除空的元素

```python
str01 = "abc::::syw,,,hiyie|||dyow\t\twhhosj\n\n\newojo"
lyst = re.split(":|,|\||\t|\n",str01)
lyst = [i for i in lyst if i]
# ['abc', 'syw', 'hiyie', 'dyow', 'whhosj', 'ewojo']
```



### 6.  sub函数和subn函数

1. sub()

   `sub(pattern,repl,str,count)`

2. subn()

   ```python
   tuple01 = subn(patten,repl,str,flags=re.I)
   print('替换后的文本',tuple01[0])
   print('替换次数：',tuple01[1])
   ```