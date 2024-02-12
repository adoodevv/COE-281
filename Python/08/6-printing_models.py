def print_models(unprinted_designs, completed_models):
   while unprinted_designs:
      current_design = unprinted_designs.pop()
      print(f"Printing model: {current_design}")
      completed_models.append(current_design)

def show_completed_models(completed_models):
   print("\nThe following models have been printed:")
   for completed_model in completed_models:
      print(completed_model)

unprinted_designs = ['phone case', 'plate', 'cube']
completed_models = []

print_models(unprinted_designs, completed_models)
show_completed_models(completed_models)

# make a copy of a list
# function_name(list_name[:])

hi = [1, 2, 3, 3]
copy_hi = hi[:]

print(f"original list is {hi} and copied list is {copy_hi}")