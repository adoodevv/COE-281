from pathlib import Path
import json

def get_stored_username():
   path = Path('Python/10/username.json')
   try:
      content = path.read_text()
      username = json.loads(content)
   except FileNotFoundError:
      return None
   else:
      return username
   
def get_new_username():
   path = Path('Python/10/username.json')
   username = input("What is your name? ")
   path.write_text(json.dumps(username))
   return username

def greet_user():
   path = Path('Python/10/username.json')
   username = get_stored_username()
   if username:
      print(f"Welcome back {username}!")
   else:
      username = get_new_username()
      print(f"We'll remember you when you come back, {username}!")

greet_user()