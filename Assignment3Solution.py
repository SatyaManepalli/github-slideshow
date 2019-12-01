# -*- coding: utf-8 -*-
"""
Created on Thu Feb 14 22:59:00 2019

@author: Satya Manepalli
"""

import pandas as pd

#Compute sum of births of all names between between 1990 and 1999
years = range(1990,2000)
pieces = []
columns = ['name','sex','births']
for year in years:   
    path = 'C:/Users/Satya Manepalli/Desktop/names/yob%d.txt'%year
    frame = pd.read_csv(path,names=columns)    
    frame['year'] = year
    pieces.append(frame) 
#Concatenate into one DataFrame
alldata = pd.concat(pieces, ignore_index=True)
#print(alldata)

#extract M/F names into 2 separate dataframes
allmales= alldata[alldata['sex'] == 'M']
allfemales= alldata[alldata['sex'] == 'F']

#convert M/F dataframes into pivot tables
mpivot = pd.pivot_table(allmales,values='births',index=['name'],columns=['year'],aggfunc=sum,fill_value= 0)
fpivot = pd.pivot_table(allfemales,values='births',index=['name'],columns=['year'],aggfunc=sum,fill_value= 0)

#convert M/F pivot table back to dataframe
mdf = mpivot.reset_index()
fdf = fpivot.reset_index()
        
#compute the average and max births 
def avgMax(adf):
    adf2 = adf.copy()
    adf2 = adf2.set_index('name')
    adf2['Average'] = adf2.mean(numeric_only=True, axis=1)
    adf2['Max'] = adf2.idxmax(axis=1)
    return adf2

mdf2 = avgMax(mdf)
print("Male AvgMax Table: occurences/year, average occurances/year and year in which names were most common")
print(mdf2)
fdf2 = avgMax(fdf)
print("-----------------------------------------------------------------------------------------------")
print("Female AvgMax Table: occurences/year, average occurances/year and year in which names were most common")
print(fdf2)

#compute the difference between years
def difference(adf):
    adf3 = adf.copy()
    adf3 = adf3.set_index('name')
    adf3 = adf3.diff(axis=1)
    adf3['MaxDiff'] = adf3.idxmax(axis=1)
    return adf3

print("-----------------------------------------------------------------------------------------------")
mdf3 = difference(mdf)
print("Male Difference Table: change/year and year in which change was greatest")
print(mdf3)
fdf3 = difference(fdf)
print("-----------------------------------------------------------------------------------------------")
print("Female Difference Table: change/year and year in which change was greatest")
print(fdf3)