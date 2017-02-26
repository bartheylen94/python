from Stock import Stock
import datetime

start = datetime.datetime(2016, 1, 1)
end = datetime.datetime(2016, 1, 5)
stk=Stock('GOOGL', start, end)
#print(stk.getQuotes())
a=stk.stkCCReturn()

print(a['CCStkReturn'])