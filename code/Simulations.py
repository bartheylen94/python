from .Stock import Stock
import datetime

start = datetime.datetime(2016, 1, 1)
end = datetime.datetime(2017, 2, 27)
if start > end:
    print('The ending date is before the starting date')
if start.isocalendar() == 6:
    start = start - 1
if start.isocalendar() == 7:
    start = start +1

stk=Stock(1, 'GOOGL', start, end)
stk.getQuotes()
print(stk)