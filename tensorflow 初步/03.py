import tensorflow as tf 
state = tf.Variable(0,name = 'counter')
# print(state.name)
one = tf.constant(1)
new_value = tf.add(state,one)
upgarde = tf.assign(state,new_value)

# 设置变量就一定要初始化
init = tf.initialize_all_variables()
with tf.Session() as sess:
    sess.run(init)
    for _ in range(3):
        sess.run(upgarde)
        print(sess.run(state))
