"""
Problem

A dataset in CSV format is given for the Fire Department of New York City. Analyze the dataset to determine:

The total number of fire department facilities in New York city
The number of fire department facilities in each borough
The facility names in Manhattan
"""

#Import the required libraries

import pandas as pd

#Import the Fire Department of New York City (FDNY) file

df_FDNYC = pd.read_csv("FDNY.csv")

#View the content of the data

df_FDNYC

#View the first five records

df_FDNYC.head()

#Skip the duplicate header row

df_FDNYC = pd.read_csv("FDNY.csv",skiprows = 1)

#Verify if the dataset is fixed

df_FDNYC

#View the data statistics (Hint: use describe() method)

df_FDNYC.describe()

#View the attributes of the dataset (Hint: view the column names)

df_FDNYC.columns

#View the index of the dataset

df_FDNYC.index

#Count number of records for each attribute

df_FDNYC.count()

#view the datatypes of all three attributes

df_FDNYC.dtypes

#Select FDNYC information boroughwise

borough = df_FDNYC.groupby("Borough")

#View FDNYC informationn for each borough

borough.size()

#Select FDNYC information for Manhattan

info_Manhattan = borough.get_group("Manhattan")

#View FDNY information for Manhattan

info_Manhattan