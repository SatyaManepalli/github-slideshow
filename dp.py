# -*- coding: utf-8 -*-
"""
Created on Mon Mar  4 13:00:02 2019

@author: Satya Manepalli
"""
import numpy as np
import pandas as pd
df = pd.DataFrame([('bird', 'Falconiformes', 389.0),
                       ('bird', 'Psittaciformes', 24.0),
                       ('mammal', 'Carnivora', 80.2),
                     ('mammal', 'Primates', np.nan),
                      ('mammal', 'Carnivora', 58)],
                     index=['falcon', 'parrot', 'lion', 'monkey', 'leopard'],
                      columns=('class', 'order', 'max_speed'))
#print (df)
grouped = df.groupby(['class', 'order'])
print (grouped)