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
    # new_stock = Stock(start, end, str(i))
    df = web.DataReader(i, 'yahoo', start, end)

    list_data[i] = df
#tt
print(list_data.get('YHOO'))

#x = list_data.get('GOOGL'))
#print(x)
# start = datetime.datetime(2016, 1, 1)
# end = datetime.datetime(2016, 1, 8)
# stk=Stock('GOOGL', start, end)
# #print(stk.getQuotes())
# print(stk.stkCCReturn())

print(a['CCStkReturn'])


#CCReturn
quotesReturn['ClosePriceB']=quotesReturn.Close.shift(1)
        quotesReturn.iloc[0, 7] = quotesReturn.iloc[0, 3]
        quotesReturn['CCReturn'] = quotesReturn['Close'] /quotesReturn['ClosePriceB']
#volatility
quotesVol['DVolatility']=(quotesVol['CCStkReturn']-quotesVol.mean('CCStkReturn'))**2