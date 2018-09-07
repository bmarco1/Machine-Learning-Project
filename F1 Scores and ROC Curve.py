#F1-Scores

>>>from sklearn.metrics import f1_score
>>>f1_score(y_train_5, y_train_pred)

>>>y_score = sgd_clf.decision_function([some_digit])
>>>y_scores
>>>threshold = 0
>>>y_some_digit_pred = (y_scores > threshold)

#ROC Curve
from sklearn.metrics import roc_curve(fpr, tpr, label=None)

fpr, tpr, thresholds = roc_curve(y_train_5, y_scores)
#FRP against the tpr
def plot_roc_curve(fpr, tpr, label=None):
    plt.plot(fpr, tpr, linewidth=2, label=label)
    plt.plot([0, 1], [0, 1], 'k--')
    plt.axis([0, 1, 0, 1])
    plt.xlabel('False Positive Rate')
    plt.ylabel('True Positive Rate')

plot_roc_curve(fpr, tpr)
plt.show()

ROC accuracy

>>>from sklearn.metrics import roc_auc_score
>>>roc_auc_score(y_train_5, y_scores)
