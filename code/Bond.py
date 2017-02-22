#initialize class BOND
class Bond(object):
    #specify properties
    def __init__(self, min_term, i_rate, min_amount, inv_time, quantity, premium):
        self.min_term = min_term
        self.min_amount = min_amount
        self.i_rate = i_rate
        self.inv_term = inv_time    #expressed in days; 360 per year
        self.quantity = quantity
        self.premium = premium

    #specify method(s)
        #compound return, yearly compounding
    def compound_return(self):
        return ((1+self.i_rate)**(self.inv_term/360)-1)

    def yearly_coupon(self):
        comp_r = float(self.compound_return)
        ycr = comp_r**(1/self.inv_term)
        return ycr*self.quantity


#define subclasses for short and long term bonds
class STBond(Bond):
    def __init__(self, i_rate, inv_time, quantity, premium, min_term=2, min_amount=1000,):
        Bond.__init__(self, min_term, i_rate, min_amount, premium, inv_time, quantity)
        self.min_term = min_term
        self.min_amount = min_amount
        self.premium = premium
class LTBond(Bond):
    def __init__(self, i_rate, inv_time, premium, quantity, min_term=5,  min_amount=3000):
        Bond.__init__(self, min_term, i_rate, premium, min_amount, inv_time, quantity)
        self.min_term = min_term
        self.min_amount = min_amount
        self.premium = premium
