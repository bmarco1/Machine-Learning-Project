#Begin Data Cleaning, get rid of corresponding districts, get rid of whole attributes, set values
    #Option 1: housing.dropna(subset=["total_bedrooms"])
    #Option 2: housing.drop("total_bedrooms", axis=1)
    #Option 3: median=housing ["total_bedrooms"].median()
    # housing["total_bedrooms"].fillna(median, inplace = True)

#Use Sci-scikit to replace missing values in the test set, Option 3

from sklearn.preprocessing import Imputer
imputer = Imputer(strategy="median")                      #the imputer computes the median of each attribute, also known as an estimator
housing_num = housing.drop("ocean_proximity", axis=1)     #We need to drop ocean_proximity since the median can only be computed in numerical attributes
imputer.fit(housing_num)

x = imputer.transform(housing_num)                        #Use the "trained" imputer to transform the training set. Replacing the missing values
housing_tr = pd.DataFrame(X, colums=housing_num.columns)        #to return to Pandas DataFrame, Optional

#Break---

#to change ocean_proximity into a numeric value if we didn't use the Imputer

>>>housing_cat = housing["ocean_proximity"]
>>>housing_cat.head(10)

#Convert all tect categories to numbers using Pandas factorize()

>>>housing_cat_encoded, housing_categories = housing_cat.factorize()
>>>housing_cat_encoded[:10]
>>>housing_categories

#Break---

#Converet interger categorical values into one-hot vectors. Only one attribute will be 1 or 0, hot or cold

>>>from sklearn.preprocessing import OneHotEncoder     #For CategoricalEncoder p.65
>>>encoder = OneHotEncoder()
>>>housing_cat_1hot = encoder.fit_transform(housing_cat_encoded.reshape(-1,1))
>>>housing_cat_1hot
>>>housing_cat_1hot.toarray()

>>>cat_encoder.categories_

#Break---
