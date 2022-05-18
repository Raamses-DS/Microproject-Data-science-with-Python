"""
Problem:

The given dataset lists the glucose level readings of several pregnant women taken either during a survey examination or routine medical care. It specifies if the 2-hour post-load plasma glucose was at least 200 mg/dl. Analyze the dataset to:

Find the features of the dataset,
Find the response label of the dataset,
Create a model  to predict the diabetes outcome,
Use training and testing datasets to train the model, and
Check the accuracy of the model.
"""

#Import the required libraries

import pandas as pd

#Import the diabetes dataset

df_diabetes = pd.read_csv("pima-indians-diabetes.data",header=None)

#View the first five observations of the dataset

df_diabetes.head()

#Use the .NAMES file to view and set the features of the dataset

features_names = ["Number of times pregnant","Plasma glucose concentration","Diastolic blood pressure (mm Hg)",
                 "Triceps skin fold thickness (mm)","2-Hour serum insulin (mu U/ml)","Body mass index (weight in kg/(height in m)^2)",
                  "Diabetes pedigree function","Age (years)","Class variable (0 or 1)"]

#Use the feature names set earlier and fix it as the column headers of the dataset

df_diabetes = pd.read_csv("pima-indians-diabetes.data",header=None,names=features_names)

#Verify if the dataset is updated with the new headers

df_diabetes.head()

#View the number of observations and features of the dataset

df_diabetes.shape

#Select features from the dataset to create the model

the_features = ["Number of times pregnant","2-Hour serum insulin (mu U/ml)",
                           "Body mass index (weight in kg/(height in m)^2)","Age (years)"]

#Create the feature object

x_feature = df_diabetes[the_features]

#Create the reponse object

target = df_diabetes["Class variable (0 or 1)"]

#View the shape of the feature object

x_feature.shape

#View the shape of the target object

target.shape

#Split the dataset to test and train the model

from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x_feature,target,random_state=1)

# Create a logistic regression model using the training set

from sklearn.linear_model import LogisticRegression
LR = LogisticRegression()
LR.fit(x_train,y_train)

#Make predictions using the testing set

y_prediction = LR.predict(x_test)

#Evaluate the accuracy of your model

from sklearn import metrics
metrics.accuracy_score(y_test,y_prediction)

#Print the first 30 actual and predicted responses

print("Actual",y_test.values[0:30])
print("Predicted",y_prediction[0:30])