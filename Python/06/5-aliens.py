alien_0 = {'color' : 'green', 'points' : 5}
alien_1 = {'color' : 'yellow', 'points' : 10}
alien_2 = {'color' : 'red', 'points' : 15}

aliens = [alien_0, alien_1, alien_2]

for alien in aliens:
   print(alien)

#automatically generate aliens
aliens = []

for alien_number in range(30):
   new_alien = {'color' : 'green', 'points' : 5, 'speed' : 'slow'}
   aliens.append(new_alien)

#show first 5 aliens
for alien in aliens[:5]:
   print(alien)
print('...')
print(f"Total number of aliens: {len(aliens)}")