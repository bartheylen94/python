from Stock import Stock
import datetime

start = datetime.datetime(2016, 1, 1)
end = datetime.datetime(2016, 1, 8)
stk=Stock('GOOGL', start, end)
#print(stk.getQuotes())
print(stk.stkCCReturn())
