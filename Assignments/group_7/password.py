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
   print(password)

generate_password(12, use_uppercase=False, use_symbols=False, include_phrase='Hello')