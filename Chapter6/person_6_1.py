person = { 'first_name': 'todd', 'last_name': 'james', 'age': 56, 'city': 'raleigh'}

print(f"Name: { person['first_name'].title() } { person['last_name'].title() }")
print(f"Age: { person['age'] }")
print(f"City: { person.get('city', 'N/A').title() }")