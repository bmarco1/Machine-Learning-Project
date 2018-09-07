#Custom transformers
#Create the following: fit(), transform(), or fit_transform()
#Combines previously used attributes

from sklearn.base import BaseEstimator, TransformerMixin            #BaseEstimator allows for 2 extra methods (get_params(), and set_params())

rooms_ix, bedrooms_ix, population_ix, household_ix = 3, 4, 5, 6

class CombinedAttributesAdder(BaseEstimator, TransformerMixin):
    def __init__(self, add_bedrooms_per_room = True):               #add_bedrooms_per_room acts as the hyperparameter, thus allowing us to determine if this attribute helps the machine learning algorithm
        self.add_bedrooms_per_room = add_bedrooms_per_room
    def fit(self, y=None):
        return self
    def transform(self, x, y=None):
        rooms_per_houshold = x[:, rooms_ix] / x[:, household_ix]
        population_per_houshold = x[:, population_ix] / x[:, household_ix]
        if self.add_bedrooms_per_room:
            bedrooms_per_room = x[:, bedrooms_ix] / x[:, rooms_ix]
            return np.c_[x, rooms_per_houshold, population_per_houshold, bedrooms_per_room]
        else:
            return np.c_[x, rooms_per_houshold, population_per_houshold]

attr_addr = CombinedAttributesAdder(add_bedrooms_per_room=False)
housing_extra_attribs = attr_addr.transform(housing.values)

#Break---
