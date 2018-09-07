#Begin Stratified Sampling

from sklearn.model_selection import StratifiedShuffleSplit

split = StratifiedShuffleSplit(n_splits=1, test_size=0.2, random_state=42)
for train_index, test_index in split.split(housing, housing["income_cat"]):
    strat_train_set = housing.loc[train_index]
    strat_test_set = housing.loc[test_index]
#Use the function
>>>strat_test_set["income_cat"].value_counts() / len(strat_test_set)

#Break---

#Because the sample income distribution is identical to the full dataset, we cane remove the income_cat to restore the dataset to it's original state

for set_in (strat_train_set, strat_test_set):
    set_.drop ("income_cat", axis=1, inplace=True)

#Break---
