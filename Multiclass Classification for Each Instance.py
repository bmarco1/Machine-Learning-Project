#Multiclass Classification for each instance

from sklearn.neighbors import KNeighborsClassifier

y_train_large = (y_train >=7)
y_tran_odd = (y_train % 2 == 1)
y_multilabel = np.c_[y_train_large, y_tran_odd]

knn_clf = KNeighborsClassifier()
knn_clf.fit(x_train, y_multilabel)

#this creates an array containing two target labels. THe first, indicates how large the digit is (7, 8, 9). The second, indicated whether or not the digit is oddself.
#Now we can make a prediction

>>>knn_clf.predict([some_digit])

#We can also measure the average F score with the following code
>>>y_train_knn_pred = cross_cal_predict(knn_clf, x_train, y_multilabel, cv=3)
>>>f1_score(y_multilabel, y_train_knn_pred, average="macro")            #To gove each label a weighted equal to it's support (the number of instances with that target label) set the average = "weighted"

#Multioutput classification is a generalization of multilabel classification where each label can be Multiclass

noise = np.random.randint(0, 100, (len(x_train), 784))
x_train_mod = x_train + noise
noise = np.random.randint(0, 100, (len(x_trst), 784))
x_test_mod = x_test + noise
y_train_mod = x_train
y_test_mod = x_test

#Clean target image

knn_clf.fit(x_train_mod, y_train_mod)
clean_digit = knn.clf.predict([x_test_mod[some_index]])
plot_digit(clean_digit)

#Break
