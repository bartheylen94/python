#---------------------------
# CLASS SIMULATION
# Authors: luca.fiorentino@iae-toulouse.fr , bart.heylen@iae-toulouse.fr
# Note:
#---------------------------
from Stock import Stock
import datetime
import pandas_datareader.data as web

list_stocks = ['GOOGL', 'YHOO', 'AXP', 'XOM', 'KO', 'NOK', 'MS', 'IBM', 'FDX']
start = datetime.datetime(2005, 1, 1)
end = datetime.datetime(2015, 12, 31)
list_data = dict()
for i in list_stocks:
    df = web.DataReader(i, 'yahoo', start, end)
    df['ClosePriceB']=df.Close.shift(1)
    df.iloc[0,6] = df.iloc[0,3]
    df['CCreturn'] = df['Close']/df['ClosePriceB']
    df['avg'] = df['CCreturn'].mean(axis=0)
    df['dif'] = df['CCreturn'] - df['avg']
    df['volatility'] = df['dif']*df['dif']
    df.drop('avg',1, inplace=True)
    df.drop('dif',1, inplace=True)
    list_data[i] = df
print(list_data.get('YHOO'))
