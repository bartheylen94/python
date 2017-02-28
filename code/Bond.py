#---------------------------
# CLASS BOND
# Authors: luca.fiorentino@iae-toulouse.fr , bart.heylen@iae-toulouse.fr
# Note:
#---------------------------



#initialize class BOND
class Bond(object):
    def __init__(self, min_term, min_amount, premium, i_rate):
        self.min_term = min_term
        self.min_amount = min_amount
        self.premium = premium
        self.i_rate = i_rate


#define subclasses for short and long term bonds
class STBond(Bond):
    def __init__(self, inv_time, quantity):
        Bond.__init__(self, min_term=2, min_amount=1000, i_rate=0.01, premium=100)
        self.inv_time = inv_time
        self.quantity = quantity

    def realized_return(self, inv_length):
        return (((1 + self.i_rate) ** (inv_length)))

    def compound_return(self):
        return (((1 + self.i_rate) ** (self.inv_time))-1)

class LTBond(Bond):
    def __init__(self, inv_time, quantity):
        Bond.__init__(self, min_term=5, min_amount=3000, i_rate=0.03, premium=100)
        self.inv_time = inv_time
        self.quantity = quantity

    def realized_return(self, inv_length):
        return (((1 + self.i_rate) ** (inv_length)))

    def compound_return(self):
        return (((1 + self.i_rate) ** (self.inv_time)) - 1)



