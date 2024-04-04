import math

c = int(input("Enter the length of the hypotenuse: "))
a = int(input("Enter the length of the adjacent side: "))

def findAngle():
   angle = math.acos(a/c)
   print(f"\nThe angle is {angle}")

def findAdjacent():
   b = math.sqrt(c**2 - a**2)
   print(f"\nThe length of the opposite side is {b}")

findAngle()
findAdjacent()