"""
Problem: 

Evaluate the dataset of the Summer Olympics, London 2012 to:

Find and print the name of the country that won maximum gold medals,
Find and print the countries who won more than 20 gold medals,
Print the medal tally,
Print each country name with the corresponding number of gold medals, and
Print each country's name with the total number of medals won.
"""

#Import the necessary library

import numpy as np

#Manually add the Summer Olympics, London 2012 dataset as arrays

olympic_country = np.array(["GBR","CHN","RUS","US","KOR","JPN","GER"])
olympic_country_gold = np.array([29,38,24,46,13,7,11])
olympic_country_silver = np.array([17,28,25,28,8,14,11])
olympic_country_bronze = np.array([19,22,32,29,7,17,14])

# Find the country with maximum gold medals: Use the argmax() method to find the highest number of gold medals

max_gold_medal = olympic_country_gold.argmax()
max_gold_country = olympic_country[max_gold_medal]

#Print the name of the country

print(max_gold_country)

# Find the countries with more than 20 gold medals: Use Boolean indexing technique to find the required output

print(olympic_country[olympic_country_gold>20])

# Evaluate the dataset and print the name of each country with its gold medals and total number of medals:
# Use a for loop to create the required output

for i in range(len(olympic_country)):
    number_of_gold_medals = olympic_country_gold[i]
    country = olympic_country[i]
    total_medals = olympic_country_gold[i] + olympic_country_silver[i] + olympic_country_bronze[i]
    print("{}, gold medals {}, Total medals {}".format(country,number_of_gold_medals,total_medals))



