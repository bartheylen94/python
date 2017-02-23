#---------------------------
# CLASS INVESTOR
# Authors: luca.fiorentino@iae-toulouse.fr , bart.heylen@iae-toulouse.fr
# Note:
#---------------------------

from Bond import STBond
from Bond import LTBond
import random
import plotly as py
import pandas as pd
from prettytable import PrettyTable

#initialize class Investor, 3 subclasses
class Investor(object):
    def __init__(self, Budget, StartDate, Portfolio, EndDate):
        self.Budget = Budget
        self.StartDate = StartDate
        self.Portfolio = Portfolio
        self.EndDate = EndDate
    #methods


#subclasses
class Defensive(Investor):
    def __init__(self, Budget, StartDate, Portfolio, EndDate):
        Investor.__init__(self, Budget, StartDate, Portfolio, EndDate)
        self.Budget = Budget
        self.StartDate = StartDate
        self.Portfolio = Portfolio
        self.EndDate = EndDate

    def Investing(self):
        #self.Portfolio = pd.DataFrame[['Index', 'Type', 'Price', 'Quantity', 'P_Date', 'S_Date']]
        inv_df = pd.DataFrame(['Type':pd.Categorical(['LT', 'ST', 'STOCK']), 'Price', 'Quantity', 'Total Amount', 'P_Date', 'S_Date'])
        while self.Budget >= STBond.min_amount:
            if random.choice(['LT', 'ST']) == 'LT':
                inv_x = pd.DataFrame('LT', LTBond.premium, LTBond.quantity, LTBond.quantityLTBond.min_amount, self.StartDate, self.EndDate)
                #inv_table.add_row("LT", LTBond.premium, 1, LTBond.min_amount, self.StartDate, "N/A" )
                self.Budget = self.Budget - LTBond.min_amount

class Aggresive(Investor):
    def __init__(self, Budget, StartDate, Portfolio, EndDate):
        Investor.__init__(self, Budget, StartDate, Portfolio)

class Mixed(Investor):
    def __init__(self, Budget, StartDate, Portfolio, EndDate):
        Investor.__init__(self, Budget, StartDate, Portfolio, EndDate)



