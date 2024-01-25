# Tuples
# An immutable list is called a tuple
dimensions = (200, 50)
print(dimensions[0])
print(dimensions[1])

for dimension in dimensions:
 print(dimension)

# writing over a tuple
dimensions = (200, 50)
print("Original dimensions:")
for dimension in dimensions:
 print(dimension)
dimensions = (400, 100)
print("\nModified dimensions:")
for dimension in dimensions:
 print(dimension)