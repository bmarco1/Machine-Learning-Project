Visualixe the Data
#Create a copy of the training set, so we don't screw it all up :)

housing = strat_train_set.copy()

#Create a geographical scatter plot with long/lat. Use an alpha = 0.1 to make the highly dense population areas more noticeable

housing.plot(kind="scatter", x="longitude", y="latitiude", alpha=0.1)

#Investigate housing prices

housing.plot(kind="scatter", x="longitude", y="latitude", alpha=0.4, s=housing["population"] / 100, label="population", figsize=(10,7), c="median_house_value", cmap=plt.get_cmap("jet"), colorbar=True,)
plt.legend()

#Break---

#Correlation Coefficient

corr_matrix = housing.corr()

#Break---

# Another way to check for correlations

from pandas.plotting import scatter_matrix

attributes = ["median_house_value", "median_income", "total_rooms", "housing_median_age"]
scatter_matrix(housing[attributes], figsize=(12, 8))

#Zoom in on the most important correlation from above

housing.plot(kind="scatter", x="median_income", y="median_house_value", alpha=0.1)

>>>corr_matrix = housing.corr()
>>>corr_matrix["median_house_value"].sort_values(ascending=False)

#Break---

#Attribute Combinations

housing["rooms_per_housholds"] = housing["total_rooms"/housing"households"]
housing["bedrooms_per_room"] = housing["total_bedrooms"/housing"total_rooms"]
housing["population_per_housholds"] = housing["population"/housing"households"]

#Get back to a clean set of data before Data Cleaning

housing = strat_train_set.drop("median_house_value", axis=1)
housing_labels = strat_train_set["median_house_value"].copy()
housing["total_bedrooms"].fillna.(median, inplace=True)    #????????? Out of Place
