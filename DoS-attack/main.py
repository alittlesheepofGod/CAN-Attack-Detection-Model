import libs
import pandas as pd
import model_lib
from pathlib import Path

# variable 
# PATH_TO_DATASET = '/mnt/d/project/dataset/CAN/Car-Hacking/DoS_dataset.csv'
PATH_TO_DATASET = '~/dataset/DoS_dataset.csv'

# main functions
data, label = libs.read_dataset(PATH_TO_DATASET)
X_train, X_test, y_train, y_test = libs.traintest_split(data, label)

# convert hexa byte to decimal
X_train_decimal = libs.convert_hex_decimal(X_train)
X_test_decimal = libs.convert_hex_decimal(X_test)

# reset index for X_train_decimal, X_test_decimal 
X_train_decimal = X_train_decimal.reset_index(drop=True)
X_test_decimal = X_test_decimal.reset_index(drop=True)
# reset index for y_train, y_test
y_train = y_train.reset_index(drop=True)
y_test = y_test.reset_index(drop=True)

# concatenate X_train_decimal and y_train 
X_train_stack = pd.concat([X_train_decimal, y_train], axis=1)
# concatenate X_test_decimal and y_test
X_test_stack = pd.concat([X_test_decimal, y_test], axis=1)

# rename features for X_train_stack and X_test_stack 
# rename features into feature0, feature1, ..., feature10
X_train_stack = X_train_stack.rename(columns={1:'feature0', 3:'feature1', 4:'feature2', 5:'feature3', 6:'feature4', 7:'feature5', 8:'feature6', 9:'feature7', 10:'feature8', 11:'label'})
X_test_stack = X_test_stack.rename(columns={1:'feature0', 3:'feature1', 4:'feature2', 5:'feature3', 6:'feature4', 7:'feature5', 8:'feature6', 9:'feature7', 10:'feature8', 11:'label'})

# change label value : R-normal message : 0 and T-injected message : 1 
X_train_stack['label'] = X_train_stack['label'].replace('R', 0)
X_train_stack['label'] = X_train_stack['label'].replace('T', 1)
X_test_stack['label'] = X_test_stack['label'].replace('R', 0)
X_test_stack['label'] = X_test_stack['label'].replace('T', 1)

# # output X_train, X_test, y_train, y_test to csv file 
# filepath_train = Path('./out/train.csv')
# filepath_train.parent.mkdir(parents=True, exist_ok=True)
# X_train_stack.to_csv(filepath_train)

# filepath_test = Path('./out/test.csv')
# filepath_test.parent.mkdir(parents=True, exist_ok=True)
# X_test_stack.to_csv(filepath_test)

