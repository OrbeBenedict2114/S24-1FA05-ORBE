# REFLECTION:
# Using a library is more practical than writing calculations from scratch because it saves time, 
# prevents errors, and optimizes performance with pre-tested functions. For example, instead of 
# writing a complex algorithm to manually calculate a square root, importing math.sqrt() allows us 
# to compute it reliably in a single line of code.

import math
# input the 2 points on the 2d plane
x1 = float(input("Enter x1: "))
y1 = float(input("Enter y1: "))
x2 = float(input("Enter x2: "))
y2 = float(input("Enter y2: "))
# The Formula/Equation
distance = math.sqrt(math.pow(x2 - x1, 2) + math.pow(y2 - y1, 2))
# The Final Answer/The distance between both points
print(f"\nThe distance between the two points is: {distance:.2f}")
