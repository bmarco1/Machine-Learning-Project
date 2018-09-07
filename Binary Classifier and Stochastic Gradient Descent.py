#Binary Classifier

y_train_5 = (y_train == 5)
y_test_5 = (y_test == 5)

#Stochastic Gradient Descent

from sklearn.linear_model import SGDClassifier

sgd_clf = SGDClassifier(random_state=42)
sgd_clf.fit(x_train, y_train_5)

>>>sgd_clf.predict([some_digit])
