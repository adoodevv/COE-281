print("Give me two numbers to divide")
print("Press 'q' to exit")

while True:
   first_number = input("\nFirst number: ")
   if first_number == 'q':
      break
   second_number = input("Second number: ")
   if second_number == 'q':
      break
   try:
      result = int(first_number)/ int(second_number)
   except ZeroDivisionError:
      print("You cannot divide by zero!")
   else:
      print(f"The answer is {result}")