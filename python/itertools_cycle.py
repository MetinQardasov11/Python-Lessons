from itertools import cycle

players = ('Ebubekir', 'Omer', 'Osman', 'Ali')

data = {p: [] for p in players}

for x in cycle(players):
    text = input(f'Players {x}: ')
    if text == 'stop':
        break
    
    data[x].append(text)
    
print(data)