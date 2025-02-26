users = {
    'aeinstein': {
        'first': 'albert',
        'last': 'einstein',
        'location': 'princeton'
    },

    'mcurie': {
        'first': 'marie',
        'last': 'curie',
        'location': 'paris'
    }
}

for username, user_info in users.items():
    print(f"\nUsername: { username }")
    full_name = f"{ user_info['first'] } { user_info['last'] }"
    print(f"Full name: { full_name.title() }")
    print(f"Location: { user_info['location'].title() }")