#Create a random forest Classifier

from sklearn.ensemble import RandomForestClassifier

forest_clf = RandomForestClassifier(random_state=42)
y_probas_forest = cross_val_predict(forest_clf, x_train, y_train_5, cv=3, method="predict_proba")

#To create a ROC curve you must have scores, not probabilities. Thus use the positive class's probability as the score.

y_scores_forest = y_probas_forest[:, 1]   #score = proba of positive class
fpr_forest, tpr_forest, thresholds_forest = roc_curve(y_train_5, y_scores_forest)

#Plot the roc curve

plt.plot(fpr, tpr, "b:", label="SGD")
plot_roc_curve(fpr_forest, tpr_forest, "Radnom Forest")
plt.legend(loc="lower right")
plt.show()

>>>roc_auc_score(y_train_5, y_score_forest)

#Break
