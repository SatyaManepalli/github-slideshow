# -*- coding: utf-8 -*-
"""
Created on Thu Apr  4 11:40:45 2019

@author: Satya Manepalli
"""
import pandas as pd
import numpy as np
from datetime import datetime
from datetime import timedelta
from dateutil.parser import parse

now = datetime.now()
#print(now)
#print(now.year, now.month, now.day, now.hour, 
#      now.minute, now.second)

#delta = datetime(2011, 1, 7) - datetime(2008, 6, 24, 8, 15)
#print(delta)
#print(delta.days)
#print(delta.seconds)
'''delta = datetime.now() - datetime(1995, 3, 16, 22, 15)
#print(delta)
#print(delta.days)
#print(delta.seconds)

start = datetime(2011, 1, 7)
print(timedelta(13))
new = start + timedelta(12)
new2 = start - 2 * timedelta(12)
print(new)
print(new2)

stamp = datetime(2011, 1, 3)
str(stamp)
print(stamp.strftime('%Y-%m-%d'))
print()

value = '2011-01-03'
print(datetime.strptime(value, '%Y-%m-%d'))
datestrs = ['7/6/2011', '8/6/2011']
print([datetime.strptime(x, '%m/%d/%Y') for x in datestrs])

print(parse('2011-01-03'))
print()

print(parse('Jan 31, 1997 10:45 PM'))
print()

print(parse('6/12/2011', dayfirst=True))
print()

dates = [datetime(2011, 1, 2), datetime(2011, 1, 5),
         datetime(2011, 1, 7), datetime(2011, 1, 8),
         datetime(2011, 1, 10), datetime(2011, 1, 12)]
ts = pd.Series(np.random.randn(6), index=dates)
print(ts)

print(ts + ts[::2])
stamp = ts.index[2]
print(stamp)
print(ts['1/10/2011'])
print(ts['20110110'])

longer_ts = pd.Series(np.random.randn(1000),
                      index=pd.date_range('1/1/2000', 
                                          periods=1000))
print(longer_ts)
print(longer_ts['2001'])

dates = pd.date_range('1/1/2000', periods=100, freq='W-WED')
long_df = pd.DataFrame(np.random.randn(100, 4),
                       index=dates,
                       columns=['Colorado', 'Texas',
                                'New York', 'Ohio'])
print(long_df.loc['5-2001'])

p = pd.Period(2007, freq='A-DEC')
print (p)

rng = pd.period_range('2000-01-01', '2000-06-30', freq='M')
print (rng)
p2= pd.Period('2007', freq='A-JUN')
print(p2)
p2.asfreq('M', how='start')
p2.asfreq('M', how='end')
print(p2)

rng = pd.date_range('2000-01-01', periods=100, freq='D')
ts = pd.Series(np.random.randn(len(rng)), index=rng)
print(ts)

print(ts.resample('M').mean())
print(ts.resample('M', kind='period').mean())

rng = pd.date_range('2000-01-01', periods=12, freq='T')
ts = pd.Series(np.arange(12), index=rng)
print(ts)

#print(ts.resample('5min', closed='right').sum())

print(ts.resample('5min', closed='left').sum())

print("------------------------------------------------------------------")
rng = pd.date_range('2000-01-01', periods=100, freq='D')
ts = pd.Series(np.random.randn(len(rng)), index=rng)
print(ts)
print(ts.resample('M').mean())
print(ts.resample('M', kind='period').mean())'''

rng = pd.date_range('2000-01-01', periods=100, freq='D')
ts = pd.Series(np.random.randn(len(rng)), index=rng)
#print(ts)
print(ts.resample('M').mean())
print(ts.resample('M', kind='period').mean())
print(ts.resample('M', kind='timestamp').mean())




