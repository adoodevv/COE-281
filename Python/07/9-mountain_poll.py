responses = {}

polling_active = True

while polling_active:
   name = input("\nWhat is your name? ")
   response = input("Which mountain would you like to climb someday? ")

   responses[name] = response

   end = input("Would you like to let another person respond? (yes/ no) ")

   if end == 'no':
      polling_active = False

print("\n--- Poll Results ---")
for name, mountain in responses.items():
   print(f"{name.title()} would like to climb {mountain.title()}")