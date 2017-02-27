#---------------------------
# CLASS STOCK
# Authors: luca.fiorentino@iae-toulouse.fr , bart.heylen@iae-toulouse.fr
# Note:the class use yahoo finance API to have the quotations of the stocks
#---------------------------
#import library


import matplotlib.pyplot as plt
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

#initialize class Stock
class Stock(object):
    #properties
    def __init__(self, startdate, enddate, tkr):
        self.startdate = startdate
        self.enddate = enddate
        self.tkr = tkr
        self.data=list_data[tkr].truncate(startdate, enddate)

    #methods
        #get the quotes for a stock between two dates
    # def getQuotes(self):
    #     # import stock data
    #     quotes = web.DataReader(self.tkr, 'yahoo', self.startdate, self.enddate)
    #     quotes['dates'] = quotes.index.map(lambda x: str(x)[:10])
    #     return quotes

        # compute the continously-compounded return of a stock in a period
    def stkCCReturn(self):
        return self.data.sum('CCReturn')

        # compute the daily volatility
    def stkVolatility(self):
        return self.data.sum('DVolatility')

    def getFirstPrice(self):
        return self.data.iloc[0, 0]

    def getLastPrice(self):
        return self.data.iloc[-1, 0]


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

#plot the investment of the minimum allowed invested amount for both bonds over a period of 100 years
    def plotStkPrice(self):
        self.data.plot(x='Date', y='Close')

        # for days in range(self.startdate, self.enddate):
        #     STlist.append(STBond.compound_return(STBond(years, 1)))
        #     LTlist.append(LTBond.compound_return(LTBond(years, 1)))
        # print(LTlist)
        # y = range(1,101)
        # plt.plot(y, STlist)
        # plt.plot(y, LTlist)
        # plt.legend(['Short Term Bond', 'Long Term Bond'], loc='upper left')
        # plt.ylabel('return')
        # plt.xlabel('years')