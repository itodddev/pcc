my_pizzas = ['pepperoni', 'sausage', 'hamburger']
friends_pizzas = my_pizzas[:]

friends_pizzas.append('cheese')

print(f"My pizzas:")
for pizza in my_pizzas:
    print(pizza.title())

print()

print(f"Friends pizzas:")
for pizza in friends_pizzas:
    print(pizza.title())