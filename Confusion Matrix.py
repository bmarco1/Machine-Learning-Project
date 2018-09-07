#Confusion Matrix

from sklearn.model_selection import cross_val_predict
y_train_pred = cross_val_predict(sgd.clf, x_train, y_train_5, cv=3)

>>>from sklearn.metrics import confusion_matrix
>>>confusion_matrix(y_train_5, y_train_pred)

>>>confusion_matrix(y_train_5, y_train_perfect_predictions)             #See 87 for TP/FP Formulas

>>>from sklearn.metrics import precision_score, recall_score
>>>precision_score(y_train_5, y_train_pred)
