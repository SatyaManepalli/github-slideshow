# -*- coding: utf-8 -*-
"""
Created on Mon Feb  4 07:04:46 2019

@author: Satya Manepalli
"""
import pandas as pd
from functools import reduce
years = range(1880,2018)
pieces = []
columns = ['name','sex','births']
for year in years:
    path = 'C:/Users/Satya Manepalli/Desktop/names/yob%d.txt'%year
    frame = pd.read_csv(path,names=columns)    
    frame['year'] = year
    pieces.append(frame) 
#Concatenate into one DataFrame
names = pd.concat(pieces, ignore_index=True)
#making the data usable by getting it into a spreadsheet kind of table (pivote table)
total_births = names.pivot_table('births',index=['year', 'name'],columns='sex', aggfunc=sum)
#dropping the nul values by using dropna
total_births = total_births.dropna(axis = 0, how ='any')
#finding the minimum of F births and M births
print(total_births[['F','M']].min(axis=1))
#finding the frequency of names each year by using groupby() and count()
frequency_of_Names=total_births.groupby('year').count()
#plotting the graph by passing names count and years as arguments in x and y axes
frequency_of_Names.plot(title='Frequency of Common Names',
   yticks=range(0, 5000, 500), xticks=range(1880, 2017, 10))

"""print(total_births)"""
#another data frame for female names
"""print(frame.loc[frame['sex'] == 'F'])
pieces1 = []
for names in years:
    frame1 = pd.read_csv(path,names=columns)    
    frame1['year'] = year
    pieces1.append(frame) 
#Concatenate into one DataFrame
names = pd.concat(pieces, ignore_index=True)
names = frame.loc[frame['sex'] == 'M']
print(names)"""
#intersection of colums in two data frames
"""print(set(frame['name']).intersection(set(frame1['name'])))"""




