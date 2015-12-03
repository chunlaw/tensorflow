import tensorflow as tf
import numpy as np

noCnt = 100
noCase = 100
# Create 100 phony x, y data points in NumPy, y = x * 0.1 + 0.3
x_data = np.random.rand(noCase,noCnt).astype("float32")
y_data = np.reshape( np.mean ( x_data, axis = 1 ), (noCase,1) )

# Try to find values for W and b that compute y_data = W * x_data + b
# (We know that W should be 0.1 and b 0.3, but Tensorflow will
# figure that out for us.)
x = tf.placeholder("float32", [None, noCnt])
y_ = tf.placeholder("float32", [None,1])

W = tf.Variable(tf.random_uniform([noCnt,1], -1.0, 1.0))
b = tf.Variable(tf.zeros([1]))
tmp = tf.matmul(x,W)
y = tf.matmul (x,W) + b

# Minimize the mean squared errors.
diff = y-y_
square = tf.square(diff)
loss = tf.reduce_mean(square)
optimizer = tf.train.GradientDescentOptimizer(0.01)
train = optimizer.minimize(loss)

# Before starting, initialize the variables.  We will 'run' this first.
init = tf.initialize_all_variables()

# Launch the graph.
sess = tf.Session()
sess.run(init)

# Fit the line.
for step in xrange(100000):
    x_data = np.random.rand(noCase, noCnt).astype("float32")
    y_data = np.reshape ( np.mean ( x_data, axis=1 ), (noCase,1) )
    sess.run(train, feed_dict={x: x_data, y_: y_data})
    if step % 20000 == 0:
        print step, sess.run(W), sess.run(b)

# Learns best fit is W: [0.1], b: [0.3]
