import random
import names
from functools import reduce

say_hello = lambda: 'hello'
print(say_hello())

# ---------------------------------------------------------------------------------------------------------------------------------------

plus = lambda a, b: a + b
print(plus(10, 20))

# ---------------------------------------------------------------------------------------------------------------------------------------

plus = lambda a, b=20: a + b
print(plus(10))

# ---------------------------------------------------------------------------------------------------------------------------------------

minus = lambda *, a, b: a - b
print(minus(a=10, b=20))
print(minus(a=20, b=10))

# ---------------------------------------------------------------------------------------------------------------------------------------

nums = lambda count, *, start, end: [random.randint(start, end) for _ in range(count)]
print(nums(10, start=1000, end=9999))

# ---------------------------------------------------------------------------------------------------------------------------------------

rand_names = lambda count, gender: [names.get_full_name(gender=gender) for _ in range(count)]
print(rand_names(5, 'male'))

# ---------------------------------------------------------------------------------------------------------------------------------------

check_even = lambda num: num % 2 == 0
print(check_even(10))
print(check_even(33))

# ---------------------------------------------------------------------------------------------------------------------------------------

check_negative = lambda num: num < 0
print(check_negative(-10))
print(check_negative(55))

# ---------------------------------------------------------------------------------------------------------------------------------------

show = lambda: print('Python')
# show()

# ---------------------------------------------------------------------------------------------------------------------------------------

greeting = lambda name: f'Hello, {name}'
print(greeting('John'))

# və ya

print((lambda name: f'Hello, {name}')('Metin'))

# ---------------------------------------------------------------------------------------------------------------------------------------

# ! Lambda functions in => map, filter, reduce, sort ...

# ---------------------------------------------------------------------------------------------------------------------------------------

# ? map

nums = [1, 2, 3, 4, 5, 6]
data = map(lambda num: str(num ** 2 if num % 2 == 0 else num), nums)
print(list(data))

# ---------------------------------------------------------------------------------------------------------------------------------------

nums = [1, 2, 3, 4, 5, 6]
data = map(lambda num: num + 10, nums)
print(list(data))

# ---------------------------------------------------------------------------------------------------------------------------------------

# ? filter

nums = [1, -2, -3, 4, 5, -6]
negative_nums = filter(lambda num: num < 0, nums)
even_and_positive_nums = filter(lambda num: num > 0 and num % 2 == 0, nums)
print(list(negative_nums))
print(list(even_and_positive_nums))

# ---------------------------------------------------------------------------------------------------------------------------------------

nums = [5, 6.7, 7.7, 13, 4, 1.3, 'python', True, False, '4.2']
int_nums = filter(lambda num: type(num) == int, nums)
float_nums = filter(lambda num: type(num) == float, nums)
str_nums = filter(lambda num: type(num) == str, nums)
bool_nums = filter(lambda num: type(num) == bool, nums)
print(list(int_nums))
print(list(float_nums))
print(list(str_nums))
print(list(bool_nums))

# ---------------------------------------------------------------------------------------------------------------------------------------

words = ['kök', 'python', 'ata', 'ana', 'qab', 'ənənə']
same_opposite = filter(lambda word: word == word[::-1], words)
print(list(same_opposite))

# ---------------------------------------------------------------------------------------------------------------------------------------

# ? sort

words = ['mişar', 'duz', 'ağac', 'it', 'Python']
# words.sort()
words.sort(key=lambda x: len(x))
print(words)

# ---------------------------------------------------------------------------------------------------------------------------------------

# ? sorted

words = ['mişar', 'duz', 'ağac', 'it', 'Python']
len_sorting = sorted(words, key=lambda x: len(x))
letter_sorting = sorted(words)
print(len_sorting)
print(letter_sorting)

# ---------------------------------------------------------------------------------------------------------------------------------------

# ? reduce
nums = [1, 2, 3, 4, 5]
sum_nums = reduce(lambda x, y: x + y, nums)
multiple_nums = reduce(lambda x, y: x * y, nums)
print(sum_nums)
print(multiple_nums)