from pathlib import Path # Import the Path class from the pathlib module.

path = Path('Python/10/pi_digits.txt') # Create a Path object that points to the file you want to read.
contents = path.read_text() # Read the contents of the file and store them as a string in contents.
lines = contents.splitlines() # Split the contents of the file on the newline character to get a list of lines from the file.
for line in lines:
   print(line)