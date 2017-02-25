#---------------------------
# CLASS INVESTOR
# Authors: luca.fiorentino@iae-toulouse.fr , bart.heylen@iae-toulouse.fr
# Note:
#---------------------------

from Bond import LTBond
from Bond import STBond
import random
import plotly as py
import pandas as pd
import numpy as np
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
        inv_df = pd.DataFrame(columns=['TYPE', 'PRICE', 'Quantity', 'Total Amount', 'P_Date', 'S_Date'])
        while self.Budget >= STBond.min_amount:
            if random.choice(['LT', 'ST']) == 'LT':
                inv_new = pd.DataFrame({'TYPE': ['LT'], 'PRICE': [LTBond.premium], 'Quantity': [LTBond.quantity], 'Total Amount': [LTBond.quantity*LTBond.premium], 'P_Date': [self.StartDate],'S_Date': [self.EndDate]})
                tot_inv = [inv_df, inv_new]
                result = pd.concat(tot_inv, axis=0)
                self.Budget = self.Budget - LTBond.min_amount
                return result
            else:
                inv_new = pd.DataFrame({'TYPE': ['ST'], 'PRICE': [STBond.premium], 'Quantity': [STBond.quantity], 'Total Amount': [STBond.quantity*LTBond.premium], 'P_Date': [self.StartDate],'S_Date': [self.EndDate]})
                tot_inv = [inv_df, inv_new]
                result = pd.concat(tot_inv, axis=0)
                self.Budget = self.Budget - LTBond.min_amount
                return result



class Aggresive(Investor):
    def __init__(self, Budget, StartDate, Portfolio, EndDate):
        Investor.__init__(self, Budget, StartDate, Portfolio)

class Mixed(Investor):
    def __init__(self, Budget, StartDate, Portfolio, EndDate):
        Investor.__init__(self, Budget, StartDate, Portfolio, EndDate)



