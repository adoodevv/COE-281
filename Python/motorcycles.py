motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

#modifying items in a list
motorcycles[0] = 'ducati' #modifying first item
print(motorcycles)

#adding elements to a list
motorcycles.append('honda')
print(motorcycles)

#inserting elements into list
motorcycles = ['honda', 'yamaha', 'suzuki']
motorcycles.insert(0, 'red bull')
print(motorcycles)

#removing items from a list
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
del motorcycles[1]
print(motorcycles)

#removing items using the pop() method
#this method allows you to work with the removed item after removing it
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
popped_motorcycle = motorcycles.pop()
print(motorcycles)
print(popped_motorcycle)