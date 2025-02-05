players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[0:3]) # prints first 3 players
print(players[1:4]) # prints 2nd, 3rd, 4th
print(players[:4]) # print 1..4, starts at index 0 if omitted
print(players[2:]) # prints 3rd item to the end

# Looping through a slice
print('\nHere are the first three players:')
for player in players[:3]:
    print(player.title())