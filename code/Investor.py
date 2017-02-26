#---------------------------
# CLASS INVESTOR
# Authors: luca.fiorentino@iae-toulouse.fr , bart.heylen@iae-toulouse.fr
# Note:
#---------------------------

from Bond import LTBond
from Bond import STBond
import random
import radar
import datetime
import plotly as py
import pandas as pd
import numpy as np
from prettytable import PrettyTable

#initialize class Investor, 3 subclasses
class Investor(object):
    def __init__(self, Budget, StartDate, EndDate):
        self.Budget = Budget
        self.StartDate = StartDate
        self.Portfolio = None
        self.EndDate = EndDate
    #methods

######################################################


#subclasses
#subclass 1: defensive investor
class Defensive(Investor):
    def __init__(self, Budget, StartDate, EndDate):
        Investor.__init__(self, Budget, StartDate, EndDate)
        self.Budget = Budget
        self.StartDate = StartDate
        self.Portfolio = None
        self.EndDate = EndDate

    #method for investing
    def definvesting(self):
        #we define the top line of our dataframe
        inv = pd.DataFrame(columns=['TYPE', 'PRICE', 'Quantity', 'Total Amount', 'P_Date', 'S_Date'])
        #investing will be done for as long as we have a budget >= the min amount needed for a ST bond
        while self.Budget >= STBond.min_amount:
            #rando pick between long and short term
            if random.choice(['LT', 'ST']) == 'LT':
                #in case of long term, we define the line which we will add to the data frame by adding the details of the investment
                inv_new = pd.DataFrame({'TYPE': ['LT'], 'PRICE': [LTBond.premium], 'Quantity': [LTBond.quantity], 'Total Amount': [LTBond.quantity*LTBond.premium], 'P_Date': [self.StartDate],'S_Date': [self.EndDate]})
                tot_inv = [inv, inv_new]
                result = pd.concat(tot_inv, axis=0)
                #the budget of the investor is recued with the amount invested
                self.Budget = self.Budget - LTBond.min_amount*LTBond.quantity
                self.Portfolio = result
            else:
                #in the case of a short term bond, a similar tactic is applied but for the ST version
                inv_new = pd.DataFrame({'TYPE': ['ST'], 'PRICE': [STBond.premium], 'Quantity': [STBond.quantity], 'Total Amount': [STBond.quantity*LTBond.premium], 'P_Date': [self.StartDate],'S_Date': [self.EndDate]})
                tot_inv = [inv_df, inv_new]
                result = pd.concat(tot_inv, axis=0)
                self.Budget = self.Budget - LTBond.min_amount
                self.Portfolio = result


######################################################
#subclass 2
class Aggresive(Investor):
    def __init__(self, Budget, StartDate, EndDate):
        Investor.__init__(self, Budget, StartDate)
        self.Budget = Budget
        self.StartDate = StartDate
        self.EndDate = EndDate

    #methods#
    #&1.investing
    def agginvesting(self):
        while self.Budget >= 100:
            inv_df = pd.DataFrame(columns=['TYPE', 'PRICE', 'Quantity', 'Total Amount', 'P_Date', 'S_Date'])
            stock = random.choice(['AAPL','GOOGL', 'YHOO', 'AXP', 'XOM', 'KO', 'NOK', 'MS', 'IBM', 'FDX'])
            max_nmbr = self.Budget/
            nmbr = random.randrange()

######################################################
#subclass 3
class Mixed(Investor):
    def __init__(self, Budget, StartDate, EndDate):
        Investor.__init__(self, Budget, StartDate, EndDate)
        self.Budget = Budget
        self.StartDate = StartDate
        self.Portfolio = None
        self.EndDate = EndDate

    #methods
    def mixinvesting(self):
        inv = pd.DataFrame(columns=['TYPE', 'PRICE', 'Quantity', 'Total Amount', 'P_Date', 'S_Date'])

        if random.choice(['STOCK', 'BOND'])=='BOND':

        else:


            ######################################################


#method to find business date closest to date

#simulating 1000 investors of each class
for x in range(1000):
    start = '01/01/2005'
    end = '31/12/2015'
    start = radar.random_date(start, end)
    bgt = 12000
    x.Defensive(bgt, start, end)
    x.Aggresive(bgt, start, end)
    x.Mixed(bgt, start, end)

