### Murchant Class ###
import random

class MerchantNPC():
    def __init__(self, name, trade1, trade2, trade3, trade4):
        self.name = name
        self.trade1 = trade1
        self.trade2 = trade2
        self.trade3 = trade3 
        self.trade4 = trade4


def generate_merchants():
    names = ["Hugo", "Conroy", "Ethad", "Ejiha"]
    merchants = []
    for i in range(0,300):
        merchant = MerchantNPC(names[random.randint(0,len(names)-1)], 
                            random.randint(60, 120), 
                            random.randint(60,120), 
                            random.randint(60,120), 
                            random.randint(100,300))
        merchants.append(merchant)
    return(merchants)
