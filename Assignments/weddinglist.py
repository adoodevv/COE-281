emails = ['Joe@outlook.com', 'ME@gmail.com', 'koFi@gmail.com']
print(emails)

emails.sort()
print(emails)

emails.append('Mummy@gmail.com')
print(emails)

del emails[2]
print(emails)

print(len(emails))

emails.sort()
print(emails)

for mail in emails:
   print(mail.lower())