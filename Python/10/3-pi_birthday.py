from pathlib import Path

path = Path('Python/10/pi_digits.txt')
contents = path.read_text()

lines = contents.splitlines()
pi_string = ''
for line in lines:
   pi_string += line.lstrip()

birthday = input('Enter your birthday in the order mmddyy: ')
if birthday in pi_string:
   print("Your birthday is in the first million digits of pi!")
else:
   print("Your birthday does not appear in the first million digits of pi.")