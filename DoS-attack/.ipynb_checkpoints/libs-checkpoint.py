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
    data = df.loc[:,3:10]
    return data, label

def traintest_split(data, label):
    X_train, X_test, y_train, y_test = train_test_split(data, label, test_size=0.2)
    return X_train, X_test, y_train, y_test

# convert each element in dataframe from str to byte
def str_to_byte(original_dataframe):
    new_dataframe = newPandasDataframe(original_dataframe)

    
    new_dataframe = 1
    return new_dataframe

# create a new pandas dataframe 
def newPandasDataframe(original_pandas_dataframe):
    index = original_pandas_dataframe.index
    columns = original_pandas_dataframe.columns
    new_dataframe = pd.DataFrame(index = index, columns = columns)
    # new_dataframe = new_dataframe.fillna(0)
    return new_dataframe

