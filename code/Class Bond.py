#initialize class BOND
class Bond(object):
    #specify properties
    def __init__(self, min_term, i_rate, min_amount):
        self.min_term = min_term
        self.min_amount = min_amount
        self.i_rate = i_rate

        #specify method(s)
    def compound_return(self, term, i_rate):
        return ((1+i_rate)**term)-1)

#define subclasses for short and long term bonds
class STBond(Bond):
    def __init__(self, min_term, min_amount):
        self.min_term = 2
        self.min_amount = 1000

class LTBond(Bond):
    def __init__(self, min_term, min_amount):
        self.min_term = 5
        self.min_amount = 3000
