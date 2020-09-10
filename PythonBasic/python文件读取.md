## Python 文件读取

## 1.with 读取文件

```python
with open(file_path,mode='r') as fd:
	content = fd.read()
print(content)
```



## 2. txt三种读取方法

- read()

  ```python
  file = open('readme') # 默认以只读方式打开
  # 第一次打开，文件指针会指向文件的开始位置
  text = file.read()
  # read 方法读取之后文件指针会移动到末尾
  print(text)
  file.close()
  ```

- readline() 按行读取

  ```python
  file = open('readme')
  while True:
       text = file.readline()
       if not text:
           break
       print(text)
  
  file.close()
  ```

- readlines()

  ```python
  file = open('readme')
  texts = file.readlines()
  # texts是一个列表list
  for text in texts:
      print(text)
  ```

## 3. 大文件的读取

### 1. 有分行的，用readline()

### 2. 没有分行的，用read(size)

```python
while True:
	content = fd.read(1024)
  if not content:
    break
  print(content)
```

### 3. 推荐使用 with 迭代器

```python
with open(file_path,mode='r') as f:
	for line in f:
		print(line,end='')
```



## 4. 写入

### 1. write() 写单行

```python
try:
  with open(file_path,mode='w') as fd:
    fd.write("123hello\n")  # 必须是字符串
except:
  print("写入异常")
else:
  print("写入成功")
```

mode='w'

1. 只能写文件 
2. 文件不存在就创建文件
3. 文件存在，先清空，再打开文件

mode ='a' 追加

1. 如果文件不存在，创建文件并写入
2. 如果文件存在，追加在文件末尾

### 2. Writelines() 写多行

```python
try:
  with open(file_path,mode='w') as fd:
    list01 = ['1000','2000','3000']
    tuple01 = ('1000','2000','3000')
    set01 = {'1000','2000','3000'}
    dict01 = {'上海':'1000','北京':'2000','南京':'3000'}  # 字典集合也可以做多行写入的参数，但是只写入key
    # 换行的问题
    for i in range(len(list01)):
      list01[i] = list01[i]+'\'
    fd.writelines(list01)  # 写list集合
except:
  print("写入异常")
else:
  print("写入成功")
```

## 5. 所有模式

| 模式 | 解释                                                         |
| ---- | ------------------------------------------------------------ |
| r    | 默认模式，文本模式下的读，不能写                             |
| w    | 文本模式下的写，文件不存在就创建，文件存在，打开内容被清空   |
| a    | 追加模式的写，不能读，文件不存在就创建，文件存在，打开不清空内容，在后面追加 |
| r+   | 可读可写，不会创建不存在的文件，从顶部开始写，会覆盖之前的此前位置的内容 |
| w+   | 可读可写，如果文件存在，会覆盖整个文件，不存在就创建         |
| a+   | 可读可写，从文件顶部读取文件，从文件底部添加内容，不存在就创建 |



## 6. 文件指针

### 1. seek(偏移量，位置)

- os.SEEK_SET 文件的相对起始位置
- os.SEEK_CUR 文件相对当前位置 `rb`格式打开
- os.SEEK_END 文件相对结束位置

### 2. tell() 获取指针的位置





复制文件

```python
file_read = open('readme','r')
file_write = open('readme[复制]','w')

while True:
    text = file_read.readline()
    if not text:
        break
    file_write.write(text)
 
file_read.close()
file_write.close()
```

## 5. Python数据格式

1. np.save和np.savez

   ```python
   np.save('name.npy',array)  # 无后缀的话自动添加后缀
   ```

   ```python
   np.savez('name.npz',array1,array2,...,c_array=c)
   ```

2. np.load

   ```python
   A=np.load('name.npz')
   print(A['arr_0'])
   print(A['arr_1'])
   print(A['c_array'])
   ```

3. 使用pickle来保存文件

4. ```python
   import pickle
   import numpy as np
   
   x = np.arange(10)
   # 导出数据
   f = open('x.pkl','wb')
   pickle.dump(x,f)
   # 导入数据
   x_ = pickle.load(f)
   ```

   
