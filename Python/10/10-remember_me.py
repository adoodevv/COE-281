from pathlib import Path
import json

username = input("What is your name? ")

path = Path('Python/10/username.json')
content = json.dumps(username)
path.write_text(content)

print(f"We'll remember you when you come back, {username}!")