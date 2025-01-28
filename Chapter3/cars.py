cars =['bmw', 'audi', 'toyota', 'subaru']
print(cars)
cars.sort() # destructive sort, changes original list
print(cars)
cars.sort(reverse=True)
print(cars) # reverse sort

# Temporary sort
print('Temporary Sort: ')
cars =['bmw', 'audi', 'toyota', 'subaru']
print(cars)
temp = sorted(cars)
print(temp)
#print(sorted(cars))
print(cars)

cars.reverse() # destructive - permanently reverses list
print(cars)  # Just prints the list in reverse order, doesnt sort reverse alphabetically

print(f"Number of cars: { len(cars) }")
