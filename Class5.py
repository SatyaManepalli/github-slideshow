# -*- coding: utf-8 -*-
"""
Created on Thu Feb 14 15:30:42 2019

@author: Satya Manepalli
"""
import pandas as pd
import numpy as np
obj = pd.Series([4,7,-5,3])
#print(obj)
#print(obj.values)
#print(obj.index)
obj2=pd.Series(obj.values,index=['d','b','a','c'])
#print(obj2)
'''print(obj2.index)
print(obj2['a'])
obj2['d'] = 6
print(obj2)
print(obj2>0)
print(obj2[obj2>0])
print(obj2*2)
print(np.exp(obj2))
print('b' in obj2)'''
sdata = {'Ohio':35000, 'Texas': 71000, 'Oregon':16000,'Utah':5000}
obj3 = pd.Series(sdata)
#print(obj3)

states = ["California", "Ohio", "Oregon", "Texas"]
obj4 = pd.Series(sdata, index=states)
#print(obj4)

'''print(pd.isnull(obj4))
print(obj4.isnull())
print(obj3 + obj4)

obj4.name = "population"
obj4.index.name = "state"
print(obj4)'''

data = {'state': ['Ohio', 'Ohio', 'Ohio', 'Nevada', 'Nevada', 'Nevada'], 
       'year': [2000, 2001, 2002, 2001, 2002, 2003],
        'pop': [1.5, 1.7, 3.6, 2.4, 2.9, 3.2]}
frame = pd.DataFrame(data)
print(frame)

pd.DataFrame(data, columns=['year', 'state', 'pop'])
frame2 = pd.DataFrame(data, columns=['year', 'state', 'pop', 'debt'],
                      index=['one', 'two', 'three', 'four', 
                            'five', 'six'])
print(frame2)
print(frame2.columns)

print(frame2['state'])
print(frame2.loc['three'])
print(frame2.iloc[2])

df = pd.DataFrame([[1.4, np.nan], [7.1, -4.5],
                   [np.nan, np.nan], [0.75, -1.3]],
                  index=['a', 'b', 'c', 'd'],
                  columns=['one', 'two'])
print(df)
print("Column sums:\n",df.sum())
print("Row sums:\n",df.sum(axis='columns'))
print("Row sums:\n",df.sum(axis='columns', skipna=False))
print(df.idxmax())
print(df.cumsum())
print(df.describe())

obj = pd.Series(['a', 'a', 'b', 'c'] * 4)
print(obj.describe())

#arr3=np.random.randn(6,3)
#print (arr3)

print("\n\n==============Begin Finance Data===================")
import pandas_datareader.data as web
all_data ={ticker: web.get_data_yahoo(ticker)
        for ticker in['AAPL','IBM','MSFT','GOOG']}

price = pd.DataFrame({ticker: data['Adj Close'] 
    for ticker, data in all_data.items()}) 
volume = pd.DataFrame({ticker: data['Volume'] 
    for ticker, data in all_data.items()})
returns = price.pct_change()
print("Price Percent Change\n",returns.tail())

print("\nMSFT -- IBM Correlation")
print(returns['MSFT'].corr(returns['IBM']))

print("\nMSFT -- IBM Covariance")
print(returns['MSFT'].cov(returns['IBM']))

from pandas_datareader import data
# Only get the adjusted close.
aapl = data.DataReader("AAPL", 
                       start='2018-1-1', 
                       end='2018-12-31', 
                       data_source='yahoo')['Adj Close']
aapl.plot(title='AAPL Adj. Closing Price')

from pandas_datareader import data
# Only get the adjusted close.
'''aapl = data.DataReader("MSFT", 
                       start='2008-1-1', 
                       end='2019-02-14', 
                       data_source='Microsoft')['Adj Close']
aapl.plot(title='MSFT Adj. Closing Price')'''

df = pd.read_csv('C:\DataScience\In Class\pydata-book-2nd-edition\pydata-book-2nd-edition\examples/ex1.csv')
print(df)
print()
print("\nRead file with read_table:")
df1= pd.read_table('C:\DataScience\In Class\pydata-book-2nd-edition\pydata-book-2nd-edition\examples/ex1.csv',sep=',')
print(df1)

#Hierarchical index from multiple columns:
#parsed = pd.read_csv('C:\DataScience\In Class\pydata-book-2nd-edition\pydata-book-2nd-edition\examples/csv_mindex.csv',
                   #  index_col=['key1', 'key2'])
#print(parsed)

data = np.arange(40).reshape(10,4)#pd.read_csv('C:\DataScience\In Class\pydata-book-2nd-edition\pydata-book-2nd-edition\examples/ex1.csv')
frame1 = pd.DataFrame(data, columns=['Alpha','Num1','Num2','Num3'],
                      index=['1', '2', '3', '4', 
                            '5', '6', '7', '8','9','10'])
#frame1.to_csv('C:\DataScience\In Class\pydata-book-2nd-edition\pydata-book-2nd-edition\examples/out1.csv', sep=',')
#frame1.to_csv('C:\DataScience\In Class\pydata-book-2nd-edition\pydata-book-2nd-edition\examples/out.csv')

parsed = pd.read_csv('C:\DataScience\In Class\pydata-book-2nd-edition\pydata-book-2nd-edition\examples/out.csv',index_col=['Alpha', 'Num3'])
#print(parsed)'''

from lxml import objectify
path = 'C:\DataScience\In Class\pydata-book-2nd-edition\pydata-book-2nd-editiondatasets/mta_perf/Performance_MNR.xml'
parsed = objectify.parse(open(path))
root = parsed.getroot()
data = []











