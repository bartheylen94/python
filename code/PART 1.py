#initialize class BOND
class Bond(object):
    #specify properties
    def __init__(self, term):
        self.term = term

    def __init__(self, amount_inv):
        self.amount_inv = amount_inv

    def __init__(self, min_price):
        self.min_price = min_price

    def __init__(self,min_term):
        self.min_term = min_term

    def __init(self,i_rate):
        self.i_rate = i_rate


     #specify method(s)
    def inv_return(self, term, amount_inv, i_rate):
        return (amount_inv*(1 + i_rate)**(term))

    def compound_return(self, term, amount_inv, i_rate):
        total = inv_return(self, term, amount_inv, i_rate)
        return ((total/amount_inv)**(1/term)-1)
