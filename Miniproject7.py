"""
Problem:

The given dataset contains ad budgets for different media channels and the corresponding ad sales of XYZ firm. Evaluate the dataset to:

Find the features or media channels used by the firm
Find the sales figures for each channel
Create a model  to predict the sales outcome
Split as training and testing datasets for the model
Calculate the Mean Square Error (MSE)
"""

#Import the required libraries

import pandas as pd

#Import the advertising dataset

df_advertising = pd.read_csv("Advertising.csv", index_col = 0)

#View the initial few records of the dataset

df_advertising.head()

#Check the total number of elements in the dataset

df_advertising.size

#Check the number of observations (rows) and attributes (columns) in the dataset

df_advertising.shape

#View the names of each of the attributes

df_advertising.columns

#Create a feature object from the columns

the_features = df_advertising[["TV Ad Budget ($)","Radio Ad Budget ($)","Newspaper Ad Budget ($)"]]

#View the feature object

the_features.head()

#Create a target object (Hint: use the sales column as it is the response of the dataset)

target = df_advertising[["Sales ($)"]]

#View the target object

target.head()

#Verify if all the observations have been captured in the feature object

the_features.shape

#Verify if all the observations have been captured in the target object

target.shape

#Split the dataset (by default, 75% is the training data and 25% is the testing data)

from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(the_features,target,random_state=1)

#Verify if the training and testing datasets are split correctly (Hint: use the shape() method)

print(x_train.shape)
print(y_train.shape)
print(x_test.shape)
print(y_test.shape)

#Create a linear regression model

from sklearn.linear_model import LinearRegression

linreg = LinearRegression()
linreg.fit(x_train,y_train)

#Print the intercept and coefficients 

print(linreg.intercept_)
print(linreg.coef_)

#Predict the outcome for the testing dataset

y_prediction = linreg.predict(x_test)
y_prediction

#Import required libraries for calculating MSE (mean square error)

import numpy as np
from sklearn import metrics

#Calculate the MSE

print(np.sqrt(metrics.mean_squared_error(y_test,y_prediction)))

#Compare the values of the y-test data and the y-predicted data

print("True",y_test.values[0:10])
print()
print("Pred",y_prediction[0:10])