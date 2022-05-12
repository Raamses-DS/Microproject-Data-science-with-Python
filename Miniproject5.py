"""
Problem:

Analyze the Federal Aviation Authority (FAA) dataset using Pandas to do the following:

View
aircraft make name
state name
aircraft model name
text information
flight phase
event description type
fatal flag

2. Clean the dataset and replace the fatal flag NaN with “No”

3. Find the aircraft types and their occurrences in the dataset

4. Remove all the observations where aircraft names are not available

5. Display the observations where fatal flag is "Yes".
"""


import numpy as np
import pandas as pd

df_Aviation = pd.read_csv("faa_ai_prelim.csv")
print(df_Aviation)

#View the dataset shape

df_Aviation.shape

#View the first five observations

df_Aviation.head()

#View all the columns present in the dataset

df_Aviation.columns

#Create a new dataframe with only the required columns: Aircraft make name, State name , Aircraft model name , 
# Text information , Flight phase , Event description type ,Fatal flag.


new_df_Aviation = df_Aviation[["ACFT_MAKE_NAME","LOC_STATE_NAME","ACFT_MODEL_NAME","RMK_TEXT","FLT_PHASE",
                               "EVENT_TYPE_DESC","FATAL_FLAG"]]

#View the type of the object

type(new_df_Aviation)

#Check if the dataframe contains all the required attributes

new_df_Aviation

#Replace all Fatal Flag missing values with the required output

new_df_Aviation["FATAL_FLAG"].fillna(value = "No", inplace=True)

#Verify if the missing values are replaced

new_df_Aviation

#Check the number of observations

new_df_Aviation.shape[0]

#Drop the unwanted values/observations from the dataset

print(new_df_Aviation['ACFT_MAKE_NAME'].isnull().values.any())

final_df_Aviation = new_df_Aviation.dropna(subset = ["ACFT_MAKE_NAME"])
final_df_Aviation

#Check the number of observations now to compare it with the original dataset and see how many values have been dropped

final_df_Aviation.shape

#Group the dataset by aircraft name

df_aircraft = final_df_Aviation.groupby("ACFT_MAKE_NAME")
df_aircraft
#Group the dataset by fatal flag

df_accidents = final_df_Aviation.groupby("FATAL_FLAG")
df_accidents

#View the total number of fatal and non-fatal accidents

df_accidents.size()

#Create a new dataframe to view only the fatal accidents (Fatal Flag values = Yes)

df_accidents_with_deaths = df_accidents.get_group("Yes")
df_accidents_with_deaths