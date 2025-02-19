rivers = { 'nile': 'egypt', 'amazon': 'south america', 'yangtze': 'eurasia' }

for river, country in rivers.items():
    print(f"The { river.title() } runs through { country.title() }")

print("Rivers: ")
for river in sorted(rivers.keys()):
    print(river.title())

print("Countries: ")
for country in sorted(rivers.values()):
    print(country.title())