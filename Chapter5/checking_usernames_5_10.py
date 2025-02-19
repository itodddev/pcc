current_users = ['tjames', 'kgray', 'ewaller', 'admin', 'epollard']
new_users = ['mherold', 'ewaller', 'mbanner', 'kgray']

for new_user in new_users:
    if new_user in current_users:
        print(f"Sorry {new_user} is already used")
    else:
        print(f"{new_user} is available")