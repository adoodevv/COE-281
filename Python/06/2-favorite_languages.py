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