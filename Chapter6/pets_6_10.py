scooter = { 'name': 'scooter', 'kind': 'cat', 'owners_name': 'todd james' }
hammy = { 'name': 'hammy', 'kind': 'cat', 'owners_name': 'ruby james' }
shadow = { 'name': 'shadow', 'kind': 'cat', 'owners_name': 'ruby james' }
bushy = { 'name': 'bushy', 'kind': 'cat', 'owners_name': 'jenny james' }

pets = [scooter, hammy, shadow, bushy]

for pet in pets:
    print(f"Name: { pet['name'].title() }")
    print(f"Type: { pet['kind'].title() }")
    print(f"Owner: { pet['owners_name'].title() }")