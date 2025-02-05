# Tuples - immutable lists- uses () not []

dimensions = ( 200, 50 )
print(dimensions[0])
print(dimensions[1])

# dimensions[0] = 250 - Can't assign a new value to a tuple

# Looping
for dimension in dimensions:
    print(dimension)

# You can't modify a tuple but you can reassign one

print("Original dimensions: ")
for dimension in dimensions:
    print(dimension)

dimensions = (400, 100)
print("Modified dimensions: ")
for dimension in dimensions:
    print(dimension)
