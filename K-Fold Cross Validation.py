#K-Fold Cross Validation

from sklearn.model_selection import cross_val_score
scores = cross_val_score(tree_reg, housing_prepared, housing_labels, scoring="neg_mean_squared_error", cv=10)
tree_rmse_scores = np.sqrt(-scores)

>>>def display_scores(scores):
        print("Scores:", scores)
        print("Mean:", mean())
        print("Standard Deviation:", scores.std())
>>>display_scores(tree_rmse_scores)
