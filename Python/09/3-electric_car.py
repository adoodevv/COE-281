class Car:
   def __init__(self, make, model, year):
      self.make = make
      self.model = model
      self.year = year
      self.odometer_reading = 0 # setting a default value for an attribute

   def get_descriptive_name(self):
      long_name = f"{self.year} {self.make} {self.model}"
      return long_name.title()
   
   def read_odometer(self):
      print(f"This car has {self.odometer_reading} miles on it")
   
   def update_odometer(self, mileage):
      if mileage >= self.odometer_reading:
         self.odometer_reading = mileage
      else:
         print("You can't roll back an odometer!")

   def increment_odometer(self, miles):
      self.odometer_reading += miles

# Inheritance
class ElectricCar(Car):
   def __init__(self, make, model, year):
      super().__init__(make, model, year) # initializing attributes of the parent class
      self.battery_size = 75 # adding new attributes to the child class

   def describe_battery(self): # adding new methods to the child class
      print(f"This car has a {self.battery_size}-kWh battery")

my_tesla = ElectricCar('tesla', 'model s', 2019)
print(my_tesla.get_descriptive_name())
my_tesla.describe_battery()

# Composition
"""In these situations, you might recognize that part of one class can 
be written as a separate class. You can break your large class into smaller 
classes that work together"""