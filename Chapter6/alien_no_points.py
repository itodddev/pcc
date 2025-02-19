
alien_0 = { 'color': 'green', 'speed': 'slow'}
# print(alien_0['points']) # Error not 'points' in dict

# Using get() to access values, second param is value to be returned if key doesnt exist
point_value = alien_0.get('points', 'No points value assigned.')
print(point_value)
