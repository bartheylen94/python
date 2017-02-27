#---------------------------
# CLASS STOCK
# Authors: luca.fiorentino@iae-toulouse.fr , bart.heylen@iae-toulouse.fr
# Note:the class use yahoo finance API to have the quotations of the stocks
#---------------------------
#import library
import math
import pandas_datareader.data as web
import datetime
import pandas as pd

#initialize class Stock
class Stock(object):
    #properties
    def __init__(self, startdate, enddate, tkr):
        self.startdate = startdate
        self.enddate = enddate
        self.tkr = tkr
        self.data = []
        if self.startdate.isocalendar() == 6:
            self.startdate = startdate - 1
        else:
            self.startdate = startdate
        if self.startdate.isocalendar() == 7:
            self.startdate = startdate + 1
        else:
            self.startdate = startdate
        if self.enddate.isocalendar() == 6:
            self.enddate = enddate - 1
        else:
            self.enddate = enddate
        if self.enddate.isocalendar() == 7:
            self.enddate = enddate + 1
        else:
            self.enddate = enddate

        if self.startdate > self.enddate:
            print('The ending date is before the starting date')

    #methods
        #get the quotes for a stock between two dates
    def getQuotes(self):
        # import stock data
        quotes = web.DataReader(self.tkr, 'yahoo', self.startdate, self.enddate)
        quotes['dates'] = quotes.index.map(lambda x: str(x)[:10])
        return quotes

        # compute the continously-compounded return of a stock in a period
    def stkCCReturn(self):
        quotesReturn=self.getQuotes()
        quotesReturn['ClosePriceB']=quotesReturn.Close.shift(1)
        quotesReturn['CCStkReturn'] = quotesReturn['Close'].map(lambda x: x!=0, 1 )
        return quotesReturn

        # compute the daily volatility
    def stkVolatility(self):
        quotesVol=self.stkCCReturn()
        quotesVol['DVolatility']=quotesVol['DVolatility'].map(lambda x: ((quotesVol[i,'CCStkReturn']-quotesVol.mean('CCStkReturn'))**2) for i in quotesVol)
        return quotesVol.sum('DVolatility')

    def getFirstPrice(self):
        firstPrice = self.getQuotes()
        return firstPrice.iloc[0, 0]

    def getLastPrice(self):
        firstPrice = self.getQuotes()
        return firstPrice.iloc[-1, 0]


# #import data for the different companies, each in one dataframe named 'STOCK'
list_stocks = ['GOOGL','YHOO','AXP','XOM','KO','NOK','MS','IBM','FDX']
list_data = []
start = datetime.datetime(2005,1,1)
end = datetime.datetime(2015,12,31)
for i in list_stocks:
    new_stock = Stock(start, end, str(i))
    new_stock.data = web.DataReader(i, 'yahoo', start, end)
    list_data.append(new_stock)

print(list_data[3].data)


#
# print(GOOGLE.data)