#Multiclass Classification (Random Forests, naive Bayes)

#Test the detection of one-versus-all scikit Classifier

>>> sgd_clf.fit(x_train, y_train)
>>> sgd_clf.predict([some_digit])

#Break

#Use the decision_function() to return all 10 scores, not just 1

>>>some_digit_scores = sgd_clf.decision_function([some_digit])
>>>some_digit_scores

>>>np.argmax(some_digit_scores)
>>>sgd_clf.classes_
>>>sgd_clf.classes_[5]

#Break

#ScikitLearn can also be told which classifer to use with: OneVsOneClassifier, or OneVsRestClassifier

>>>from sklearn.Multiclass import OneVsOneClassifier
>>>ovo_clf = OneVsOneClassifier(SGDClassifier(random_state = 42))
>>>ovo_clf.fit(x_train, y_train)
>>>ovo_clf.predict([some_digit])
>>>len(ovo_clf.estimators_)

#Use this to train the RandomForestClassifier

>>>forest_clf.fit(x_train, y_train)
>>>forest_clf.predict({some_digit})

#call predict_proba() to get the list of possibilities that the classifier assigned to each instance of each class

>>>forest_clf.predict_proba([some_digit])

#now evaluate the classifier with crossvalidation

>>>cross_val_score(sgd_clf, x_train, y_train, cv=3, scoring="accuracy")

#Try scaling the inputs to improve accuracy

>>>from sklearn.preprocessing import StandardScaler
>>>scaler=StandardScaler()
>>>x_train_scaled = scaler.fit_transform(x_train.astype(np.float(64))
>>>cross_val_score(sgf_clf, x_train_scaled, y_train, cv=3, scoring="accuracy")

#Break
