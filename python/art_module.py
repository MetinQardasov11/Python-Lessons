from art import art, tprint, text2art, randart, tsave

text = text2art('Metin Qardasov')
print(text)

tprint('Metin Qardasov')
tsave('Metin Qardasov', filename='txt/name.txt')

arts = [art('random') for x in range(10)]
print('\n'.join(arts))