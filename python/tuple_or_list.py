
print(divmod(10,2))

def dmode(a,b):
    return a // b, a % b

print(dmode(10, 3))

# ---------------------------------------------------------------------------------------------------------------------------------------

text = 'Python'
print(list(enumerate(text)))
print(*enumerate(text))
print(*enumerate(text, 5))


def my_enumerate(data, start=0):
    result = []
    for x in data:
        result.append((start, x))
        start += 1
    return result

print(my_enumerate('Python'))
print(my_enumerate('Python', 10))

# ---------------------------------------------------------------------------------------------------------------------------------------

import names
import random

def random_names(count=10):
    return [names.get_full_name() for x in range(count)]

print(random_names())
print(random_names(4))
print(random_names(random.randint(1, 5)))

# ---------------------------------------------------------------------------------------------------------------------------------------

import random
def dominoes():
    data = []
    for x in range(28):
        for y in range(x, 7):
            data.append((x, y))
    
    return data

print(dominoes())
print(len(dominoes()))

all_domino = dominoes()
random.shuffle(all_domino)

player_1 = [all_domino.pop() for x in range(7)]
player_2 = [all_domino.pop() for x in range(7)]
player_3 = [all_domino.pop() for x in range(7)]
print(player_1)
print(player_2)
print(player_3)
print(all_domino)
print(len(all_domino))