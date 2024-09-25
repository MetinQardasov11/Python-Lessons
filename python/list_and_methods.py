
bag = ['apple', 'orange', 'banana', 'grape', 'kiwi']
print(bag[2])
print(bag[-1])
print(f'I\'ll buy {bag[2]}, {bag[-2]}')
print(bag[-1][-2])

# ---------------------------------------------------------------------------------------------------------------------------------------

lists = [1, 100, 5, -5, [1, 2, 3], True, None, 'hello']
print(len(lists))
print(lists[4][2])
print(lists[-4][-1])

# ---------------------------------------------------------------------------------------------------------------------------------------

companies = []
if companies:
    print('not empty')
else:
    print('empty')

print('not empty' if companies else 'empty')
print(companies[0] if companies else 'No')

# ---------------------------------------------------------------------------------------------------------------------------------------

programming_languages = ['Python', 'c#', 'java', 'c++', 'swift', 'kotlin']
if 'python'.title() in programming_languages:
    print('Ok')
else:
    print('Failed')


questions = [['2 * 2 = ', 4], ['5 > 4 =>', True]]
answer = 5
if questions[0][1] == answer:
    print('Correct')
else:
    print('Wrong')


# ---------------------------------------------------------------------------------------------------------------------------------------
word = 'hello'
word_list = list(word)
num_list = list('123456789')
print(word_list)
print(num_list)


char_list = ['h', 'e', 'l', 'l', 'o']
word = ''.join(char_list)
print(word)


names = ['Ebubekir', 'Omer', 'Osman', 'Ali']
print(', '.join(names))
print('\n'.join(names))
print('\t'.join(names))

# ---------------------------------------------------------------------------------------------------------------------------------------

# claer, count, index, reverse, sort, insert, extend, append, pop, remove, copy

names = ['Orxan', 'Samir', 'Metin', 'Xezer', 'Azer']
names[0] = 'Nihat'
names[-1] = 'Emin'
print(names)

# ---------------------------------------------------------------------------------------------------------------------------------------

names = ['Orxan', 'Samir', 'Metin', 'Xezer', 'Azer']
names[2:] = ['Not name', 1, True, None, False]
names[2:] = 'Not name', 1, True, None, False
print(names)

# ---------------------------------------------------------------------------------------------------------------------------------------

names = ['Orxan', 'Samir', 'Metin', 'Xezer', 'Azer', 'Metin']
names.clear()
print(names)

# ---------------------------------------------------------------------------------------------------------------------------------------

names = ['Orxan', 'Samir', 'Metin', 'Xezer', 'Azer', 'Metin']
print(names.count('Metin'))

# ---------------------------------------------------------------------------------------------------------------------------------------

names = ['Orxan', 'Samir', 'Metin', 'Xezer', 'Azer']
print(names.index('Xezer'))

# ---------------------------------------------------------------------------------------------------------------------------------------

names = ['Orxan', 'Samir', 'Metin', 'Xezer', 'Azer']
names.reverse()
print(names)

# ---------------------------------------------------------------------------------------------------------------------------------------

names = ['Orxan', 'Samir', 'Metin', 'Xezer', 'Azer']
names.sort()
print(names)
names.sort(reverse=True)
print(names)

# ---------------------------------------------------------------------------------------------------------------------------------------

nums = [12, 3, 9, 7, 5, 60, 32, 1, 10]
nums.sort()
print(nums)
nums.sort(reverse=True)
print(nums)

# ---------------------------------------------------------------------------------------------------------------------------------------

names = ['Orxan', 'Samir', 'Metin', 'Xezer', 'Azer']
names.append('Huseyn')
names.append('Hesen')
print(names)

# ---------------------------------------------------------------------------------------------------------------------------------------

names = ['Orxan', 'Samir', 'Metin', 'Xezer', 'Azer']
names.insert(2, 'Huseyn')
names.insert(-1, 'Hesen')
print(names)

# ---------------------------------------------------------------------------------------------------------------------------------------

names = ['Orxan', 'Samir', 'Metin', 'Xezer', 'Azer']
names.extend(['Huseyn', 'Hesen'])
print(names)

# ---------------------------------------------------------------------------------------------------------------------------------------

names = ['Orxan', 'Samir', 'Metin', 'Xezer', 'Azer']
deleted_name = names.pop(2)
print(names)
print('deleted name: ', deleted_name)

# ---------------------------------------------------------------------------------------------------------------------------------------

names = ['Orxan', 'Samir', 'Metin', 'Xezer', 'Azer']
deleted_names = []

delete1 = names.pop(1)
deleted_names.append(delete1)

delete2 = names.pop(2)
deleted_names.append(delete2)

print(names)
print('deleted names: ', deleted_names)

# ---------------------------------------------------------------------------------------------------------------------------------------

names = ['Orxan', 'Samir', 'Metin', 'Xezer', 'Azer']
names.remove('Xezer')
print(names)

# ---------------------------------------------------------------------------------------------------------------------------------------

names = ['Orxan', 'Samir', 'Metin', 'Xezer', 'Azer']
name = 'Anar'
if name in names:
    names.remove(name)
print(names)

# ---------------------------------------------------------------------------------------------------------------------------------------

names = ['Orxan', 'Samir', 'Metin', 'Xezer', 'Azer']
test = names.copy()
names.append('Kenan')
print(names)
print(test)