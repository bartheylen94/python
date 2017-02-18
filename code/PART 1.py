#initialize class BOND
class Bond(object):
    #specify properties
    def __init__(self, term, amount_inv, i_rate):
        self.term = term
        self.amount_inv = amount_inv
        self.i_rate = i_rate

        #specify method(s)
    def inv_return(self, term, amount_inv, i_rate):
        return (amount_inv*(1 + i_rate)**(term))

    def compound_return(self, term, i_rate):
        return ((1+i_rate)**term)-1)

class STBond(Bond):
    def __init__(self, min_term, min_amount):
        self.min_term = 2
        self.min_amount = 1000

class LTBond(Bond):
    def __init__(self, min_term, min_amount):
        self.min_term = 5
        self.min_amount = 3000
