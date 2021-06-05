class  applebasket:
    
    def __init__(self,apple_color,apple_quantity):
        self.apco = apple_color
        self.apqu = int(apple_quantity)

    def inc(self):
        self.apqu = self.apqu+1
        print("Increased Quantity:",self.apqu)

    def __str__(self):
        print("A basket of",self.apqu,self.apco,"apples")

Buyer1 = applebasket("Red",49)
Buyer1.__str__()
Buyer1.inc()

# A basket of 49 Red apples

# A basket of 49 Red apples
# Increased Quantity: 50
                       