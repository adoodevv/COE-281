mails = ['joe@gmail.com', 'darko@gmail.com', 'adoo@outlook.com']

print(mails) # original mail list

mails.sort() # sort alphabetically

mails.append('Peggy@gmail.com') # add new invitee

del mails[1] # remove one invited person

print(len(mails)) # number of nveited people

invited = []
for i in range(len(mails)):
   invited.append(mails[i].lower())

print(invited) # current list of invitees