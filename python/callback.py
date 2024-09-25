from typing import Callable

def plus(a, b):
    return a + b

add = plus
print(add(1, 2))

# ---------------------------------------------------------------------------------------------------------------------------------------

total = sum
print(total([11, 22, 33, 44, 55]))

# ---------------------------------------------------------------------------------------------------------------------------------------

show = print
# show('Python Programmgin language 🐍🐍🐍')

# ---------------------------------------------------------------------------------------------------------------------------------------

nums: list[int] = [1, 2, 3, 4, 5]
# nums: list[str] = map(str, nums)
print(list(nums))

# ---------------------------------------------------------------------------------------------------------------------------------------

def plus_num(a: int, b: int) -> int:
    return a + b

def minus(a: int, b: int) -> int:
    return a - b

def multiply(a: int, b: int) -> int:
    return a * b


def calc(func: Callable[[int, int], int], a, b) -> int:
    return func(a, b)
    
print(calc(plus_num, 4, 3))
print(calc(minus, 14, 9))
print(calc(multiply, 9, 7))

fns = [plus_num, minus, multiply]

for x in fns:
    print(x(30, 3))
    # və ya
    print(calc(x, 30, 3))

# ---------------------------------------------------------------------------------------------------------------------------------------

sqr_sum = lambda a, b: a**2 + b**2
print(calc(sqr_sum,3, 4))
print(calc(lambda a, b: a**2 + b**2, 3, 4))

# ---------------------------------------------------------------------------------------------------------------------------------------

nums: list[int] = [1, 2, 3, 4, 5]
print(list(map(lambda x: x**2, nums)))

# ---------------------------------------------------------------------------------------------------------------------------------------

def pow5(number: int) -> int:
    return number**5

nums = list(map(pow5, nums))
print(nums)

# ---------------------------------------------------------------------------------------------------------------------------------------

nums: list[int] = [1, 2, 3, 4, 5]
def my_map(fn: Callable, data: list) -> list:
    result = []
    for x in data:
        result.append(fn(x))
    
    return result

print(list(my_map(pow5, nums)))
print(list(my_map(str, nums)))

# ---------------------------------------------------------------------------------------------------------------------------------------

def metin(work: str) -> str:
    return f'Metin: {work} is completed'

def omer(work: str) -> str:
    return f'Omer: {work} is completed'

def osman(work: str) -> str:
    return f'Osman: {work} is completed'

workers: dict[str, Callable] = {
    'Computer' : metin,
    'Network' : omer,
    'Database' : osman
}

def repair(problem: str) -> str | bool:
    expert = workers.get(problem)
    if expert is None:
        return 'No expert found'

    return expert(problem)

print(repair('Network'))
print(repair('Database'))
print(repair('Computer'))