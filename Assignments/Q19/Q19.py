print("Enter the cordinates of the point: ")
x1 = int(input("Enter the x-coordinate: "))
y1 = int(input("Enter the y-coordinate: "))

def functQuad():
   if x1 > 0 and y1 > 0:
      print(f"\nThe point ({x1},{y1}) lies in the first quadrant")
   elif x1 < 0 and y1 > 0:
      print(f"\nThe point ({x1},{y1}) lies in the second quadrant")
   elif x1 < 0 and y1 < 0:
      print(f"\nThe point ({x1},{y1}) lies in the third quadrant")
   elif x1 > 0 and y1 < 0:
      print(f"\nThe point ({x1},{y1}) lies in the fourth quadrant")
   else:
      print(f"\nUndefined quadrant")

def XReflect():
   print(f"\nThe reflection of the point across the x-axis is ({x1},{-y1})")

def YReflect():
   print(f"\nThe reflection of the point across the y-axis is ({-x1},{y1})")

def functSlope():
   slope = (-5 - y1) / (5 - x1)
   print(f"\nThe slope of the line is {slope}")

functQuad()
XReflect()
YReflect()
functSlope()