from .Stock import Stock
import datetime

start = datetime.datetime(2016, 1, 1)
end = datetime.datetime(2017, 2, 27)

stk=Stock(1,'GOOGL',start,end)
stk.getQuotes(start,end)
print(stk)