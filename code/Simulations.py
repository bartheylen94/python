#---------------------------
# CLASS SIMULATION
# Authors: luca.fiorentino@iae-toulouse.fr , bart.heylen@iae-toulouse.fr
# Note:
#---------------------------
from Stock import Stock
import datetime
from Investor import Defensive
import radar
# start = datetime.datetime(2015, 1, 1)
# end = datetime.datetime(2015, 12, 31)
#
#
# stk=Stock(start, end, 'GOOGL')
# stk.ploStkPrice()

start = datetime.datetime(2005, 1, 1)
end = datetime.datetime(2015, 12, 31)
startdate = radar.random_date(start, end)
bgt = 12000
new_inv = Defensive(bgt, startdate, end)
print(new_inv.StartDate)
print(new_inv.definvesting())