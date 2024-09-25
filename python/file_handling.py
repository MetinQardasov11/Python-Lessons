
file = open('file/test.txt', 'w')
file.write('Hello World\n')
file.write('Bye\n')
file.close()


# ---------------------------------------------------------------------------------------------------------------------------------------


with open('file/test.txt', 'w') as file:
    file.write('New Test File\n')
    file.write('Change file info\n')


# ---------------------------------------------------------------------------------------------------------------------------------------


for i in range(10):
    with open(f'file/{i+1}.txt', 'w') as file:
        file.write(f'File {i+1}\n')
        

# ---------------------------------------------------------------------------------------------------------------------------------------


with open('file/hadith.txt', 'r') as file:
    print(file.read())
    print(file.read(100))
    data = file.read()
    data = file.readlines()

print(data)



# ---------------------------------------------------------------------------------------------------------------------------------------


with open('file/hadith.txt', 'r') as file:
    while True:
        line = file.readline()
        if not line:
            break
        print(line)


# ---------------------------------------------------------------------------------------------------------------------------------------


with open('file/hadith.txt', 'r+') as file:
    file.write('These hadiths is belong Imam Bukhari:')


# ---------------------------------------------------------------------------------------------------------------------------------------


with open('file/test.txt', 'a') as file:
    file.write('Add new line\n')
    file.write('Add new line\n')
    file.write('Add new line\n')


# ---------------------------------------------------------------------------------------------------------------------------------------


with open('file/example.txt', 'w') as file:
    for i in range(10):
        file.write('Hello World\n')


# və ya

ten_hello = ['hello'] * 10
with open('file/example.txt', 'w') as file:
    file.write('\n'.join(ten_hello))


# ---------------------------------------------------------------------------------------------------------------------------------------


nums = [1, 2, 3, 4, 5]
with open('file/nums.txt', 'w') as file:
    file.write('\n'.join(map(str, nums)))


# ---------------------------------------------------------------------------------------------------------------------------------------


greetings = ['hello\n', 'hi\n', 'hey\n']

with open('file/greetings.txt', 'w') as file:
    file.writelines(greetings)


# ---------------------------------------------------------------------------------------------------------------------------------------

# x modunda olanda, yeni fayl yaradir. Eger fayl path-da mocuddursa, error verir
'''
with open('file/xfile.txt', 'x') as file:
    file.write('This is new file\n')
    file.write('This is new file\n')
    file.write('This is new file\n')
'''

# ---------------------------------------------------------------------------------------------------------------------------------------


with open('img/asus.png', 'rb') as file:
    info = file.read()


with open('img/asus_copy.png', 'wb') as file:
    file.write(info)



# ---------------------------------------------------------------------------------------------------------------------------------------


with open('file/message.txt') as f1, open('file/new_message.txt', 'w') as f2:
    data = f1.read()
    f2.write(data)


