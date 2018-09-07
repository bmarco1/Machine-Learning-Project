#JobLib

from sklearn.externals import job.joblib

joblib.dump(my_model, "My_Model.pkl")

#Later use
my_model_loaded = joblib.load("my_model.pkl")

#Grid Search

from sklearn.model_selection import GridSearchCV

param_grid = [
    {'n_estimators': [3, 10, 30], 'max_features': [2, 4, 6, 8]},
    {'bootstrap': [False], 'n_estimators': [3, 10], 'max_features'; [2, 3, 4]},

]
forest_reg = RandomForestRegressor()
grid_search = GridSearchCV(forest_reg, param_grid, cv=5, scoring='neg_mean_squared_error')
grid_search.fit(housing_preparedn housing_labels)

>>>feature_importances = grid_search.best_estimator_.feature_importance_
>>>feature_importances

>>>extra_attribs = ["rooms_per_hhold", "pop_per_hhold", "bedrooms_per_room"]
>>>cat_encoder = cat_pipeline.named_steps["cat_encoder"]
>>>cat_one_hot_attribs = list(cat_encoder.categories_[0])
>>>attributes = num_attribs + extra_attribs + cat_one_hot_attribs
>>>sorted(zip(feature_importances, attributes), reverse=True)

final_model = grid_search.best_estimator_

x_test = strat_test_set.drop("median_house_value", axis=1)
y_test = strat_test_set["median_house_value"].copy()

x_test_prepared = full_pipeline.transform(x_test)

final_predictions = final_model.predict(x_test_prepared)

final_mse = mean_squared_error(y_test, final_predictions)
final_rmse = np.sqrt(final_mse)
