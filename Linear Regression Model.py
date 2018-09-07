#Linear Regrssion Model

>>>lin_scores = cross_val_score(lin_reg, housing_prepared, housing_labels, scoring="neg_mean_squared_error", cv=10)
>>>lin_rmse_scores  = np.sqrt(-lin_scores)
>>>display_scores(lin_rmse_scores)
