#---------------------------
# CLASS STOCK
# Authors: luca.fiorentino@iae-toulouse.fr , bart.heylen@iae-toulouse.fr
# Note:the class use yahoo finance API to have the quotations of the stocks
#---------------------------
#import library
from numpy import log
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
        self.data=list_data{tkr}.truncate(startdate, enddate)

    #methods
        #get the quotes for a stock between two dates
    # def getQuotes(self):
    #     # import stock data
    #     quotes = web.DataReader(self.tkr, 'yahoo', self.startdate, self.enddate)
    #     quotes['dates'] = quotes.index.map(lambda x: str(x)[:10])
    #     return quotes

        # compute the continously-compounded return of a stock in a period
    def stkCCReturn(self):
        return data.sum('CCReturn')

        # compute the daily volatility
    def stkVolatility(self):
        return data.sum('DVolatility')

    def getFirstPrice(self):
        return data.iloc[0, 0]

    def getLastPrice(self):
        return data.iloc[-1, 0]


# # #import data for the different companies, each in one dataframe named 'STOCK'
# list_stocks = ['GOOGL','YHOO','AXP','XOM','KO','NOK','MS','IBM','FDX']
# df_data = pd.DataFrame(columns=['STOCK','DATA'])
# start = datetime.datetime(2005,1,1)
# end = datetime.datetime(2015,12,31)
# for i in list_stocks:
#     new_stock = Stock(start, end, str(i))
#     new_df = web.DataReader(i, 'yahoo', start, end)
#     df_data.append(i):new_stock]
#
#
# #list_data[new_stock[3].tkr] =='GOOGL':
# print(list_data['GOOGL'].data)
# print(list_data[0].tkr)


#
# print(GOOGLE.data)