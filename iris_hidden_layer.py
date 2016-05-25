import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt

graph = raw_input("Show errors graph (y/n): ")
response = str(graph).strip()

# Translate a list of labels into an array of 0's and one 1.
# i.e.: 4 -> [0,0,0,0,1,0,0,0,0,0] 
def one_hot(x, n):
    if type(x) == list:
        x = np.array(x)
    x = x.flatten()
    o_h = np.zeros((len(x), n))
    o_h[np.arange(len(x)), x] = 1
    return o_h


data = np.genfromtxt('iris.data', delimiter=",")
np.random.shuffle(data)
x_data = data[:,0:4].astype('f4')
y_data = one_hot(data[:,4].astype(int), 3)

#print y_data

#print "\nSome samples..."
#for i in range(20):
#    print x_data[i], " -> ", y_data[i]
#print


NUMBER_OF_ENTRIES = 4
OUTPUT_LAYER_NEURONS = 3

x = tf.placeholder("float", [None, NUMBER_OF_ENTRIES])
y_ = tf.placeholder("float", [None, OUTPUT_LAYER_NEURONS])


HIDDEN_LAYER_NEURONS = 4

hidden_W = tf.Variable(np.float32(np.random.rand(NUMBER_OF_ENTRIES, HIDDEN_LAYER_NEURONS)) * 0.1)
hidden_b = tf.Variable(np.float32(np.random.rand(HIDDEN_LAYER_NEURONS)) * 0.1)

W = tf.Variable(np.float32(np.random.rand(HIDDEN_LAYER_NEURONS, OUTPUT_LAYER_NEURONS)) * 0.1)
b = tf.Variable(np.float32(np.random.rand(OUTPUT_LAYER_NEURONS)) * 0.1)

hidden_y = tf.sigmoid(tf.matmul(x, hidden_W) + hidden_b)

y = tf.nn.softmax((tf.matmul(hidden_y, W) + b))


cross_entropy = tf.reduce_sum(tf.square(y_ - y))
#cross_entropy = -tf.reduce_sum(y_*tf.log(y))

train = tf.train.GradientDescentOptimizer(0.01).minimize(cross_entropy)

init = tf.initialize_all_variables()

sess = tf.Session()
sess.run(init)

print "----------------------"
print "   Start training...  "
print "----------------------"

batch_size = 20

errors = []
for step in xrange(1000):
    for jj in xrange(len(x_data) / batch_size):
        batch_xs = x_data[jj*batch_size : jj*batch_size+batch_size]
        batch_ys = y_data[jj*batch_size : jj*batch_size+batch_size]

        sess.run(train, feed_dict={x: batch_xs, y_: batch_ys})
        if step % 50 == 0:
            error = sess.run(cross_entropy, feed_dict={x: batch_xs, y_: batch_ys})
            errors.append(error)
            print "Iteration #:", step, "Error: ", error
            result = sess.run(y, feed_dict={x: batch_xs})
            for b, r in zip(batch_ys, result):
                print b, "-->", r
            print "----------------------------------------------------------------------------------"


if response == "y":
    plt.plot(errors)
    plt.show()
            
            
            
