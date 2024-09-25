
from itertools import count
import random

count_num = count(start = 0, step=5)
print(next(count_num))
print(next(count_num))
print(next(count_num))
print(next(count_num))

# ---------------------------------------------------------------------------------------------------------------------------------------

count_num = count(start = 0, step=5)
for x in count_num:
    print(x)
    if x > 90:
        break

# ---------------------------------------------------------------------------------------------------------------------------------------
    
count_num = count(start = 15, step=-1)
for x in count_num:
    print(x)
    if x <= 2:
        break

# ---------------------------------------------------------------------------------------------------------------------------------------

names = ['John', 'Corey', 'Adam', 'Steve', 'Rick', 'Thomas']
points = [random.randint(10, 30) for i in range(len(names))]
counter = count(1)

for n, p, c in zip(names, points, counter):
    print(f"{c}. {n} - {p} points")