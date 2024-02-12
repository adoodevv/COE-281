# pass an arbitrary number of arguments
def make_pizza(*toppings):
   print(f"\nMaking a pizza with the following ingredients:")
   for topping in toppings:
      print(f"- {topping}")

make_pizza('pepperoni')
make_pizza('mushrooms', 'green pepper', 'extra cheese')

# mixing arbitrary arguments and positional arguments
# arbitrary argument should come last
def make_pizza(size, *toppings):
   print(f"\nMaking a {size}-inch pizza with the following ingredients:")
   for topping in toppings:
      print(f"- {topping}")

make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')