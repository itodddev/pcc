invite_to_party = ['kelli', 'ella', 'ruby']
print(f"{invite_to_party[0].title()} please come to my party")
print(f"{invite_to_party[1].title()} you are invited to my party")
print(f"{invite_to_party[2].title()} please come to my party")

print(invite_to_party)
print(f"{invite_to_party[-1]} cant make it")
invite_to_party.pop()
invite_to_party.append('pat')
print(invite_to_party)  
print(f"New list of guests: {invite_to_party}")