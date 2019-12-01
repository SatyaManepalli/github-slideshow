# -*- coding: utf-8 -*-
"""
Created on Tue Feb 26 11:38:12 2019

@author: Satya Manepalli
"""

import pandas as pd
import warnings
warnings.filterwarnings("ignore", category=FutureWarning)
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
#dataframe with unique values
names['name'].unique()
girlNames = names.loc[names['sex'] == "F"]
boyNames = names.loc[names['sex'] == "M"]
#printing male names and female names
print (girlNames)
print (boyNames)
print (boyNames[['year', 'name','sex', 'births']])
print (girlNames[['year', 'name','sex', 'births']])
#finding the mean value
print (names.groupby(['name'])['births'].mean())
#print (names.groupby('name', as_index=False)['births'].mean())

Count_boys = boyNames.groupby(['name','year'])['births'].sum()
print(Count_boys)

Count_girls = girlNames.groupby(['name','year'])['births'].sum()
print(Count_girls)
#avg and max of each name
Avgnames = names.groupby(['name' , 'year'])['births'].max()
print(Avgnames)
#converting into a dataframe again
df_Avgnames = Avgnames.to_frame()
print (df_Avgnames.sort_values(['name', 'births'], ascending=[True, False]))

boys_df = Count_boys.to_frame().reset_index()
girls_df= Count_girls.to_frame().reset_index()

'''for year in years:
    print (Avgnames.iloc[Avgnames.births.argmax()].tolist())'''
#maximal value for each year #most common name 
print (df_Avgnames.loc[df_Avgnames['births'].idxmax()])
print (df_Avgnames.groupby('year').apply(lambda x: x.loc[x.births.idxmax(),['births']]).reset_index())
#name and the highest differnce between between previous year births
boys_df ['dif'] = boys_df.groupby('name')['births'].diff().fillna(0)
print(boys_df.loc[boys_df.groupby(['year','name'])['dif'].idxmax()].reset_index())

girls_df ['dif'] = boys_df.groupby('name')['births'].diff().fillna(0)
print(girls_df.loc[girls_df.groupby(['year','name'])['dif'].idxmax()].reset_index())

#showing the differnce between previous year and present year
#df_Avgnames = df_Avgnames.diff(axis=1)
#df_Avgnames['Diff'] = df_Avgnames.idxmax(axis=1)
#print(df_Avgnames)