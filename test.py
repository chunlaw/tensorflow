import random
import tensorflow as tf

numberOfDigit = 10
rank = 1

fo = open ("numbers", "r")
answers = open ( "answers", "r" )
idx = 0
no=[[0 for i in range(numberOfDigit)] for i in range (1000000)]
while True:
    str = fo.readline()
    if ( str == '' ):
        break;
    numbers = str.split()
    for i in range(numberOfDigit):
        no[idx][i] = int( numbers[i] )
    idx += 1

fo.close()
answers.close()

def next_batch( no, size ):
    batch_x = random.sample(no, size)
    batch_y = [0 for i in range (size)]
    for i in range(size):
        batch_y[i] = [reduce(lambda xx, yy: xx + yy, batch_x[i]) / (len(batch_x[i])+0.)]
    return batch_x, batch_y

x = tf.placeholder("float", [None,numberOfDigit])
#W = tf.Variable(tf.random_uniform([numberOfDigit,1],0,1))
W = tf.Variable(tf.random_uniform([numberOfDigit,1],0.1,0.1))
b = tf.Variable(tf.zeros([1]))

y = tf.matmul(x,W)+b # tf.nn.softmax(tf.matmul(x,W)+b)
y_= tf.placeholder("float", [None,1])

cross_entropy = tf.sqrt((tf.abs(y_ -y)))

train_step = tf.train.GradientDescentOptimizer(0.).minimize(cross_entropy)
init = tf.initialize_all_variables()

sess = tf.Session()
sess.run(init)

for i in range (10):
    batch_xs, batch_ys = next_batch(no, 500)
    print sess.run(cross_entropy, feed_dict={x:batch_xs, y_:batch_ys})
    print sess.run (W)
    #print sess.run (y, feed_dict={x:batch_xs, y_:batch_ys})
    sess.run (train_step, feed_dict={x:batch_xs, y_:batch_ys})

correct_prediction = tf.less_equal ( tf.sub ( y, y_ ), tf.constant(0.1) )
accuracy = tf.reduce_mean(tf.cast(correct_prediction, "float"))
batch_xs, batch_ys = next_batch(no,10)
print numberOfDigit, rank
ans = sess.run(y, feed_dict = {x: batch_xs, y_:batch_ys})

for i in range(10):
    print ans[i], batch_ys[i]
