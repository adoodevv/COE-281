import math

print("Enter the first point: ")
x1 = int(input("Enter the x-coordinate: "))
y1 = int(input("Enter the y-coordinate: "))

print("\nEnter the second point: ")
x2 = int(input("Enter the x-coordinate: "))
y2 = int(input("Enter the y-coordinate: "))

distance,slope, y_intercept = 0,0,0

def functDistance():
   distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
   print(f"\nthe distance between the two points is {distance}")

def functSlope():
   slope = (y2 - y1) / (x2 - x1)
   print(f"the slope of the line is {slope}")

def functEquation():
   slope = (y2 - y1) / (x2 - x1)
   y_intercept = y1 - slope * x1
   print(f"the equation of the line is y = {slope}x + {y_intercept}")

functDistance()
functSlope()
functEquation()