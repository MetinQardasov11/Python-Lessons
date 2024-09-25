
# ƏBOB(ən böyük ortaq bölən)
# natural ədədlərin hər ikisinin bölündüyü ən böyük natural ədəd
# Məsələn
a = 75
b = 45
# Burda ƏBOB 15 olacaq. Çünki hər ikisinə bölünən max ədəd 15-dir.

# ---------------------------------------------------------------------------------------------------------------------------------------

# və ya
a = 75
b = 25
# Burda ƏBOB 25-in özü olacaq. Çünki hər ikisinə bölünən max ədəd 25-dir.

# Burda for dövründən istifadə edirik
# Burda ona görə min(a, b) yazırıq ki, ən böyük ortaq bölən ədəd maksimum iki ədəddən ən kiçiyi ola bilər. Yəni 75 və 25 olan yerdə əbob 25-dən böyük ola bilməz.

a = int(input('Enter a number: '))
b = int(input('Enter b number: '))

for x in range(1, min(a, b) + 1):
    if a % x == 0 and b % x == 0:
        max_num = x

print(max_num)

# ---------------------------------------------------------------------------------------------------------------------------------------

# və ya

def greatest_denominator(a, b):
    for x  in range(1, min(a, b) + 1):
        if a % x == 0 and b % x == 0:
            max_num = x
    
    return max_num

print(greatest_denominator(a, b))

# ---------------------------------------------------------------------------------------------------------------------------------------

# ƏKOB(ən kiçik ortaq bölünən)
# natural ədədlərin hər ikisə bölünən ən kicik natural ədəd
# Məsələn
a = 16
b = 24
# Burda ƏKOB 48 olacaq. Həm 16-a, həm də 24-ə bölünən min ədəd 48-dir.

# ---------------------------------------------------------------------------------------------------------------------------------------

# və ya
a = 7
b = 11
# Burda ƏKOB 77 olacaq. Həm 7-a, həm də 11-ə bölünən min ədəd 77-dir.

# Burda da for dövründən istifadə edəcəyik. 
# Burda ona görə max(a, b) yazırıq ki, min ƏKOB iki ədəddən ən böyüyü ola bilər. Ən böyük ƏKOB-da onların hasili ola bilər. 7 və 11 misalı kimi. 7 və 11 ikisi də sadə ədədlər olduğu üçün, onların ƏKOB-u onların hasilinə bərabərdir.

a = int(input('Enter a number: '))
b = int(input('Enter b number: '))
for x in range(max(a, b), a * b + 1):
    if x % a == 0 and x % b == 0:
        min_num = x
        break

print(min_num)

# və ya

# ---------------------------------------------------------------------------------------------------------------------------------------

def least_common_multiple(a, b):
    for x in range(max(a, b), a * b + 1):
        if x % a == 0 and x % b == 0:
            return x

print(least_common_multiple(a, b))

# Əgər ƏBOB məlumdursa, ƏKOB-u tapmağın yolu:
# ƏKOB = (a * b) / ƏBOB
def greatest_denominator(a, b):
    for x  in range(1, min(a, b) + 1):
        if a % x == 0 and b % x == 0:
            max_num = x
    
    return max_num

num1 = int(input('Enter number 1: '))
num2 = int(input('Enter number 2: '))

lower_divisor = (num1 * num2) // greatest_denominator(num1, num2)
print(lower_divisor)