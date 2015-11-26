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
    batch_y = [[0 for i in range (numberOfDigit)] for i in range(size)]
    for i in range(size):
        tmp_x = sorted(batch_x[i])
        for j in range(numberOfDigit):
            if tmp_x[rank-1] == batch_x[i][j]:
                batch_y[i][j] = 1
    return batch_x, batch_y

x = tf.placeholder("float", [None,numberOfDigit])
W = tf.Variable(tf.zeros([numberOfDigit,numberOfDigit]))
b = tf.Variable(tf.zeros([numberOfDigit]))

y = tf.nn.softmax(tf.matmul(x,W)+b)
y_= tf.placeholder("float", [None,numberOfDigit])

cross_entropy = -tf.reduce_mean(y_*(tf.log(tf.clip_by_value(y,1e-11,1.0))))

train_step = tf.train.AdamOptimizer(0.01).minimize(cross_entropy)
init = tf.initialize_all_variables()

sess = tf.Session()
sess.run(init)

for i in range (10000):
    batch_xs, batch_ys = next_batch(no, 1000)
    #print sess.run(cross_entropy, feed_dict={x:batch_xs, y_:batch_ys})
    sess.run (train_step, feed_dict={x:batch_xs, y_:batch_ys})

correct_prediction = tf.equal(tf.arg_max(y,1), tf.arg_max(y_,1))
accuracy = tf.reduce_mean(tf.cast(correct_prediction, "float"))
batch_xs, batch_ys = next_batch(no,10000)
print numberOfDigit, rank
print sess.run(accuracy, feed_dict = {x: batch_xs, y_:batch_ys})
