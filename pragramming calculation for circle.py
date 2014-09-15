#jAunik Hussain
#variable improvement exercise
#05-09-12

import math

r = float(input("please enter the radius of the circle: "))

circumference = 2* math.pi * r
circumference = round(circumference,2)

area = math.pi * r**2
area = round(area,2)

print("The circumference of this circle is {0}.".format(circumference))
print("The area of this circle is {0}.".format(area))
