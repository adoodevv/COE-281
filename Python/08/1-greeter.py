def greet_user():
   print("Hello!")

greet_user()

# passing a value to a function
def greet_user(username):
   print(f"Hello, {username.title()}!")

greet_user('joe')