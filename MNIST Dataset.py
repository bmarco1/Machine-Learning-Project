#MNIST dataset

>>>from sklearn.datasets import fetch_mldata
>>>mnist = fetch_mldata('MNIST original')
>>>mnist

>>>x, y =mnist["data"], mnist["target"]
>>>X.shape
>>>y.shape

%matplot inline
import matplotlib
import matplotlib.pyplot as plt

some_digit = x[36000]
some_digit_image = some_digit.reshape(28, 28)

plt.imshow(some_digit_image, cmap=matplotlib.cm.binary, interpolation="nearest")
plt.axis("off")
plt.show()

>>>y[36000]

import numpy as np

shuffle_index = np.random.permutation(60000)
x_train, y_train = x_train[shuffle_index], y_train[shuffle_index]
