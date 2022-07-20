# import libraries 
import pandas as pd 
import numpy as np 
from sklearn.model_selection import train_test_split

# function to read dataset
def read_dataset(path_to_dataset):
    # read file DoS_dataset.csv
    df = pd.read_csv(str(path_to_dataset), header=None)
    # drop timestamp 
    df.drop([0], axis=1, inplace=True)
    # remove nan 
    df = df.dropna(axis=0)
    # drop data length column
    df.drop([2], axis=1, inplace=True)
    # label 
    label = df[11]
    # data
    data = df.loc[:,:10]
    return data, label

# function to split dataset
def traintest_split(data, label):
    X_train, X_test, y_train, y_test = train_test_split(data, label, test_size=0.2)
    return X_train, X_test, y_train, y_test

# function to convert hexa elements to decimal elements in a set 
def convert_hex_decimal(_set_before_convert):
    _set_after_convert = pd.DataFrame()
    for i in _set_before_convert:
        firstlist = []
        for j in _set_before_convert[i]:
            _list = firstlist.append(int(j, 16))
        _set_after_convert[i] = firstlist 
    return _set_after_convert




