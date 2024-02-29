from pathlib import Path

def count_words(filename):
   try:
      contents = path.read_text(encoding='utf-8')
   except FileNotFoundError:
      pass
   else:
      words = contents.split()
      num_words = len(words)
      print(f"The file {path} has about {num_words} words.")

filenames = ['alice.txt', 'siddhartha.txt', 'moby_dick.txt', 
 'little_women.txt']
for filename in filenames:
   path = Path(f"Python/10/{filename}")
   count_words(path)