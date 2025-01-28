invite_to_party = ['kelli', 'ella', 'ruby']
print(f"{invite_to_party[0].title()} please come to my party")
print(f"{invite_to_party[1].title()} you are invited to my party")
print(f"{invite_to_party[2].title()} please come to my party")

print(invite_to_party)
print(f"{invite_to_party[-1]} cant make it")
invite_to_party.pop()
invite_to_party.append('pat')
print(invite_to_party)

print("More Guests Arriving")
print(invite_to_party)
invite_to_party.insert(0, 'jennifer')
middle = int(len(invite_to_party) / 2)
invite_to_party.insert(middle, 'liz')
invite_to_party.append('sam')

print("Sorry, only two guests for dinner")
print(invite_to_party)
uninvited = invite_to_party.pop()
print(f"Sorry, {uninvited} maybe next time")
uninvited = invite_to_party.pop()
print(f"Sorry, {uninvited} maybe next time")
uninvited = invite_to_party.pop()
print(f"Sorry, {uninvited} maybe next time")
uninvited = invite_to_party.pop()
print(f"Sorry, {uninvited} maybe next time")
print(f"\n{invite_to_party[0]} is still going")
print(f"{invite_to_party[1]} is still going")
del invite_to_party[1]
del invite_to_party[0]
print(invite_to_party)
