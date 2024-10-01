#Zachary LaMar
#9/26/24
#P2Lab1
#Calculate diameter, circumference and area of a circle with a given radius

import math

#Get the radius and calculate diameter then print it
radius=float(input("What is the radius of the circle? "))
diameter=radius*2
print(f"The diameter of the circle is {diameter:.1f}")

#Calculate circumference
circ=2*math.pi*radius
print(f"The circumference of the circle is {circ:.2f}")

#Calculate area
area=math.pi*radius**2
print(f"The area of the circle is {area:.3f}")
