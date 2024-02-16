current_users = ['adoo_2', 'nk42', 'singleton_1', 'kojo21', 'yourock']
new_users = ['pegg78', 'shot45', 'nk41', 'kojo21', 'masa']
index = 0

for new_user in new_users:
   current_user = current_users[index]
   if new_user == current_user:
      print(f"Enter a new name, {new_user} not available")
   else:
      print(f"{new_user} is available")
      index += 1