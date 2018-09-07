#Break---

#Histogram plot
#Shows the number of instances that have a given range

%matplot inline
import matplotlib.pyplot as plt
housing.hist(bins=50, figsize=(20,15))
plt.show()

#Break---

#Creating a test set
#Typically set aside 20% of the dataset

import numpy as np
def split_train_test(data, test_ratio):
    shuffled_indices = np.random.permutation(len(data)) #random number generator
    test_set_size = int(len(data) * test_ratio)
    test_indices = shuffled_indices[:test_set_size]
    train_indices = shuffled_indices[test_set_size:]
    return data.iloc[train_indices], data.iloc[test_indices]
#Use the function
>>>train_set, test_set = split_train_test(housing, 0.2)
>>>print (len(train_set), "train +", len(test_set), "test")
16512 train + 4128 test
