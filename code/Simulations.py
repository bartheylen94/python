#---------------------------
# CLASS SIMULATION
# Authors: luca.fiorentino@iae-toulouse.fr , bart.heylen@iae-toulouse.fr
# Note:
#---------------------------
from Stock import Stock
import datetime
from Investor import Defensive
from Investor import Aggresive
from Investor import Mixed
import numpy as np


import radar
import pandas as pd
# start = datetime.datetime(2015, 1, 1)
# end = datetime.datetime(2015, 12, 31)
#
#
# stk=Stock(start, end, 'GOOGL')
# stk.ploStkPrice()
#list of input provided by the user


input_par=[]


input_par.append(datetime.datetime.strptime(input("Please define the starting date of the model (format dd/mm/yyyy)"), '%d/%m/%Y'))
input_par.append(datetime.datetime.strptime(input("Please define the ending date of the model (format dd/mm/yyyy)"), '%d/%m/%Y'))
inbudget=input("Which is the budget for each investors? If you want a random choise based on a normal distrinution type 'r' ")
if inbudget=='r':
    input_par.append(np.random.normal(20000,5000,1)[0])
else:
    input_par.append(float(inbudget))
input_par.append(input("How many defensive investors do you want in the model?"))
input_par.append(input("How many mixed investors do you want in the model?"))
input_par.append(input("How many agressive investors do you want in the model?"))

#Model execution
invmodel = pd.DataFrame()
rows = len(invmodel)
if rows == 0:
    #we define the top line of our dataframe in case it is the first investment
    invmodel = pd.DataFrame(columns=['TYPE', 'BUDGET', 'N_INVESTMENT', 'ABSOLUTE_RETURN', 'REL_RETURN'])
    #invmodel = pd.DataFrame(columns=['TYPE', 'BUDGET', 'N_INVESTMENT', 'ST_BOND_ALLOCATION', 'LT_BOND_ALLOCATION', 'STOCK_ALLOCATION', 'ABSOLUTE_RETURN', 'CCRETURN', 'VOLATILITY'])

#creation of difensive investors
for i in range(0, int(input_par[3])):
    definv=Defensive(input_par[2], input_par[0], input_par[1])
    definv.investing()
    newinv=pd.DataFrame({'TYPE': [definv.type], 'BUDGET': [input_par[2]], 'N_INVESTMENT': [len(definv.Portfolio)], 'ABSOLUTE_RETURN':[definv.Portfolio['AbsReturn'].sum()],'REL_RETURN':[(definv.Portfolio['AbsReturn'].sum()/input_par[2])-1]})
    #print(definv.Portfolio)
    conc=[invmodel, newinv]
    invmodel= pd.concat(conc, axis=0)
for i in range(0, int(input_par[5])):
    agrinv=Aggresive(input_par[2], input_par[0], input_par[1])
    agrinv.investing()
    newinv=pd.DataFrame({'TYPE': [agrinv.type], 'BUDGET': [input_par[2]], 'N_INVESTMENT': [len(agrinv.Portfolio)], 'ABSOLUTE_RETURN':[agrinv.Portfolio['AbsReturn'].sum()],'REL_RETURN':[(agrinv.Portfolio['AbsReturn'].sum()/input_par[2])-1]})
    conc = [invmodel, newinv]
    invmodel = pd.concat(conc, axis=0)
for i in range(0, int(input_par[4])):
    mixinv=Mixed(input_par[2], input_par[0], input_par[1])
    mixinv.investing()
    newinv=pd.DataFrame({'TYPE': [mixinv.type], 'BUDGET': [input_par[2]], 'N_INVESTMENT': [len(mixinv.Portfolio)], 'ABSOLUTE_RETURN':[mixinv.Portfolio['AbsReturn'].sum()],'REL_RETURN':[(mixinv.Portfolio['AbsReturn'].sum()/input_par[2])-1]})
    conc = [invmodel, newinv]
    invmodel = pd.concat(conc, axis=0)

print(invmodel)
dfanalysis=invmodel.groupby(by='TYPE').sum()
dfanalysis.drop('REL_RETURN', axis=1, inplace=True)
dfanalysis['REL_RETURN']=(dfanalysis['ABSOLUTE_RETURN']/dfanalysis['BUDGET'])-1
print(dfanalysis)