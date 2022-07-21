import libs
import pandas as pd
import model_lib
from pathlib import Path

# variable 
PATH_TO_DATASET = '/mnt/d/project/dataset/CAN/Car-Hacking/DoS_dataset.csv'

# main functions
data, label = libs.read_dataset(PATH_TO_DATASET)
X_train, X_test, y_train, y_test = libs.traintest_split(data, label)

# convert hexa byte to decimal
X_train_decimal = libs.convert_hex_decimal(X_train)
X_test_decimal = libs.convert_hex_decimal(X_test)

# output X_train, X_test, y_train, y_test to csv file 
filepath_train = Path('./out/train.csv')
filepath_train.parent.mkdir(parents=True, exist_ok=True)
X_train.to_csv(filepath_train)

filepath_test = Path('./out/test.csv')
filepath_test.parent.mkdir(parents=True, exist_ok=True)
X_test.to_csv(filepath_test)

filepath_train_label = Path('./out/train_label.csv')
filepath_train_label.parent.mkdir(parents=True, exist_ok=True)
X_train.to_csv(filepath_train_label)

filepath_test_label = Path('./out/test_label.csv')
filepath_test_label.parent.mkdir(parents=True, exist_ok=True)
X_test.to_csv(filepath_test_label)

