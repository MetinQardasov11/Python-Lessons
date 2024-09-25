
def recursive_hello():
    print("Hello")
    recursive_hello()

# recursive_hello()

# ---------------------------------------------------------------------------------------------------------------------------------------

# 100-dən 0-a qədər azalan sıra ilə düzüləcək
def numbers(x):
    if x == 0:
        return
    print(x)
    numbers(x - 1)

# numbers(100)

# ---------------------------------------------------------------------------------------------------------------------------------------

# 0-dan 100-ə qədər artan sıra ilə düzüləcək
def numbers(x):
    if x == 0:
        return
    numbers(x - 1)
    print(x)

numbers(100)

# ---------------------------------------------------------------------------------------------------------------------------------------

def numbers(x):
    if x == 0:
        return 'done'
    print(x)
    return numbers(x - 1)

print(numbers(100))

# ---------------------------------------------------------------------------------------------------------------------------------------

def factorial(x):
    if x == 1:
        return 1
    return x * factorial(x - 1)

print(factorial(10))

# ---------------------------------------------------------------------------------------------------------------------------------------

fib_nums = {}

def fib(x):
    if x in fib_nums:
        return fib_nums.get(x)
    
    if x == 1:
        return 1
    elif x == 2:
        return 1
    else:
        data = fib(x - 1) + fib(x - 2)
        
    fib_nums[x] = data
    return data

print(fib(20))

for x in range(1, 200):
    print(f'Fibonacci [{x}] => {fib(x)}')

# ---------------------------------------------------------------------------------------------------------------------------------------

def power(a, b):
    if a == 0:
        return 0
    elif b == 0:
        return 1
    elif b == 1:
        return a
    else:
        return a * power(a, b - 1)

print(power(2, 20))
print(power(9, 10))