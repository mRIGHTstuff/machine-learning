import numpy as np 
import matplotlib.pyplot
%matplotlib inline
import tensorflow as tf 

learn = tf.contrib.learn
tf.logging.set_verbosity(tf.logging.ERROR)

# Import the dataset
mnist = learn.datasets.load_dataset('mnist')
data = mnist.train.images
labels = np.asarray(mnist.train.labels, dtype=np.int32)
test_data = minst.test.images
test_labels = np.asarray(mnist.test.labels, dtype=np.int32)

max_examples = 10000
data = data[:max_examples]
labels = labels[:max_examples]

# Display some digits
def display(i):
	img = test_data[i]
	plt.title('Example %d. Label: %d' % (i, test_labels[i]))
	plt.imshow(img.reshape((28,28)), cmap=plt.cm.gray_r)

feature_columns = learn.infer_real_valued_columns_from_input(data)
classifier = learn.LinearClassifier(feature)