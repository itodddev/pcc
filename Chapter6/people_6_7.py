
people = [
    {'first_name': 'todd', 'last_name': 'james', 'age': 56, 'city': 'raleigh'},
    {'first_name': 'jenny', 'last_name': 'james', 'age': 48, 'city': 'cary'},
    {'first_name': 'ruby', 'last_name': 'james', 'age': 12, 'city': 'cary'},
]
for person in people:
    print(f"Name: { person['first_name'].title() } { person['last_name'].title() }")
    print(f"Age: { person['age'] }")
    print(f"City: { person.get('city', 'N/A').title() }")