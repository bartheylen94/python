#---------------------------
# CLASS INVESTOR
# Authors: luca.fiorentino@iae-toulouse.fr , bart.heylen@iae-toulouse.fr
# Note:
#---------------------------

from Bond import LTBond
from Bond import STBond
from Stock import Stock

import random
import radar
import datetime
import plotly as py
import pandas as pd
import numpy as np
from prettytable import PrettyTable

#initialize class Investor, 3 subclasses
class Investor(object):
    def __init__(self, Budget, start, end):
        self.Budget = Budget
        self.StartDate = start
        self.EndDate = end
        self.Portfolio = []
    #methods

######################################################


#subclasses
#subclass 1: defensive investor
class Defensive(Investor):
    def __init__(self, Budget, StartDate, EndDate):
        Investor.__init__(self, Budget, StartDate, EndDate)
        self.Portfolio = []

    #method for investing
    def definvesting(self):
        inv = pd.DataFrame()
        rows = len(inv)
        if rows == 0:
            #we define the top line of our dataframe in case it is the first investment
            inv = pd.DataFrame(columns=['TYPE', 'PRICE', 'Quantity', 'Total Amount', 'P_Date', 'S_Date'])
        #investing will be done for as long as we have a budget >= the min amount needed for a ST bond
        stb = STBond(1,1)
        ltb = LTBond(1,1)
        while self.Budget >= ltb.min_amount:
            #rando pick between long and short term
            if random.choice(['LT', 'ST']) == 'LT':
                #in case of long term, we define the line which we will add to the data frame by adding the details of the investment
                inv_new = pd.DataFrame({'TYPE': ['LT'], 'PRICE': [ltb.premium], 'Quantity': [ltb.quantity], 'Total Amount': [ltb.quantity*ltb.min_amount], 'P_Date': [self.StartDate],'S_Date': [self.EndDate]})
                tot_inv = [inv, inv_new]
                inv = pd.concat(tot_inv, axis=0)
                #the budget of the investor is reduced with the amount invested
                self.Budget = self.Budget - ltb.min_amount*ltb.quantity
                self.Portfolio = inv
            else:
                #in the case of a short term bond, a similar tactic is applied but for the ST version
                inv_new = pd.DataFrame({'TYPE': ['ST'], 'PRICE': [stb.premium], 'Quantity': [stb.quantity], 'Total Amount': [stb.quantity*stb.min_amount], 'P_Date': [self.StartDate],'S_Date': [self.EndDate]})
                tot_inv = [inv, inv_new]
                inv = pd.concat(tot_inv, axis=0)
                self.Budget = self.Budget - stb.min_amount*stb.quantity
                self.Portfolio = inv
        while self.Budget <= ltb.min_amount and self.Budget >= stb.min_amount:
            inv_new = pd.DataFrame({'TYPE': ['ST'], 'PRICE': [stb.premium], 'Quantity': [stb.quantity], 'Total Amount': [stb.quantity * stb.min_amount], 'P_Date': [self.StartDate], 'S_Date': [self.EndDate]})
            tot_inv = [inv, inv_new]
            inv = pd.concat(tot_inv, axis=0)
            self.Budget = self.Budget - stb.min_amount * stb.quantity
            self.Portfolio = inv
        return self.Portfolio

######################################################
#subclass 2
class Aggresive(Investor):
    def __init__(self, Budget, StartDate, EndDate):
        Investor.__init__(self, Budget, StartDate, EndDate)
        self.Portfolio = []


    #methods#
    #&1.investing
    def agginvesting(self):
        while self.Budget >= 100:
            inv = pd.DataFrame()
            if len(inv) == 0:
                inv = pd.DataFrame(columns=['TYPE', 'PRICE', 'Quantity', 'Total Amount', 'P_Date', 'S_Date'])
            #we select a random stock from the list of stocks
            stock = random.choice(['AAPL','GOOGL', 'YHOO', 'AXP', 'XOM', 'KO', 'NOK', 'MS', 'IBM', 'FDX'])
            #an instance of class stock is initialized
            Stock(stock, start, end)
            #we look for the price on the first day
            first_price = Stock.getFirstPrice
            #and thus determine how many stock we could buy
            max_nmbr = self.Budget/first_price
            #a random number of stock between 0 and the max_nmbr is chosen
            nmbr_invested = random.randrange(0, max_nmbr)
            #we add a line to our portfolio, stating the stock, the day of purchase and the number of stocks we buy
            inv_new = pd.DataFrame({'TYPE': [stock], 'PRICE': [first_price], 'Quantity': [nmbr_invested], 'Total Amount': [nmbr_invested*first_price], 'P_Date': [self.StartDate], 'S_Date': [self.EndDate]})
            tot_inv = [inv, inv_new]
            inv = pd.concat(tot_inv, axis=0)
            #our budget is reduced with the amount invested
            self.Budget = self.Budget - nmbr_invested*first_price
            self.Portfolio = inv


######################################################
#subclass 3
#class Mixed(Investor):
#    def __init__(self, Budget, StartDate, EndDate):
#        Investor.__init__(self, Budget, StartDate, EndDate)
#        self.Portfolio = []

    #methods
    #def mixinvesting(self):
     #   inv = pd.DataFrame(columns=['TYPE', 'PRICE', 'Quantity', 'Total Amount', 'P_Date', 'S_Date'])

      #  if random.choice(['STOCK', 'BOND'])=='BOND':

       # else:


            ######################################################
#
#
# #simulating 1000 investors of each class
    #for x in range(1000):
 #     start = datetime.datetime(2005, 1, 1)
 #     end = datetime.datetime(2015,12,31)
 #     start = radar.random_date(start, end)
 #     bgt = 12000
 # #   Aggresive(bgt, start, end)
 #     x = Defensive(bgt, start, end)
 #     port = Defensive.definvesting(x)