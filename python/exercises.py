
# 1) Daxil edilen n rəqəmli ədədlərin cəmin tapmaq
number = int(input('Enter a number: '))

total = 0

while number > 0:
    digit = number % 10
    total += digit
    number //= 10
print(total)

# ---------------------------------------------------------------------------------------------------------------------------------------

# 2) Daxil edilen ədədin tək və ya cüt olduğunu yoxlamaq
number = int(input('Enter a number: '))

if number > 0:
    if number % 2 == 0:
        print(f'{number} is even')
    else:
        print(f'{number} is odd')
else:
    print(f'{number} is not a number')

# və ya

print(f'{number} is even' if number % 2 == 0 else f'{number} is odd')

# ---------------------------------------------------------------------------------------------------------------------------------------

# 3) 1-dən 50-ə qədər olan ədədlərdən 5-ə bölünənləri çap etmək
i = 1
counter = 0
while i <= 50:
    if i % 5 == 0:
        counter += 1
    i += 1
print(counter)
    
# və ya

counter = 0
for i in range(1, 51):
    if i % 5 == 0:
        counter += 1
print(counter)

# ---------------------------------------------------------------------------------------------------------------------------------------

# 4) [4,5,6,7,8,9] olan listdə indeksi 4 dəyərində olan ədədi çap etmək
my_list = [4,5,6,7,8,9]

for i in range(len(my_list)):
    if i == 4:
        print(my_list[i])
        
# ---------------------------------------------------------------------------------------------------------------------------------------

# 5) x = 25 olduqda x ədədinin onluq və təklik rəqəmlərinin cəmini tapmaq
x = 25
total_digit = 0
print(divmod(x, 10)[0] + divmod(x, 10)[1])
while x > 0:
    digit = x % 10
    total_digit += digit
    x //= 10

print(total_digit)

# ---------------------------------------------------------------------------------------------------------------------------------------

# 6) Klaviaturadan daxil edilən x = 658 ədədin 865 kimi çevirmək
x = 658
first_num = x // 100
second_num = x // 10 % 10
third_num = x % 10
new_num = third_num * 100 + second_num * 10 + first_num
print(new_num)

# və ya

x = str(658)
print(int(x[::-1]))

# ---------------------------------------------------------------------------------------------------------------------------------------

# 7) x = 256 ədədinin rəqəmlərinin cəmini və hasilini tapmaq
x = 256
sum_digit = 0
multiply_digit = 1
while x > 0:
    digit = x % 10
    sum_digit += digit
    multiply_digit *= digit
    x //= 10

print(f'Sum of digit of 256: {sum_digit}')
print(f'Multiply of digit of 256: {multiply_digit}')

# və ya

x = '256'
a, b, c = map(int, x)
print(a + b + c)
print(a * b * c)

# ---------------------------------------------------------------------------------------------------------------------------------------

# 8) Ilk 30 ədədin cəmini tapmaq
sum_num = 0
for i in range(1, 31):
    sum_num += i

print(sum_num)

# və ya

print(sum(range(1, 31)))

# və ya

print(sum(i for i in range(1, 31)))

# və ya
i = 1
sum_num = 0
while i <= 30:
    sum_num += i
    i += 1
    
print(sum_num)

# ---------------------------------------------------------------------------------------------------------------------------------------

# 9) Klaviaturadan daxil simvolların ədədin ən böyüyünü tapmaq
symbol = input('Enter a number: ')
max_num = int(symbol[0])

for i in symbol:
    if int(i) > max_num:
        max_num = int(i)
print(max_num)

# və ya
num = input('Enter a number: ')
list_num = list(num)
print(max(list_num))

# və ya
print(max(list(input('Enter a number: '))))

# ---------------------------------------------------------------------------------------------------------------------------------------

# 10) üçbucağın verilmiş tərəflərinə görə perimiterini tapmaq
first_side = int(input('Enter first side: '))
second_side = int(input('Enter second side: '))
third_side = int(input('Enter third side: '))

if first_side == second_side == third_side:
    perimeter = 3 * first_side
    print('Equilateral triangle. Perimeter = {}'.format(perimeter))
else:
    perimeter = first_side + second_side + third_side
    print('Perimeter = {}'.format(perimeter))
    
# və ya

def perimeter_triangle(side1, side2, side3):
    if side1 == side2 == side3:
        perimeter = 3 * side1
        print('Equilateral triangle. Perimeter = {}'.format(perimeter))
    else:
        perimeter = side1 + side2 + side3
        print('Perimeter = {}'.format(perimeter))

perimeter_triangle(first_side, second_side, third_side)

# və ya

def perimeter_tri(*side):
    return sum(side)

print(perimeter_tri(first_side, second_side, third_side))

# ---------------------------------------------------------------------------------------------------------------------------------------

# 11) 100-ə qədər olan fibonacci ədədlərini tapmaq
a, b = 0, 1  # ilk 2 fibonacci ədədi 0 və 1-dir. Sonrakılar isə belə olacaq: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89
print(a)
while b < 100:
    print(b)
    a, b = b, a + b
    
# və ya

def fibonacci(max_num):
    data = [0, 1]
    while True:
        next_num = data[-1] + data[-2]
        if next_num > max_num:
            break
        data.append(next_num)
    return data 
  
print(fibonacci(100))
print(f'Sum of first 100 fibonacci numbers: {sum(fibonacci(100))}')