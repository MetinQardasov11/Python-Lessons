
# [true] if [statement] else [false]

# 1.
num = int(input('Enter the num: '))
result = ''

result= 'Even' if num % 2 == 0 else 'Odd'
print(result)

# ---------------------------------------------------------------------------------------------------------------------------------------

# 2.
print('more' if not 5 > 4 else 'less')

# ---------------------------------------------------------------------------------------------------------------------------------------

# 3. 
text = 'equal' if 10 == 10 else 'not equal'
print(text)

# ---------------------------------------------------------------------------------------------------------------------------------------

# 4.
num = int(input('Enter the num: '))
result = 'positive' if num > 0 else 'negative' if num < 0 else 'zero'
print(result)

# ---------------------------------------------------------------------------------------------------------------------------------------

# 5.
word = 'python'
result = 'yes' if 'p' in word else 'no'
print(result)

# ---------------------------------------------------------------------------------------------------------------------------------------


# 6.
word = 'python'
result = 'yes' if word[-1] == 'n' else 'no'
print(result)

# ---------------------------------------------------------------------------------------------------------------------------------------

# 7.
age = 10
parent = True
ok_message = 'Access granted'
no_message = 'Access denied'

if age < 18:
    print(ok_message if parent else no_message)
else:
    print(no_message)
    