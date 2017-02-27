from Stock import Stock
import datetime

start = datetime.datetime(2016, 1, 1)
end = datetime.datetime(2016, 1, 5)
stk=Stock('GOOGL', start, end)
#print(stk.getQuotes())
a=stk.stkCCReturn()

print(a['CCStkReturn'])


#CCReturn
quotesReturn['ClosePriceB']=quotesReturn.Close.shift(1)
        quotesReturn.iloc[0, 7] = quotesReturn.iloc[0, 3]
        quotesReturn['CCReturn'] = quotesReturn['Close'] /quotesReturn['ClosePriceB']
#volatility
quotesVol['DVolatility']=(quotesVol['CCStkReturn']-quotesVol.mean('CCStkReturn'))**2