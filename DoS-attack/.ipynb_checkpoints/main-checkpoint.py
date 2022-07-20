import libs
import pandas as pd

# variable 
PATH_TO_DATASET = '/mnt/d/project/dataset/CAN/Car-Hacking/DoS_dataset.csv'

# main functions
data, label = libs.read_dataset(PATH_TO_DATASET)
X_train, X_test, y_train, y_test = libs.traintest_split(data, label)

# convert hexa byte to decimal
X_train_decimal = libs.convert_hex_decimal(X_train)
X_test_decimal = libs.convert_hex_decimal(X_test)

# model DNN 



