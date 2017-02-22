#---------------------------
# CLASS STOCK
# Authors: luca.fiorentino@iae-toulouse.fr , bart.heylen@iae-toulouse.fr
# Note:the class use yahoo finance API to have the quotations of the stocks
#---------------------------
#import library
    import pandas_datareader.data as web
    import datetime
# initialize class Stock
class Stock(object):
    #properties
    def __init__(self, StockNumber, StockTkr, StartDate, EndDate):
        self.StockNumber = StockNumber
        self.StockTkr = StockTkr
        self.StartDate = StartDate
        self.EndDate = EndDate

    #methods
        #def stockreturn(self):
    def __init__(self, startDate, endDate):
        # import stock data
        quotes = web.DataReader(self.StockTkr, 'yahoo', startDate, endDate)
        return quotes

