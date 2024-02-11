# positional argument
def describe_pet(animal_type, pet_name):
   print(f"\nI have a {animal_type}")
   print(f"My {animal_type}'s name is {pet_name.title()}")

describe_pet('dog', 'kwame')
describe_pet('fish', 'melike')

# keyword arguments
def describe_pet(animal_type, pet_name):
   print(f"\nI have a {animal_type}")
   print(f"My {animal_type}'s name is {pet_name.title()}")

describe_pet(animal_type='cat', pet_name='george')

# default values
def describe_pet(pet_name, animal_type='dog'):
   print(f"\nI have a {animal_type}")
   print(f"My {animal_type}'s name is {pet_name.title()}")

describe_pet(pet_name='george')