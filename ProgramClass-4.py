/usr/bin/python3
""" Write a class that represents a Planet. The constructor class should accept the arguments radius (in meters) and rotation_period (in seconds). """
""" You should implement three methods: surface_area rotation_frequency. """


class planet:
    def __init__(self,radius,rotation_period):
        self.rdm = radius
        self.rps = rotation_period

    def surface_area(self):
        surf = (4*3.14*self.rdm*self.rdm)
        print("Surface Area",int(surf),"Sqm")

    def rotation_frequency(self):
        rfs = 2*3.14/self.rps
        print("Rotation Frequency "+str(rfs)+"/s")

Area = int(input("Radius of Planet="))
Frequency = int(input("Rotation Period Of Planet="))

Dimensions = planet(Area,Frequency) 
Dimensions.surface_area()
Dimensions.rotation_frequency()

# Surface Area  3629 Sqm
# Rotation Frequency 2.0933333333333333/s
