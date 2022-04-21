import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

import seaborn as sns

from scipy import stats


"""OBJECTIVE:  This project help to establish a linear regression model to predict the graduation rate in Michigan"""
# load data and drop the name of institutes:
data = pd.read_excel("graduation_rate.xlsx")
data = data.drop(columns= "Inst")

print(data.dtypes)
print(data.head())
data_stats = data.describe()

# get the predictors x and the prediction y:
x = data.iloc[:, :-1]
y = data.iloc[:, -1]

name_x = x.columns
print("predictors are: ", name_x)

# Plot data:
plt.figure("Hist: enrollment")
sns.distplot(data[name_x[0]], kde= False).set_title("Number of enrollment")
plt.figure("Boxplot: enrollment")
sns.boxplot(data[name_x[0]]).set_title("Number of enrollment")


# number of data points:
n = data.shape[0] - 1

#number of independent varables:
beta = data.shape[1] - 2

print("There are {0} independent variables and {1} observations".format(beta, n))

# checking missing values:
# num_missing = data.columns[data.isnull().any()]

num_missing = data.isnull().sum().sum()
print("There are {0} observations has missing values".format(num_missing))

"""Data statistic: """