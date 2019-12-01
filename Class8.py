# -*- coding: utf-8 -*-
"""
Created on Sat Mar 23 11:07:40 2019

@author: Satya Manepalli
"""

import quandl
import numpy as np
import pandas as pd
np.random.seed(12345)
import matplotlib.pyplot as plt
plt.rc('figure', figsize=(10, 6))
PREVIOUS_MAX_ROWS = pd.options.display.max_rows
pd.options.display.max_rows = 20
np.set_printoptions(precision=4, suppress=True)
from datetime import datetime
now = datetime.now()
print(now)
print(now.year, now.month, now.day, now.hour, 
      now.minute, now.second)
