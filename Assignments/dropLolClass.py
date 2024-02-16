current_users = ['adoo_2', 'nk42', 'singleton_1', 'kojo21', 'yourock']
new_users = ['pegg78', 'shot45', 'nk42', 'kojo21', 'masa']

for new_user in new_users:
    if new_user in current_users:
        print(f"Enter a new name, {new_user} not available")
    else:
        print(f"{new_user} is available")


#FizzBuzz
for number in range(101):
   print(number)
   
numbers = range(101)
for number in numbers:
   if (number % 3 == 0) and (number % 5 == 0):
      print('FizzBuzz')
   elif number % 3 == 0:
      print('Fizz')
   elif number % 5 == 0:
      print('Buzz')
   else:
      print('none')