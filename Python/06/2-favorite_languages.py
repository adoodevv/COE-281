favorite_languages = {
   'jen': 'python',
   'sarah': 'c',
   'edward': 'rust',
   'phil': 'python',
}

language = favorite_languages['sarah'].title()
print(f"Sarah's favorite language is {language}.")

#looping through dictionary
for name, language in favorite_languages.items():
   print(f"{name.title()}'s favorite language is {language.title()}.")

#looping through keys in a dictionary
for name in favorite_languages.keys():
   print(name.title())

#looping through a dictionary's keys in a particular order
favorite_languages = {
   'jen': 'python',
   'sarah': 'c',
   'edward': 'rust',
   'phil': 'python',
}

for name in sorted(favorite_languages.keys()):
   print(f"{name.title()}, thank you for taking the poll.")

# list in a dictionary
favorite_languages = {
   'jen': ['python', 'rust'],
   'sarah': ['c'],
   'edward': ['rust', 'go'],
   'phil': ['python', 'haskell']
}

for name, languages in favorite_languages.items():
   print(f"\n{name.title()}'s favorite languages are: ")
   for language in languages:
      print(f"\t{language}")