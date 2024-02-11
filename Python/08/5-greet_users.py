def greet_users(names):
   for name in names:
      msg = f"Hello, {name.title()}!"
      print(msg)

usernames = ['joe', 'adoo', 'darko']
greet_users(usernames)