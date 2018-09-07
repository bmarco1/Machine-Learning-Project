#Cross Validation

from sklearn.model_selection import StratfiedKFold
from sklearn.base import clone

skfolds = StratifiedKFold(n_splits =3, random_state = 42)

for train_index, test_index in skfolds.split(x_train, y_train_5):
    clone_clf = clone(sgd_clf)
    x_train_folds = x_train[train_index]
    y_train_folds = y_train_5[train_index]
    x_test_fold = x_train[test_index]
    y_test_fold = y_train_5[test_index]

    clone_clf.fit(x_train_folds, y_train_folds)
    y_pred = clone_clf.predict(x_test_fold)
    n_correct = sum(y_pred == y_test_fold)
    print(n_correct / len(y_pred))

>>>from sklearn.model_selection import cross_val_score
>>>cross_val_score(sgd.clf, x_train, y_train_5, cv=3, scoring="accuracy")

from sklearn.Base import BaseEstimator

class Never5Classifier(BaseEstimator):
    def fit(self, x, y=None):
        pass
    def predict(self, x):
        return np.zeros((len(x), 1), dtype=bool)

>>>never_5_clf = Never5Classifier()0000
>>>cross_val_score(never_5_clf, x_train, y_train_5, cv=3, scoring="accuracy")
