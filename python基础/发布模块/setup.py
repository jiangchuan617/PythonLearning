from distutils.core import setup

setup(name='message_package', # 包名
    version='1.0', # 版本
    description='发送和接受模块', # 描述信息
    author='重小烟', # 作者
    author_email='gward@python.net', # 作者邮箱
    url='https://www.python.org/sigs/distutils-sig/', # 主页
    #   packages=['message_package.send_message', 'message_package.receive_message']
    py_modules = ['message_package.send_message', 'message_package.receive_message']
      )


# 构建模块 
# python3 setup.py build

# 生成发布的压缩包
# python3 setup.py sdist

# 安装模块
# tar -zxvf message_package-1.0.tar.gz 
# sudo python3 setup.py install

# 卸载模块
# cd /Library/Frameworks/Python.framework/Versions/3.6/lib/python3.6/site-packages
# sudo rm -r message_package*
