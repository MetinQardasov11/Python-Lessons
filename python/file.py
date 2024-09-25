
folder = 'txt'
file = 'file.txt'

with open(f'{folder}/{file}', 'w') as f:
    f.write('Hello, world!\n')


for x in range(1, 6):
    with open(f'{folder}/file{x}.txt', 'a') as f:
        f.write(f'File : {x}\n')