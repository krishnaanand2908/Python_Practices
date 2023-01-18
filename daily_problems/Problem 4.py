# Write a Python program that calculates the area of a circle based on the radius entered by the user. Go to the editor
# Sample Output :
# r = 1.1
# Area = 3.8013271108436504

# My solution:
radius = float(input("Enter the radius of your circle: "))
PI =  3.14159 #3.141592653589793238
print(f"Area of the circle with radius {radius} unit is {PI*(radius**2)} unit square")

#Sample solution:
from math import pi
r = float(input ("Input the radius of the circle : "))
print ("The area of the circle with radius " + str(r) + " is: " + str(pi * r**2))
