#sort list permanently
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort() #alphabetical order
print(cars)

cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort(reverse=True) #reverse alphabetical order
print(cars)

#length of list with len function
cars = ['bmw', 'audi', 'toyota', 'subaru']
print(len(cars))

# if statements
for car in cars:
   if car == 'bmw':
      print(car.upper())
   else:
      print(car.title())