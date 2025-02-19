from shapely.speedups import available

requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']

for requested_topping in requested_toppings:
    if requested_topping == 'green peppers':
        print('Sorry we are out of green peppers right now')
    else:
        print(f"Adding {requested_topping}")

print("Finished making your pizza")

# Make sure a list isnt empty

requested_toppings = []

if requested_toppings: # If nothing in list skip adding toppings
    for requested_topping in requested_toppings:
        print(f"Adding {requested_topping}")

    print("Finished making your pizza")
else:
    print("Are you sure you want a plain cheese pizza")

# Multiple lists

available_toppings = ['mushrooms', 'olives', 'green peppers', 'extra cheese', 'pepperoni', 'pineapple']

requested_toppings = ['mushrooms', 'french fries', 'extra cheese']

for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print(f"Adding {requested_topping}")
    else:
        print(f"Sorry, we don't have { requested_topping }")

print("Finished making your pizza")