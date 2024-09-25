
def say_hi():
    print('hi')

say_hi()

# ---------------------------------------------------------------------------------------------------------------------------------------

def plus():
    a = 5
    b = 10
    print(a + b)

plus()

# ---------------------------------------------------------------------------------------------------------------------------------------

def show_five():
    print('five show')
    return 5


def give_five():
    return 5

show_five()
print(give_five())

number = give_five()
number += 10
print(number)

print(show_five())

# ---------------------------------------------------------------------------------------------------------------------------------------

def test_me():
    num = 6
    if num > 5:
        return 'ok'
    else:
        return 'not ok'

print(test_me())

# ---------------------------------------------------------------------------------------------------------------------------------------

def show_even_1_and_100():
    even_list = []
    for i in range(1, 101):
        if i % 2 == 0:
            even_list.append(i)
    
    return even_list

print(show_even_1_and_100())

for a in show_even_1_and_100():
    print(a)
    
# ---------------------------------------------------------------------------------------------------------------------------------------

import random
def roll_dice():
    return random.randint(1, 6), random.randint(1, 6)

for x in range(10):
    print(roll_dice())

# ---------------------------------------------------------------------------------------------------------------------------------------

def echo(word):
    return word

print(echo('salam'))
print(echo('hi'))
print(echo('hello'))

# ---------------------------------------------------------------------------------------------------------------------------------------

def say_hello(word, count):
    data = []
    for x in range(count):
        data.append(word)
    
    return '\n'.join(data)

print(say_hello('salam', 4))
print(say_hello('hi', 3))
print(say_hello('hello', 10))

# və ya

def say_hello(word, count):
    return '\n'.join([word for x in range(count)])

print(say_hello('salam', 4))
print(say_hello('hi', 3))
print(say_hello('hello', 10))

# ---------------------------------------------------------------------------------------------------------------------------------------

def plus(num1=0, num2=3):
    return num1 + num2

print(plus(12, 4))