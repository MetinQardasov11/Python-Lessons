
# Dictionary mutable, ordered və iterable data tipidir.

# Dicitionary-də açarlar təkrarlana bilməz, unikaldır.
data_1 = {
    'name' : 'Metin',
    'age' : 30,
    'name' : 'Ali',
    1: 'one',
    (1,2): 'one and two'
}
print(data_1['name'])
print(data_1['age'])
print(data_1[1])
print(data_1[(1, 2)])
print(data_1[1, 2])

# ---------------------------------------------------------------------------------------------------------------------------------------

data_2 = {
    'nums' : [1, 2, 3, 4],
    None : 'no',
    True : 'yes',
    False : 'no',
    'tuple' : (5, 6, 7)
}
print(data_2)
print(data_2['nums'][1])
print(data_2[None][-1])
print(data_2['tuple'][1])

# ---------------------------------------------------------------------------------------------------------------------------------------

data_3 = {
    'name' : 'Metin',
    'surname' : 'Qardasov',
    'age' : 30,
}

data_3['age'] = 20
data_3['hobbies'] = ['coding', 'reading a book', 'swimming']
print(data_3)

# ---------------------------------------------------------------------------------------------------------------------------------------

data_4 = {
    'name' : 'Metin',
    'surname' : 'Qardasov',
    'age' : 30,
}

for key in data_4:
    print(key, ':', data_4[key])

# ---------------------------------------------------------------------------------------------------------------------------------------

students = {
    'Metin' : 90,
    'Ali' : 80,
    'Veli' : 70,
    'Süleyman' : 60
}

name = 'Kenan'

if name in students:
    print(students[name])
else:
    print('Student not found')
    
# ---------------------------------------------------------------------------------------------------------------------------------------

data_students = [
    {'name' : 'Metin', 'age' : 30},
    {'name' : 'Ali', 'age' : 25},
    {'name' : 'Veli', 'age' : 20},
    {'name' : 'Süleyman', 'age' : 35}
]

print(data_students)

for data in data_students:
    print(f'{data["name"]} : {data["age"]}')

# ---------------------------------------------------------------------------------------------------------------------------------------

data = {}
data['one'] = 1
data['two'] = 2
print(data)

# ---------------------------------------------------------------------------------------------------------------------------------------

data = {}
for x in range(1, 11):
    data[x] = x * 2

print(data)

# ---------------------------------------------------------------------------------------------------------------------------------------

data = {}
for x in 'salam':
    data[x] = x.upper() * 2

print(data)

# ---------------------------------------------------------------------------------------------------------------------------------------

# clear metodu
data = {'a' : 'A',1: 'one',None: 'none',True: 'ok',(1, 2) : [1, 2]}
data.clear()
print(data)

# ---------------------------------------------------------------------------------------------------------------------------------------

# copy metodu
students = {
    'Metin' : 90,
    'Ali' : 80,
    'Veli' : 70,
    'Süleyman' : 60
}

copy_students = students.copy()
students['Osman'] = 50
print(students)
print(copy_students)

# ---------------------------------------------------------------------------------------------------------------------------------------

# fromkeys metodu
word = 'python'
data = dict.fromkeys(word, 'char')
print(data)

nums = [1, 2, 3, 4, 5]
data = dict.fromkeys(nums, 'nums')
print(data)

tuple_ = 1, 2, 3, 4, 5
data = dict.fromkeys(tuple_, 'tuple')
print(data)

words = {'a' : 'A', 'b' : 'B'}
data = dict.fromkeys(words, 'words')
print(data)

# ---------------------------------------------------------------------------------------------------------------------------------------

# keys metodu
students = {'Metin' : 90,'Ali' : 80,'Veli' : 70,'Süleyman' : 60}
keys = students.keys()

for x in keys:
    print(x)
    
new_dict = dict.fromkeys(keys, 'new')
print(new_dict)

all_keys = list(students.keys())
print(all_keys.index('Veli'))

# ---------------------------------------------------------------------------------------------------------------------------------------

# values metodu
students = {'Metin' : 90,'Ali' : 80,'Veli' : 70,'Süleyman' : 60}
all_values = students.values()
print(all_values)

# ---------------------------------------------------------------------------------------------------------------------------------------

# items metodu
students = {'Metin' : 90,'Ali' : 80,'Veli' : 70,'Süleyman' : 60}
all_items = students.items()
print(all_items)

for name, point in students.items():
    print(f'{name} - {point}')

# ---------------------------------------------------------------------------------------------------------------------------------------

# get metodu
students = {'Metin' : 90,'Ali' : 80,'Veli' : 70,'Süleyman' : 60}
print(students.get('Metin'))
print(students.get('Osman', False))

# ---------------------------------------------------------------------------------------------------------------------------------------

# setdefault metodu
# setdefault ilə get metodu eynidir demək olarki. Amma əsas fərqi ondadır ki, setdefault metodu dictionary-də olmayan dəyəri çıxarmır amma həmin dəyəri yaradır.

students = {'Metin' : 90,'Ali' : 80,'Veli' : 70,'Süleyman' : 60}
print(students.setdefault('Metin'))
print(students.setdefault('Osman', 'not found'))
print(students)

# ---------------------------------------------------------------------------------------------------------------------------------------

# update metodu
students = {'Metin' : 90,'Ali' : 80,'Veli' : 70,'Süleyman' : 60}
new_students = {'Osman' : 50, 'Sultan' : 40, 'Orxan': 100}
students.update(new_students)
students.update([('Omer' , 90), ('Talha', 80)])
print(students)

# ---------------------------------------------------------------------------------------------------------------------------------------

# pop metodu
students = {'Metin' : 90,'Ali' : 80,'Veli' : 70,'Süleyman' : 60}
deleted_value = students.pop('Metin')
print(students)
print(deleted_value)

# ---------------------------------------------------------------------------------------------------------------------------------------

# popitem metodu
students = {'Metin' : 90,'Ali' : 80,'Veli' : 70,'Süleyman' : 60}
deleted_item = students.popitem()
print(students)
print(deleted_item)

students = {'Metin' : 90,'Ali' : 80,'Veli' : 70,'Süleyman' : 60}
deleted_item = []

for x in range(3):
    item = students.popitem()
    deleted_item.append(item)

print(students)
print(deleted_item)