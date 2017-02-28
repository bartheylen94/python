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
        self.type = 'Defensive'

    #method for investing
    def investing(self):
        inv = pd.DataFrame()
        rows = len(inv)
        difference = self.EndDate - self.StartDate
        dif_in_years = (difference.days + difference.seconds / 86400) / 365.2425
        if rows == 0:
            #we define the top line of our dataframe in case it is the first investment
            inv = pd.DataFrame(columns=['TYPE', 'PRICE', 'Quantity', 'Total Amount', 'P_Date', 'S_Date', 'Return'])
        #investing will be done for as long as we have a budget >= the min amount needed for a ST bond
        stb = STBond(1,1)
        ltb = LTBond(1,1)
        while self.Budget >= ltb.min_amount:
            #rando pick between long and short term
            if random.choice(['LT', 'ST']) == 'LT':
                #in case of long term, we define the line which we will add to the data frame by adding the details of the investment
                inv_new = pd.DataFrame({'TYPE': ['LTBond'], 'PRICE': [ltb.premium], 'Quantity': [ltb.quantity], 'Total Amount': [ltb.quantity*ltb.min_amount], 'P_Date': [self.StartDate],'S_Date': [self.EndDate], 'Return': [ltb.realized_return(dif_in_years)]})
                tot_inv = [inv, inv_new]
                inv = pd.concat(tot_inv, axis=0)
                #the budget of the investor is reduced with the amount invested
                self.Budget = self.Budget - ltb.min_amount*ltb.quantity
                self.Portfolio = inv
            else:
                #in the case of a short term bond, a similar tactic is applied but for the ST version
                inv_new = pd.DataFrame({'TYPE': ['STBond'], 'PRICE': [stb.premium], 'Quantity': [stb.quantity], 'Total Amount': [stb.quantity*stb.min_amount], 'P_Date': [self.StartDate],'S_Date': [self.EndDate], 'Return': [stb.realized_return(dif_in_years)]})
                tot_inv = [inv, inv_new]
                inv = pd.concat(tot_inv, axis=0)
                self.Budget = self.Budget - stb.min_amount*stb.quantity
                self.Portfolio = inv
        while self.Budget <= ltb.min_amount and self.Budget >= stb.min_amount:
            inv_new = pd.DataFrame({'TYPE': ['STBond'], 'PRICE': [stb.premium], 'Quantity': [stb.quantity], 'Total Amount': [stb.quantity * stb.min_amount], 'P_Date': [self.StartDate], 'S_Date': [self.EndDate], 'Return': [stb.realized_return(dif_in_years)]})
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
        self.type = 'Aggresive'

    #methods#
    #&1.investing
    def investing(self):
        inv = pd.DataFrame()
        rows = len(inv)
        if rows == 0:
            #we define the top line of our dataframe in case it is the first investment
            inv = pd.DataFrame(columns=['TYPE', 'PRICE', 'Quantity', 'Total Amount', 'P_Date', 'S_Date', 'Return'])
        while self.Budget >= 100:
            #we select a random stock from the list of stocks
            stock = random.choice(['AAPL','GOOGL', 'YHOO', 'AXP', 'XOM', 'KO', 'NOK', 'MS', 'IBM', 'FDX'])
            #an instance of class stock is initialized
            new_stock = Stock(self.StartDate, self.EndDate, stock)
            #we look for the price on the first day
            first_price = new_stock.getFirstPrice()
            #and thus determine how many stock we could buy
            max_nmbr = int(self.Budget/first_price)
            #a random number of stock between 0 and the max_nmbr is chosen
            nmbr_invested = random.randint(0, max_nmbr)
            #we add a line to our portfolio, stating the stock, the day of purchase and the number of stocks we buy
            inv_new = pd.DataFrame({'TYPE': [stock], 'PRICE': [first_price], 'Quantity': [nmbr_invested], 'Total Amount': [nmbr_invested*first_price], 'P_Date': [self.StartDate], 'S_Date': [self.EndDate], 'Return': [new_stock.stkCCReturn()]})
            tot_inv = [inv, inv_new]
            inv = pd.concat(tot_inv, axis=0)
            #our budget is reduced with the amount invested
            self.Budget = self.Budget - nmbr_invested*first_price
            self.Portfolio = inv
        return self.Portfolio



######################################################
#subclass 3
class Mixed(Investor):
    def __init__(self, Budget, StartDate, EndDate):
        Investor.__init__(self, Budget, StartDate, EndDate)
        self.Portfolio = []
        self.type = 'Mixed'

    #methods
    def investing(self):
        inv = pd.DataFrame()
        rows = len(inv)
        difference = self.EndDate - self.StartDate
        dif_in_years = (difference.days + difference.seconds / 86400) / 365.2425
        if rows == 0:
            # we define the top line of our dataframe in case it is the first investment
            inv = pd.DataFrame(columns=['TYPE', 'PRICE', 'Quantity', 'Total Amount', 'P_Date', 'S_Date', 'Return'])
        # investing will be done for as long as we have a budget >= the min amount needed for a ST bond
        stb = STBond(1,1)
        ltb = LTBond(1,1)
        while self.Budget >= stb.min_amount:
            if random.choice(['Stock', 'Bond']) == 'Bond':
                #the mixed investor decides to invest in a BOND and makes a random pick between Short and Long Term
                if random.choice(['LT', 'ST']) == 'LT':
                    #in case of long term, we define the line which we will add to the data frame by adding the details of the investment
                    inv_new = pd.DataFrame({'TYPE': ['LTBond'], 'PRICE': [ltb.premium], 'Quantity': [ltb.quantity], 'Total Amount': [ltb.quantity*ltb.min_amount], 'P_Date': [self.StartDate],'S_Date': [self.EndDate], 'Return': [stb.realized_return(dif_in_years)]})
                    tot_inv = [inv, inv_new]
                    inv = pd.concat(tot_inv, axis=0)
                    #the budget of the investor is reduced with the amount invested
                    self.Budget = self.Budget - ltb.min_amount*ltb.quantity
                    self.Portfolio = inv
                else:
                    # in the case of a short term bond, a similar tactic is applied but for the ST version
                    inv_new = pd.DataFrame({'TYPE': ['STBond'], 'PRICE': [stb.premium], 'Quantity': [stb.quantity], 'Total Amount': [stb.quantity * stb.min_amount], 'P_Date': [self.StartDate], 'S_Date': [self.EndDate], 'Return': [stb.realized_return(dif_in_years)]})
                    tot_inv = [inv, inv_new]
                    inv = pd.concat(tot_inv, axis=0)
                    self.Budget = self.Budget - stb.min_amount * stb.quantity
                    self.Portfolio = inv
            else:
                stock = random.choice(['AAPL', 'GOOGL', 'YHOO', 'AXP', 'XOM', 'KO', 'NOK', 'MS', 'IBM', 'FDX'])
                # an instance of class stock is initialized
                new_stock = Stock(self.StartDate, self.EndDate, stock)
                # we look for the price on the first day
                first_price = new_stock.getFirstPrice()
                # and thus determine how many stock we could buy
                max_nmbr = int(self.Budget / first_price)
                # a random number of stock between 0 and the max_nmbr is chosen
                nmbr_invested = random.randint(0, max_nmbr)
                r_r = new_stock.stkCCReturn()
                print(r_r)
                # we add a line to our portfolio, stating the stock, the day of purchase and the number of stocks we buy
                inv_new = pd.DataFrame({'TYPE': [stock], 'PRICE': [first_price], 'Quantity': [nmbr_invested], 'Total Amount': [nmbr_invested * first_price], 'P_Date': [self.StartDate], 'S_Date': [self.EndDate], 'Return': [new_stock.stkCCReturn()]})
                tot_inv = [inv, inv_new]
                inv = pd.concat(tot_inv, axis=0)
                # our budget is reduced with the amount invested
                self.Budget = self.Budget - nmbr_invested * first_price
                self.Portfolio = inv
        return self.Portfolio


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