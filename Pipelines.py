#Create a  pipeline for numerical attributes
#Pipeline constrictor takes a list of name/estimator pairs to define a sequence of steps. All but the last estimator must be transformers

from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler

num_pipeline = Pipeline([
        ('imputer', Imputer(strategy="median")),
        ('attribs_adder', CombinedAttributesAdder()),
        ('std_scaler', StandardScaler()) #transformer
])

housing_num_tr = num_pipeline.fit-transform(housing_num)

#Break---

#Custom tranormer that allows us to feed the PandasDataFrame containing non-numerical colums directly into the Pipeline

from sklearn.base import BaseEstimator, TransformerMixin

class DataFrameSelector(BaseEstimator, TransformerMixin):       #selecs the desired attributes, dropping the rest, and converts the resulting dataframe to a NumPy arrray
    def __init__(self, attrbute_names):
        self.attribute_names = attribute_names
    def fit(self, X, y=None):
        return self
    def transform(self, X):
        return X[self.attribute_names].values

#Break---

#Create a pipeline for catergorical attributes

num_attribs = list(housing_num)
cat_attribs = ["ocean_proximity"]

num_pipeline = Pipeline([
        ('selector', DataFrameSelector(num_attribs)),
        ('imputer', Imputer(strategy="median")),
        ('attribs_adder', CombinedAttributesAdder()),
        ('std_scaler', StandardScaler()),
])

cat_pipeline = Pipeline([
        ('selector', DataFrameSelector(cat_attribs)),
        ('cat_encoder', CategoricalEncoder(encoding="onehot-dense")),
])

#Full pipeline, joining the two scripted above using FeatureUnion

from sklearn.pipeline import FeatureUnion

full_pipeline = FeatureUnion(transformer_list=[
        ("num_pipeline", num_pipeline)
        ("cat_pipeline", cat_pipeline)
])

>>>housing_prepared = full_pipeline.fit_transform(housing)
>>>housing_prepared

#Break---

from sklearn.linear_model import Linear_Regression

lin_reg = Linear_Regression()
lin_reg.fit(housing_prepared, housing_labels)

>>>some_data = housing.iloc[:5]
>>>some_labels = housing_labels.iloc[:5]
>>>some_data_prepared = full_pipeline.transform(some_data)
>>>print("labels", list(some_labels))

>>>from sklearn.metrics import mean_squared_error
>>>housing_predictions = lin_reg.predict(housing_prepared)
>>>lin_mse = mean_squared_error(housing_labels, housing_predictions)
>>>lin_rmse = np.sqrt(lin_mse)
>>>lin_rmse   #prediction error
