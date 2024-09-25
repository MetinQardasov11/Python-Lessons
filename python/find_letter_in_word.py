
word = input('Sözü daxil edin: ')
letter = input('Hərf daxil edin: ')
result = []

if letter in word:
    for index, l in enumerate(word):
        if l == letter:
            result.append(index)
    
    print(f'\n {" Nəticə ".center(20, '✅')}')
    print(f'Sözdə hərfin yeri: {', '.join(map(str, result))}')
    print(f'Sözdə {letter} hərfinin sayı : {len(result)}')
else:
    print(f'\n {" Nəticə ".center(20, '❌')}')
    print(f'Sözdə {letter} hərfi yoxdur')