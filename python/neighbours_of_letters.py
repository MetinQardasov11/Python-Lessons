
import string

alphabet = string.ascii_lowercase
print(alphabet)

letter = input('Enter a letter: ')

if letter in alphabet:
    print(f' {letter} is in the alphabet '.center(50, '✅'))
    letter_index = alphabet.index(letter)
    if letter_index == 0:
        result = (None, alphabet[letter_index + 1])
    elif letter_index == alphabet.index(alphabet[-1]):
        result = (alphabet[letter_index - 1], None)
    else:
        result = (alphabet[letter_index - 1], alphabet[letter_index + 1])
    
    print(result)
else:
    print(f'{letter} is not in the alphabet')