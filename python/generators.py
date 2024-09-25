
# ! Generators

import string, names
from faker import Faker


def numbers():
    yield 1
    yield 2
    yield 3
    yield 4
    
gen = numbers()
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))

# və ya

for x in numbers():
    print(x)

# ---------------------------------------------------------------------------------------------------------------------------------------

def numbers():
    for i in range(1, 101):
        yield i
    
gen_nums = numbers()

for i in gen_nums:
    print(i, end=' ')

# ---------------------------------------------------------------------------------------------------------------------------------------

def alphabet():
    letters = string.ascii_lowercase
    for x in letters:
        yield x

letter1 = alphabet()
letter2 = alphabet()

for x in letter1:
    print(x, end=' ')

# print()

for x in letter2:
    print(x, end=' ')

# ---------------------------------------------------------------------------------------------------------------------------------------

def infinite_numbers(n = 1):
    while True:
        yield n
        n += 1

gen = infinite_numbers()
# for i in gen:
#     print(i)
    
word = 'python'

for num, letter in zip(gen, word):
    print(f'num: {num} => letter: {letter}')

# ---------------------------------------------------------------------------------------------------------------------------------------

def get_name(letter):
    fake = Faker('az_AZ')
    while True:
        name = fake.first_name()
        if name.startswith(letter):
            yield name

az_names = get_name('M')
# for name in az_names:
#     print(name)


# və ys

for i,x in enumerate(az_names, 1):
    print(x)
    if i == 100:
        break
    
    
data = [next(az_names) for _ in range(10)]
print(data)

# ---------------------------------------------------------------------------------------------------------------------------------------

# n qədər fibonacci ədədi çap etmək
def fib(count=10):
    a, b = 0, 1
    
    for _ in range(count):
        yield a
        a, b = b, a + b

for x in fib(20):
    print(x)

print('Cem :',sum(fib(20)))

# ---------------------------------------------------------------------------------------------------------------------------------------

# Qeyd etdiyimiz edede qeder olan fibonacci ədədləri çap etmək
def fib(num):
    a, b= 0, 1
    while a < num:
        yield a
        a, b = b, a + b

for x in fib(500):
    print(x)

print('Cem :',sum(fib(500)))

# ---------------------------------------------------------------------------------------------------------------------------------------

# ! Generate Expression

nums = (x for x in range(1, 11))

for x in nums:
    print(x, end=' ')

# və ya

print(*nums)
    
# ---------------------------------------------------------------------------------------------------------------------------------------

square_nums = (x ** 2 for x in range(1, 100))

for num in square_nums:
    print(num, end=' ')

# və ya

print(*square_nums)

# ---------------------------------------------------------------------------------------------------------------------------------------

names_generator = (names.get_first_name() for _ in range(10))

for name in names_generator:
    print(name)