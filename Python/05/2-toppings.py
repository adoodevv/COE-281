requested_toppings = 'mushrooms'

if requested_toppings != 'anchovies': # inequality check
   print("Hold the anchovies")

requested_toppings = ['mushrooms', 'extra cheese']
if 'mushrooms' in requested_toppings:
   print("Adding mushrooms.")
if 'pepperoni' in requested_toppings:
   print("Adding pepperoni.")

requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']
for requested_topping in requested_toppings:
   print(f"Adding {requested_topping}.")

print("\nFinished making your pizza!")