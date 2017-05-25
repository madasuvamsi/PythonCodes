__author__ = 'vamsi'
import pandas as pd
import datetime
from pandas_datareader import data
import matplotlib.pyplot as plt

stockprice=input("Enter the Stock Symbol:")


start = datetime.datetime(2010, 1, 1)
end = datetime.datetime(2015, 8, 22)
df=data.DataReader(stockprice, "yahoo", start, end)
print(df.head())
df['High'].plot()
plt.legend()
plt.show()