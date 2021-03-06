#---------------------------
# CLASS STOCK
# Authors: luca.fiorentino@iae-toulouse.fr , bart.heylen@iae-toulouse.fr
# Note:the class use yahoo finance API to have the quotations of the stocks
#---------------------------
#import library

import plotly as py
import plotly.graph_objs as go
import os
import datetime
import pandas_datareader.data as web
import numpy as np
#-----
list_stocks = ['AAPL', 'GOOGL', 'YHOO', 'AXP', 'XOM', 'KO', 'NOK', 'MS', 'IBM', 'FDX']
start = datetime.datetime(2005, 1, 1)
end = datetime.datetime(2015, 12, 31)
list_data = dict()
for i in list_stocks:
    df = web.DataReader(i, 'yahoo', start, end)
    df['ClosePriceB']=df.Close.shift(1)
    df.iloc[0,6] = df.iloc[0,3]
    df['CCreturn'] = np.log(df['Close']/df['ClosePriceB'])
    df['avg'] = df['CCreturn'].mean(axis=0)
    df['dif'] = df['CCreturn'] - df['avg']
    df['volatility'] = df['dif']*df['dif']
    df.drop('avg',1, inplace=True)
    df.drop('dif',1, inplace=True)
    list_data[i] = df

#initialize class Stock
class Stock(object):
    #properties
    def __init__(self, startdate, enddate, tkr):
        self.startdate = startdate
        self.enddate = enddate
        self.tkr = tkr
        self.data=list_data[tkr].truncate(startdate, enddate)

        # compute the continously-compounded return of a stock in a period
    def stkCCReturn(self, date):
        x=self.data.index.searchsorted(date)
        begin = self.getFirstPrice()
        end = self.data.iloc[x, 3]
        rr = (end-begin)/begin
        return rr

        # compute the daily volatility

    def getFirstPrice(self):
        return self.data.iloc[0, 3]

    def getPriceAt(self,date):
        x = self.data.truncate(before=date)
        price = self.data.loc['x','Close']
        return price

    def getLastPrice(self):
        return self.data.iloc[-1, 3]

#plot the investment of the minimum allowed invested amount for both bonds over a period of 100 years
    def plotStkPrice(self):
        plotresult= os.path.abspath("../data/Stock_Plot.html")
        data_par = [go.Scatter(x=self.data.index, y=self.data['Close'])]
        fig=go.Figure(data=data_par)
        py.offline.plot(fig,filename=plotresult)

    def plotStkReturn(self):
        plotresult= os.path.abspath("../data/Stock_Plot_Return.html")
        data_par = [go.Scatter(x=self.data.index, y=self.data['CCreturn'])]
        fig=go.Figure(data=data_par)
        py.offline.plot(fig,filename=plotresult)
