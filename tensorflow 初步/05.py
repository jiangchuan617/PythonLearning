import tensorflow as tf 
import numpy as np 
def add_layer(inputs,in_size,out_size,activation_function = None):
    Weights = tf.Variable(tf.random_normal([in_size,out_size]))
    # biases = tf.Variable(tf.zeros([out_size,1]))+0.1
    biases = tf.Variable(tf.zeros([1,out_size]))+0.1
    Wx_plus_b = tf.matmul(inputs,Weights)+biases
    if activation_function is None:
        outputs = Wx_plus_b
    else:
        outputs = activation_function(Wx_plus_b)

    return outputs

x_data = np.linspace(-1,1,300)[:,np.newaxis]
# x_data = np.linspace(-1,1,300)
noise = np.random.normal(0,0.05,x_data.shape)
y_data = np.square(x_data)-0.5+noise
# print(x_data.shape)
xs = tf.placeholder(tf.float32,[None,1])
ys = tf.placeholder(tf.float32,[None,1])
l1 = add_layer(xs,1,10,activation_function = tf.nn.relu)
prediction = add_layer(l1,10,1,activation_function = None)

loss = tf.reduce_mean(tf.reduce_sum(tf.square(ys-prediction),reduction_indices = [1]))
train_step = tf.train.GradientDescentOptimizer(0.1).minimize(loss)
init = tf.initialize_all_variables()
with tf.Session() as sess:
    sess.run(init)
    for i in range(1000):
        sess.run(train_step,feed_dict={xs:x_data,ys:y_data})
        if i %20 == 0:
            print(sess.run(loss,feed_dict={xs:x_data,ys:y_data}))





