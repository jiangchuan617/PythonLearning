## 异常处理包含

1. 异常捕获
2. 异常抛出

## 异常捕获

### 形式

1. try...except...

   ```python
   try:
     ...如果可能出现异常的代码
   except:
     ...如果出现异常执行的代码
   ```

   ```python
   try:
     ...
   except Exception as e:
     print(e)  # 反馈基本的异常信息
     print(str(e))
     print(e.args[0])
     print(repr(e))  # 返回的是异常的类型和基本信息
     
   ```

   ```python
   import traceback
   try:
     ...
   except ValueError as e:
     print('数值异常')
   except ZeroDivisionError as e:
     print('除零异常')
   except Exception as e:
     print(traceback.format_exc()) # 异常的详细信息
     # 将异常的详细信息写入到日志中
     traceback.print_exc(file = './systemlogerror.txt','w')
   ```

2. try...except...else:

   ```python
   try:
     ...如果可能出现异常的代码
   except:
     ...如果出现异常执行的代码
   else: 
     ...如果没有出现异常执行的代码 
   ```

3. try...except...finally:

   ```python 
   try:
     ...如果可能出现异常的代码
   except:
     ...如果出现异常执行的代码
   finally: 
     ...无论是否有异常都执行的代码（主要是做资源的回收，文件的打开关闭，数据库关闭连接）
   ```

   

4. try...except...else...finally:

   ```python
   try:
     ...如果可能出现异常的代码
   except:
     ...如果出现异常执行的代码
   else: 
     ...如果没有出现异常执行的代码 
   finally: 
     ...无论是否有异常都执行的代码（主要是做资源的回收，文件的打开关闭，数据库关闭连接）
   ```

## 抛出异常

 关键字  raise 

```python
raise Exception("...")
```

