# -*- coding: utf-8 -*-
"""
Created on Thu Mar 14 16:54:48 2019

@author: Satya Manepalli
"""

import pandas as pd
import numpy as np
from numpy import nan as NA
df = pd.DataFrame(np.random.randn(8, 4))
print (df, "\n")
df.iloc[:5, 1] = NA
df.iloc[3:5, 3] = NA
print (df, "\n")
df1 = df.dropna()
print (df1, "\n")
df2 = df.dropna(thresh = 3)
print (df2, "\n")

df5 = df
print("\nExploring fill with mean\n")
df5 = df5.fillna(df5.mean())
print (df5.mean(), "\n")
print(df5)

ages = [20, 22, 25, 27, 21, 23, 37, 31, 61, 45, 41, 32]
bins = [18, 25, 35, 60, 100]
cats = pd.cut(ages, bins)
print("\n\n\nCategories:\n,", cats)

print(cats.codes)
print(cats.categories)
print(pd.value_counts(cats))

book = open("C:/Users/Satya Manepalli/Desktop/names/yob1880.txt")
import re
allwords = []
for line in book:
    words = line.split()
    for w in words:
        if w.isalpha:
            allwords.append(w)
vocab = set(allwords)
#print (vocab)

#print([w for w in vocab if re.search('ed$', w)])
#print([w for w in vocab if re.search("<<..g..c..>>", w)])

data = pd.DataFrame(np.random.randn(1000, 4))
print(data.describe())
col = data[2]
#print (data)

print("\nLocations of data with abs value > 3\n", col[np.abs(col) > 3])
print(data[(np.abs(data) > 3).any(1)])
data[np.abs(data) > 3] = np.sign(data) * 3
print(data.describe())





