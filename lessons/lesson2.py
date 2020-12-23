# Lesson 1: How Models Work
# Using Pandas to get Familiar with Data

# we want to use DataFrame, which is like a table in excel
import pandas as pd

# file path of the dataset
melbourne_fp = '../datasets/melb_data.csv'

# turn csv into a DataFrame
melbourne_data = pd.read_csv(melbourne_fp)

print(melbourne_data.describe())
