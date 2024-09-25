for x in range(10):
    print(x)

# ---------------------------------------------------------------------------------------------------------------------------------------
    
for x  in range(1, 11, 3):
    print(x)
   
# ---------------------------------------------------------------------------------------------------------------------------------------
    
new_word = ''
for x in 'python':
    if x == 'o':
        x = '*'
    new_word += x
    
print(new_word)

# ---------------------------------------------------------------------------------------------------------------------------------------

names = ['Ebubekir', 'Omer', 'Osman', 'Ali']
for name in names:
    if name.startswith('O'):
        print(name)

# ---------------------------------------------------------------------------------------------------------------------------------------

for x in range(10):
    if x == 5:
        break
    
    print(x)    
    
# ---------------------------------------------------------------------------------------------------------------------------------------    

names = ['Ebubekir', 'Omer', 'Osman', 'Ali']
for name in names:
    print(name)
    if name == 'Omer':
        break

# ---------------------------------------------------------------------------------------------------------------------------------------

even_numbers = []
for x in range(1, 101):
    if x % 2 == 0:
        even_numbers.append(x)

print(even_numbers)

# ---------------------------------------------------------------------------------------------------------------------------------------

even_numbers = []
for x in range(0, 100, 2):
    if x % 2 == 0:
        even_numbers.append(x)
        
print(even_numbers)

# ---------------------------------------------------------------------------------------------------------------------------------------

even_numbers = []
for x in range(100):
    if x == 41:
        break
    if x % 2 == 0:
        even_numbers.append(x)

print(even_numbers)

# ---------------------------------------------------------------------------------------------------------------------------------------

odd_numbers = []
for x in range(100):
    if x % 2 == 0:
        continue
    odd_numbers.append(x)

print(odd_numbers)

# ---------------------------------------------------------------------------------------------------------------------------------------

names = ['Ebubekir', 'Omer', 'Osman', 'Ali']
new_names = []
for name in names:
    if name.startswith('O'):
        continue
    new_names.append(name)

print(new_names)

# ---------------------------------------------------------------------------------------------------------------------------------------

names = ['Ebubekir', 'Omer', 'Osman', 'Ali', 'Talha', 'Zubeyr', 'Abdurrahman bin Avf', 'Sad bin Ebu Vakkas', 'Said bin Zeyd', 'Ebu Ubeyde']
letter = 'A'
for name in names:
    if name.startswith(letter):
        print(name)
        break
else:
    print('No name found')   

# ---------------------------------------------------------------------------------------------------------------------------------------

names = ['Ebubekir', 'Omer', 'Osman', 'Ali']
letter_list = []
for name in names:
    temp_list = []
    for letter in name:
        temp_list.append(letter)
    
    letter_list.append(temp_list)

print(letter_list)


# və ya

# ---------------------------------------------------------------------------------------------------------------------------------------

letter_list = []
for name in names:
    letter_list.append(list(name))

print(letter_list)