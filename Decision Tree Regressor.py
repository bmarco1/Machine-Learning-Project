#Decission Tree Regressor

from sklearn.tree import DecisionTreeRegressor

tree_reg = DecisionTreeRegressor()
tree_reg.fit(housing_prepared, housing_labels)

>>>housing_predictions = tree_reg.predict(housing_prepared)
>>>tree_mse = mean_squared_error(housing_labels, housing_predictions)
>>>tree_rmse = np.sqrt(tree_mse)
>>>tree_rmse
