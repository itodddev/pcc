my_foods = ['pizza', 'falafel', 'carrot cake']
friends_foods = my_foods[:] # Copies the list [:] copies all the elements

print('My favorite foods are:')
print(my_foods)
my_foods.append('Italian Sub')
print(my_foods)

print('\nMy friends favorite foods are:')
print(friends_foods)
friends_foods.append('Salad')
print(friends_foods)

friends_foods = my_foods
print('\nWhen list is assigned and not copied')
print(friends_foods)