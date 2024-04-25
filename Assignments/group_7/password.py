import string
import random

def generate_password(length, use_uppercase=True, use_lowercase=True, use_digits=True, use_symbols=True, include_phrase=None):
   characters = ''
   if use_uppercase:
      characters += string.ascii_uppercase
   if use_lowercase:
      characters += string.ascii_lowercase
   if use_digits:
      characters += string.digits
   if use_symbols:
      characters += string.punctuation
   password = include_phrase if include_phrase else ''
   while len(password) < length:
      password += random.choice(characters)
   print(f"\nYour generated password is: {password}")

while True:
   try:
      length = int(input("Enter the length of the password: "))
      break
   except ValueError:
      print("Invalid input. Please enter a number.")

while True:
   use_uppercase = input("Include uppercase letters? (y/n): ").lower()
   if use_uppercase in ['y', 'n']:
      use_uppercase = use_uppercase == 'y'
      break
   else:
      print("Invalid input. Please enter 'y' or 'n'.")

while True:
   use_lowercase = input("Include lowercase letters? (y/n): ").lower()
   if use_lowercase in ['y', 'n']:
      use_lowercase = use_lowercase == 'y'
      break
   else:
      print("Invalid input. Please enter 'y' or 'n'.")

while True:
   use_digits = input("Include digits? (y/n): ").lower()
   if use_digits in ['y', 'n']:
      use_digits = use_digits == 'y'
      break
   else:
      print("Invalid input. Please enter 'y' or 'n'.")

while True:
   use_symbols = input("Include symbols? (y/n): ").lower()
   if use_symbols in ['y', 'n']:
      use_symbols = use_symbols == 'y'
      break
   else:
      print("Invalid input. Please enter 'y' or 'n'.")

while True:
   include_phrase = input("Include a phrase? (y/n): ").lower()
   if include_phrase in ['y', 'n']:
      include_phrase = include_phrase == 'y'
      if include_phrase:
         include_phrase = input("Enter the phrase: ")
      break
   else:
      print("Invalid input. Please enter 'y' or 'n'.")

generate_password(length, use_uppercase,use_lowercase,use_digits, use_symbols, include_phrase)