import libs
import pandas as pd

# main functions
data, label = libs.read_dataset("DoS_dataset.csv")
X_train, X_test, y_train, y_test = libs.traintest_split(data, label)

# convert hexa byte to decimal
X_train_decimal = libs.convert_hex_decimal(X_train)
X_test_decimal = libs.convert_hex_decimal(X_test)

# model DNN 



