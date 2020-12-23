import pandas as pd

melbourne_file_path = '../datasets/melb_data.csv'
melbourne_data = pd.read_csv(melbourne_file_path)
print(melbourne_data.columns)

# drops missing values, 0 = row, 1 = column
melbourne_data = melbourne_data.dropna(axis = 0)

# set price as the prediction target
y = melbourne_data.Price

# define the features
melbourne_features = ['Rooms', 'Bathroom', 'Landsize', 'Lattitude', 'Longtitude']

# features data in a dataframe
X = melbourne_data[melbourne_features]

print(X.describe())
print(X.head()) # prints the first 5 or n nodes

from sklearn.tree import DecisionTreeRegressor

# Define model. Specify a number for random_state to ensure same results each run
melbourne_model = DecisionTreeRegressor(random_state=1)

# Fit model
melbourne_model.fit(X, y)
print("Making predictions for the following 5 houses:")
print(X.head())
print("The predictions are")
print(melbourne_model.predict(X.head()))
