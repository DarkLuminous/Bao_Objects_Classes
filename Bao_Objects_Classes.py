import os
import math

while True:
    class circle:
        def __init__(self, rad):
            self.rad= rad
    
        def area(self):
            Cir_area = math.pi * self.rad ** 2
            print(f"\nArea = {Cir_area:.2f}")
        
        def parimeter(self):
            Cir_area = 2 * math.pi * self.rad
            print(f"Parimeter = {Cir_area:.2f}")
            

    rad = float(input("[0] = End the Program \nEnter Radius: "))
    
    if rad == float(0):
       exit()

    circle = circle(rad)
        

    circle.area()
    circle.parimeter()
    input("\n\n[Press Enter] To Continue . . .")
    os.system('cls')