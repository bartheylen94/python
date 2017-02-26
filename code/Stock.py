#---------------------------
# CLASS STOCK
# Authors: luca.fiorentino@iae-toulouse.fr , bart.heylen@iae-toulouse.fr
# Note:the class use yahoo finance API to have the quotations of the stocks
#---------------------------
#import library
import math
import pandas_datareader.data as web


#initialize class Stock
class Stock(object):
    #properties
    def __init__(self, StockTkr, StartDate, EndDate):
        if StartDate.isocalendar() == 6:
            self.StartDate = StartDate - 1
        if StartDate.isocalendar() == 7:
            self.StartDate = StartDate + 1
        if EndDate.isocalendar() == 6:
            self.EndDate = EndDate - 1
        if StartDate.isocalendar() == 7:
            self.EndDate = EndDate + 1
        self.StockTkr = StockTkr

    #methods
        #get the quotes for a stock between two dates
    def getQuotes(self):
        # import stock data
        quotes = web.DataReader(self.StockTkr, 'yahoo', self.StartDate, self.EndDate)
        quotes['dates'] = quotes.index.map(lambda x: str(x)[:10])
        return quotes

        # compute the continously-compounded return of a stock in a period
    def stkCCReturn(self):
        quotesReturn=self.getQuotes()
        quotesReturn['CCStkReturn'] = quotesReturn['CCStkReturn'].map(lambda x: math.log(quotesReturn[i, 'Close'] / quotesReturn[i - 1, 'Close']) for i in len(quotesReturn))
        return quotesReturn.sum('CCStkReturn')

        # compute the daily volatility
    def stkVolatility(self):
        quotesVol=self.stkCCReturn()
        quotesVol['DVolatility']=quotesVol['DVolatility'].map(lambda x: ((quotesVol[i,'CCStkReturn']-quotesVol.mean('CCStkReturn'))**2) for i in len(quotesVol))
        return quotesVol.sum('DVolatility')

    def getFirstPrice(self):
        firstPrice = self.getQuotes()
        return firstPrice.iloc[3,3]
