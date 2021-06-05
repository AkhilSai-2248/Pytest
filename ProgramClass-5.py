/usr/bin/python3
class point:
    def __init__(self):
        self.xo = 0
        self.yo = 0

class initialize(point):
    
    def distance(self,x_co,y_co):         
        self.x = x_co
        self.y = y_co
        DOPOF  = ((self.x-self.xo)**2+(self.y-self.xo)**2)**0.5
        print("Distance from Origin",DOPOF)

x_co = int(input("Enter X-Coordinates="))
y_co = int(input("Enter Y-Coordinates="))

Dis = initialize()
Dis.distance(x_co,y_co)
