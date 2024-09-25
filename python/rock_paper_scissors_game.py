from random import randint

rpc = {
    1: "🪨",
    2: "📑",
    3: "✂️"
}

rules = {
    1: {1, 3},
    2: {1, 2},
    3: {2, 3},
}

player1, player2 = 'Metin', 'Computer'
select_one = [f'{x} {y}' for x, y in rpc.items()]

print('\n')
print(' Welcome to Rock, Paper, Scissors Game '.center(50, '✅'))
print('\n')
hand1 = int(input(f'Select: {' , '.join(select_one)}\n>> Numbers: '))
hand2 = randint(1, 3)

print(rpc[hand1], 'vs', rpc[hand2])

game = {
    hand1: player1,
    hand2: player2,
    'player1' : (hand1, rpc[hand1]),
    'player2' : (hand2, rpc[hand2]),
    'hands' : {hand1, hand2},
}

if len(game['hands']) > 1:
    print(f"{player1} => {rpc[hand1]} vs {player2} => {rpc[hand2]}")
    
    for num, data_set in rules.items():
        if data_set == game['hands']:
            print(f'{'.' * 20}\n WINNER: {game[num]}\n{'.' * 20}')
            break
    
else:
    print(f'DRAW! {player1} and {player2} => {rpc[hand1]}')