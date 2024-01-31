alien_0 = {'color': 'green', 'points': 5}

print(alien_0['color']) # reading data from dictionary
print(alien_0['points'])

new_points = alien_0['points']
print(f"You just earned {new_points} points!")

# adding new key-value pairs
alien_0 = {'color': 'green', 'points': 5}
print(alien_0)

alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)

# modifying values in dictionary
alien_0 = {'color': 'green'}
print(f"The alien is {alien_0['color']}.")

alien_0['color'] = 'yellow'
print(f"The alien is now {alien_0['color']}.")

# determine alien position based on speed
alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'slow'}
print(f"Original position: {alien_0['x_position']}")

if alien_0['speed'] == 'slow':
   x_increment = 1
elif alien_0['speed'] == 'medium':
   x_increment = 2
else:
   x_increment = 3

alien_0['x_position'] = alien_0['x_position'] + x_increment

print(f"New positon: {alien_0['x_position']}")