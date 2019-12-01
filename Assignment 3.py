# -*- coding: utf-8 -*-
"""
Created on Mon Feb 11 17:08:35 2019

@author: Satya Manepalli
"""

import pandas as pd
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
#avg and max of each name
Avgnames = names.groupby(['name' , 'year'])['births'].max()
print(Avgnames)
#converting into a dataframe again
df_Avgnames = Avgnames.to_frame()
print (df_Avgnames.sort_values(['name', 'births'], ascending=[True, False]))

'''for year in years:
    print (Avgnames.iloc[Avgnames.births.argmax()].tolist())'''
#maximal value for each year #most common name 
print (df_Avgnames.loc[df_Avgnames['births'].idxmax()])
print (df_Avgnames.groupby('year').apply(lambda x: x.loc[x.births.idxmax(),['births']]).reset_index())

#showing the differnce between previous year and present year
df_Avgnames = df_Avgnames.diff(axis=1)
df_Avgnames['Diff'] = df_Avgnames.idxmax(axis=1)
print(df_Avgnames)


'''work'''
#df_Avgnames = df_Avgnames.set_index('name')
#print (df_Avgnames)
#print (df_Avgnames.iloc[df_Avgnames.births.argmax()].tolist())
#print (names.ix[names['births'].idxmax()])
#print (Avgnames['births'] = Avgnames.mean(numeric_only=True, axis=1))
#print (Avgnames['Max'] = Avgnames.idxmax(axis=1))
#print (df_Avgnames.groupby(['year']).max().reset_index())
#print (df_Avgnames.iloc[names.births.argmax()].tolist())
#sort_by_life = Avgnames.sort_values(['births'],ascending=[False])
#df.sort(['a', 'b'], ascending=[True, False])
#names = names.sort_values('births')
#print (sort_by_life)
#for name in names:
    #girlNames = (names.loc[names['births'].idxmax()])
    #print (girlNames)
    #filtered_data = names[names["year"]==2002]
#print (filtered_data)
#print(names[['name', 'sex']])
#print (total_births)
#making the data usable by getting it into a spreadsheet kind of table (pivot table)
#total_births = names.pivot_table('births',index=['year','name'],columns='sex', margins=True, aggfunc=sum)
#total_births = pd.Series(names['name'].unique())
#total_births = total_births.isnull()
#total_births = names[names.isnull()]
#total_births = names[pd.isnull(names['sex'])]
#print (total_births)

#total_births = names[total_births.isnull().any(axis=1)]
#print (total_births)