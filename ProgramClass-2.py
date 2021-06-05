class bike:
    
    def __init__(self,color,price):
        self.clr = color
        self.prc = float(price)
    
    def specification(self):
        print("Bike Color:",self.clr)
        print("Bike Price:",self.prc)

testone = bike("Blue",89.99)    
testtwo = bike("Purplr",25.0)

testone.specification()
testtwo.specification()

# Bike Color: Blue
# Bike Price: 89.99
# Bike Color: Purplr
# Bike Price: 25.0