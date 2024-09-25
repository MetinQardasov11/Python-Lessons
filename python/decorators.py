import random

def nums(count: int) -> list[int]:
    return [x for x in range(count)]

print(nums(10))

# ---------------------------------------------------------------------------------------------------------------------------------------

def outer():
    def inner():
        print('Inner function')
        return 'Inner function called'
    
    return inner

data = outer()    
print(outer()())
print(data())

# ---------------------------------------------------------------------------------------------------------------------------------------

def outer(outer_var):
    def inner(inner_var):
        print(f'{outer_var=}',f'{inner_var=}')
        return f'{outer_var} : {inner_var}'

    return inner

data = outer('Programming language')
print(data('Python'))

# ---------------------------------------------------------------------------------------------------------------------------------------

def outer(fn):
    def inner(*args, **kwargs):
        return fn(*args, **kwargs)
    return inner


def plus(*, a: int, b: int):
    return a + b


number = outer(plus)
print(number(a=11, b=21))

# ---------------------------------------------------------------------------------------------------------------------------------------

def pw2(fn):
    def inner(*args, **kwargs):
        return fn(*args, **kwargs) ** 2
    return inner

@pw2
def plus(a: int, b: int):
    return a + b

print(plus(1, 2))

# ---------------------------------------------------------------------------------------------------------------------------------------

def twice(count):
    def inside(fn):
        def inner(*args, **kwargs):
            return str(fn(*args, **kwargs)) * count
        return inner
    return inside

@twice(10)
def plus(a: int, b: int, c: int) -> int:
    return a + b + c


print(plus(2, 3, 4))

# ---------------------------------------------------------------------------------------------------------------------------------------

def to_str(fn):
    def wrapper(*args, **kwargs):
        return [str(x) for x in fn(*args, **kwargs)]
    return wrapper

@to_str
def nums(count: int) -> list[int]:
    return [x for x in range(count)]

print(nums(10))

# ---------------------------------------------------------------------------------------------------------------------------------------

def to_file(filename):
    def inside(fn):
        def inner(*args, **kwargs):
            data = [str(x) for x in fn(*args, **kwargs)]
            with open(filename, 'w') as file:
                file.write('\t'.join(data))
            return data
        return inner
    return inside

@to_file('txt/nums.txt')
def nums(count: int) -> list[int]:
    return [random.randint(100, 1000) for x in range(count)]

print(nums(100))