def make_pizza(size, *toppings):
   print(f"\nMaking a {size}-inch pizza with the following ingredients:")
   for topping in toppings:
      print(f"- {topping}")