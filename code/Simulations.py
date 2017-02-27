#---------------------------
# CLASS SIMULATION
# Authors: luca.fiorentino@iae-toulouse.fr , bart.heylen@iae-toulouse.fr
# Note:
#---------------------------
from Stock import Stock
import datetime
start = datetime.datetime(2015, 1, 1)
end = datetime.datetime(2015, 12, 31)


stk=Stock(start, end, 'GOOGL')
stk.ploStkPrice()