from pathlib import Path

path = Path('Python/10/programming.txt')

content = 'I love programming\n'
content += 'I love building webpages\n'
content += 'I also love building robots\n'

path.write_text(content)