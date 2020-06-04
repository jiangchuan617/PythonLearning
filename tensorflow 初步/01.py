import tensorflow as tf 
import numpy as np
# 创建数据 
x_data = np.random.rand(100).astype(np.float32)
y_data = x_data*0.1 + 0.3

# create tensorflow structure 
Weights = tf.Variable(tf.random_uniform([1],-1,1))
biases = tf.Variable(tf.zeros([1]))
y = Weights*x_data + biases

loss = tf.reduce_mean(tf.square(y-y_data))
optimizer = tf.train.GradientDescentOptimizer(0.5)# learning rate
train = optimizer.minimize(loss)
init = tf.initialize_all_variables()

sess = tf.Session()
sess.run(init)  # 激活初始化
for step in range(201):
    sess.run(train)
    if step % 10 ==0:
        print(step,sess.run(Weights),sess.run(biases))

