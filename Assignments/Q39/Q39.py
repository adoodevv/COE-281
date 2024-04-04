import math

a = int(input("Enter the value of a: "))
b = int(input("Enter the value of b: "))
c = int(input("Enter the value of c: "))

condition = (3 * a**4) - b**3 

if condition >= 0:
   print("we are good to go")

   def functEquation1():
      ans = (b ** 2 - math.log(3 * a)) / math.sqrt(condition)
      print(f"functEquation1 returns {ans}")

   def functEquation2():
      ans = (b ** 2 + math.log(3 * a)) / math.sqrt(condition)
      print(f"functEquation2 returns {ans}")

   functEquation1()
   functEquation2()

else:
   print("let's  call it a day")