#---------------------------
# CLASS STOCK
# Authors: luca.fiorentino@iae-toulouse.fr , bart.heylen@iae-toulouse.fr
# Note:the class use yahoo finance API to have the quotations of the stocks
#---------------------------
#import library

    from math import log
    import pandas_datareader.data as web

#initialize class Stock
class Stock(object):
    #properties
    def __init__(self, StockNumber, StockTkr, StartDate, EndDate):
        self.StockNumber = StockNumber
        self.StockTkr = StockTkr
        self.StartDate = StartDate
        self.EndDate = EndDate

    #methods
        #get the quotes for a stock between two dates
    def getQuotes(self, startDate, endDate):
        # import stock data
        quotes = web.DataReader(self.StockTkr, 'yahoo', startDate, endDate)
        quotes['dates'] = quotes.index.map(lambda x: str(x)[:10])
        return quotes

        # compute the continously-compounded return of a stock in a period
    def stkCCReturn(self,startReturn, endReturn):
        quotesReturn=self.getQuotes(startReturn, endReturn)
        quotesReturn['CCStkReturn'] = quotesReturn['CCStkReturn'].map(lambda x: log(quotesReturn[i, 'Close']/quotesReturn[i-1, 'Close']) for i in len(quotesReturn) )
        return quotesReturn.sum('CCStkReturn')

        # compute the daily volatility
    def stkVolatility(self, startVol, endVol):
        quotesVol=self.getQuotes(startVol, endVol)
        quotesVol['DVolatility']=quotesVol['DVolatility'].map(lambda x: ((quotesVol[i,'CCStkReturn']-quotesVol.mean('CCStkReturn'))**2) for i in len(quotesVol))
        
