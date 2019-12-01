# -*- coding: utf-8 -*-
"""
Created on Sun Feb  3 22:39:07 2019

@author: Satya Manepalli
"""

import pandas as pd
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
"""print(names)"""

total_births = names.pivot_table('births',index='year',columns='sex', aggfunc=sum)
"""print(total_births.head())"""
"""total_births.plot(title="Total births by sex and year")"""

def add_prop(group):
    group['prop'] = group.births/group.births.sum()
    return group

names = names.groupby(['year','sex']).apply(add_prop)
"""names = names.groupby(['year','sex']).prop.sum()"""
"""print(names)"""

"""def get_top1000(group):    
    return group.sort_values(by='births',ascending=False)[:1000]"""

"""grouped = names.groupby(['year','sex'])
top1000 = grouped.apply(get_top1000)
#Drop the group index, not needed
"""top1000.reset_index(inplace=True,drop=True)
for i in top1000:
    print(i)
print(get_top1000)"""