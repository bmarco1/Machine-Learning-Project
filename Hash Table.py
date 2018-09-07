#hash table, save the test set on the first run to be used in subsequent Runs

import hashlib

def test_set_check(identifier, test_ratio, hash):
    return hash(np.int64(identifier)).digest()[-1] < 256 *test_ratio

def split_train_test_by_id(data, test_ratio, id_column, hash=hashlib.md5):
    ids = data[id_column]
    in_test_set = ids.apply(lambda id_: test_set_check(id_, test_ratio, hash))
    return data.loc[~in_test_set], data.loc[in_test_set]
#Add an Index columsn, this will act as a unique identifier
housing_with_id =housing.reset_index()
train_set, test_set = split_train_test_by_id(housing_with_id, 0.2, "index")
#May also use a stable feature as the unique identifier, such as longitude/latitude
housing_with_id["id"] = housing["longitude"] * 1000 + housing["latitude"]
train_set, test_set = split_train_test_by_id(hosuing_with_id, 0.2, "id")

#scikit-learn provides functions to split a dataset
from sklearn.model_selection import train_split
train_set, test_set = train_test_split(housing, test_size=0.2, random_state=42)

#Break---

#Create an income category attribute
#This code divides the median income by 1.5 to limit the number of income categories

hosuing["income_cat"] = np.ceil(housing["median_income"]/ 1.5)
housing["income_cat"].where(housing["income_cat"] < 5, 5.0, inplace=True)

#Break---
