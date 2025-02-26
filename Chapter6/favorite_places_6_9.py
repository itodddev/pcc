favorite_places = {
    'todd': ['raleigh', 'new york', 'san francisco'],
    'ruby': ['cary', 'crab mall'],
    'jenny': ['new york', 'los angeles'],
}

for name, places in favorite_places.items():
    print(f"Name: { name.title() }")
    for place in places:
        print(place.title())
    print()