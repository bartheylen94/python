import random
import plotly as py
import pandas as pd
from prettytable import PrettyTable

#initialize class Investor, 3 subclasses
class Investor(object):
    def __init__(self, Budget, StartDate, Portfolio):
        self.Budget = Budget
        self.StartDate = StartDate
        self.Portfolio = Portfolio
    #methods


#subclasses
class Defensive(Investor):
    Investor.__init__(self, Budget, StartDate, Portfolio)

    def Investing(self):
        #self.Portfolio = pd.DataFrame[['Index', 'Type', 'Price', 'Quantity', 'P_Date', 'S_Date']]
        inv_df = pd.DataFrame(['Type', 'Price', 'Quantity', 'Total Amount', 'P_Date', 'S_Date'])
        while self.Budget >= STBond.min_amount:
            if random.choice(['LT', 'ST']) == 'LT':
                inv_x = pd.DataFrame()
                #inv_table.add_row("LT", LTBond.premium, 1, LTBond.min_amount, self.StartDate, "N/A" )
                self.Budget = self.Budget - LTBond.min_amount

class Aggresive(Investor):
    Investor.__init__(self, Budget, StartDate, Portfolio)

class Mixed(Investor):
    Investor.__init__(self, Budget, StartDate, Portfolio)



