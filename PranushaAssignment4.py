# -*- coding: utf-8 -*-
"""
Created on Sat Feb 16 14:50:59 2019

@author: Satya Manepalli
"""

import pandas as pd
import numpy as np
#Read the data and create the Dataframe from all years 
years = range(1990,2000)
pieces = []
columns = ['name','sex','births']
for year in years:
    path = 'C:/Users/Satya Manepalli/Desktop/names/yob%d.txt'%year
    frame = pd.read_csv(path,names=columns)    
    frame['year'] = year
    pieces.append(frame) 
#Concatenate into one DataFrame
names = pd.concat(pieces, ignore_index=True)
print(names)


subsetDataFrame1 = names[names['sex'] == 'M']
#print the list of all unique boy names 
uniq_boys = subsetDataFrame1['name'].unique()
print(uniq_boys)

subsetDataFrame2 = names[names['sex'] == 'F']
#print the list of all unique girl names 
uniq_girls = subsetDataFrame2['name'].unique()
print(uniq_girls)

#print the number of occurrences for each name for each year for boys

frequency_boys= subsetDataFrame1.groupby(['name','year'])['births'].sum()
print(frequency_boys) 

#print the number of occurrences for each name for each year for girls

frequency_girls= subsetDataFrame2.groupby(['name','year'])['births'].sum()
print(frequency_girls)


#print the average number of times each boy name occurred over the decade

avg_boys= subsetDataFrame1.groupby(['name'])['births'].mean()
print(avg_boys)


#print the average number of times each girl name occurred over the decade

avg_girls= subsetDataFrame2.groupby(['name'])['births'].mean()
print(avg_girls)


frequency_boys_df = frequency_boys.to_frame().reset_index()

frequency_girls_df= frequency_girls.to_frame().reset_index()

# print the year in which it was most common , for each boy name 

common_boys=(frequency_boys_df.sort_values(['name', 'births'], ascending=[True, False]).drop_duplicates(['name']).reset_index(drop=True))
print(common_boys)

# print the year in which it was most common , for each girl name 

common_girls=(frequency_girls_df.sort_values(['name', 'births'], ascending=[True, False]).drop_duplicates(['name']).reset_index(drop=True))
print(common_girls)

#Print For each boy name, find the year in which it showed the greatest change from the previous year.

frequency_boys_df ['value_diff'] = frequency_boys_df.groupby('name')['births'].diff().fillna(0)
print(frequency_boys_df.loc[frequency_boys_df.groupby(['year','name'])['value_diff'].idxmax()])

#Print For each girl name, find the year in which it showed the greatest change from the previous year.

frequency_girls_df ['value_diff'] = frequency_girls_df.groupby('name')['births'].diff().fillna(0)
print(frequency_girls_df.loc[frequency_girls_df.groupby(['year','name'])['value_diff'].idxmax()])