motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

#motorcycles[0] = 'ducati'
#print(motorcycles)

motorcycles.append('ducati')
print(motorcycles)

motorcycles.insert(0, 'BMW')
print(motorcycles)

# two ways to remove items from a list
del motorcycles[0] # removes item at index
deleted_motocycle = motorcycles.pop() # removes last item and place in variable
first_motorcycle = motorcycles.pop(0) # You can also pop with an index number
print(motorcycles)
print(f"{deleted_motocycle} was removed")
print(f"{first_motorcycle} was my first motocycle")

# removing an item by value
motorcycles.remove('suzuki')
print(motorcycles)

# if you need to retain the value
# * .remove() only removes the first instance, if there are multiple you will have
# to loop through the list
too_yellow = 'yamaha'
motorcycles.remove(too_yellow)
print(motorcycles)
print(f"The {too_yellow} was too yellow")