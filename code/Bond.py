import matplotlib.pyplot as plt
import matplotlib

#initialize class BOND
class Bond(object):
    def __init__(self, min_term, min_amount, premium, i_rate):
        self.min_term = min_term
        self.min_amount = min_amount
        self.premium = premium
        self.i_rate = i_rate
    #specify properties
    #specify method(s)
        #compound return, yearly compounding

#define subclasses for short and long term bonds
class STBond(Bond):
    def __init__(self, inv_time, quantity):
        Bond.__init__(self, min_term=2, min_amount=1000, i_rate=0.01, premium=100)
        self.inv_time = inv_time
        self.quantity = quantity

    def compound_return(self):
        return ((1 + self.i_rate) ** (self.inv_time)-1)

    def yearly_coupon(self):
        comp_r = self.compound_return
        ycr = comp_r**(1/self.inv_time)
        return ycr*self.quantity


class LTBond(Bond):
    def __init__(self, inv_time, quantity):
        Bond.__init__(self, min_term=5, min_amount=3000, i_rate=0.03, premium=100)
        self.inv_time = inv_time
        self.quantity = quantity

    def compound_return(self):
        return ((1 + self.i_rate) ** (self.inv_time) - 1)

    def yearly_coupon(self):
        comp_r = int(self.compound_return)
        ycr = comp_r**(1/self.inv_time)
        return ycr*self.quantity

#plot the investment of the minimum allowed invested amount for both bonds over a period of 100 years
STlist=[]
LTlist=[]
for years in range(1, 101):
    STlist.append(STBond.compound_return(STBond(years, 1)))
    LTlist.append(LTBond.compound_return(LTBond(years, 1)))
print(LTlist)
y = range(1,101)
plt.plot(y, STlist)
plt.plot(y, LTlist)
plt.legend(['Short Term Bond', 'Long Term Bond'], loc='upper left')
plt.ylabel('return')
plt.xlabel('years')
plt.show()


