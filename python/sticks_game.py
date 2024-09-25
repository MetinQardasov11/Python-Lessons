import itertools

player1 = input('Enter the player1 name: ')
player2 = input('Enter the player2 name: ')
players = (player1, player2)

def lines(count, stick='|'):
    return [stick for i in range(count)]


def show_lines(data_list, sep='.'):
    return sep.join(data_list) + f' >> {len(data_list)}'


def delete_lines(data_list, count):
    return data_list[:-count]

player_turn = itertools.cycle(players)
sticks = lines(15)

print('\n')
print(' 15 STICKS GAME '.center(40, '='))
print(show_lines(sticks) + '\n\n')

while len(sticks) > 1:
    player = next(player_turn)
    delete_count = int(input(f'✅{player}: '))
    
    if delete_count not in (1, 2, 3, 4):
        print('Enter a valid number!')
        player = next(player_turn)
        continue
    
    if len(sticks) <= 4 and delete_count >= len(sticks):
        print('Enter a valid number!')
        player = next(player_turn)
        continue
    
    sticks = delete_lines(sticks, delete_count)
    print(show_lines(sticks) + '\n')
    if len(sticks) == 1:
        print(f'{player} wins!')