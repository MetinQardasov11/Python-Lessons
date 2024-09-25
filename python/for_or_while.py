
text = 'I love Python'
for x in text:
    print(x)

# və ya

i = 0
while i < len(text):
    print(text[i])
    i += 1

# ---------------------------------------------------------------------------------------------------------------------------------------

data_list = [11, True, None, 'Hello', 12.3]
for x in data_list:
    print(x)


for i, x in enumerate(data_list):
    print(i, x)
    

# və ya

i = 0
while i < len(data_list):
    print(data_list[i])
    i += 1

# ---------------------------------------------------------------------------------------------------------------------------------------

data_tuple = 11, 'Hello', 'salam', 77
for x in data_tuple:
    print(x)

# ---------------------------------------------------------------------------------------------------------------------------------------

data_set = {33, True, 'salam', None, 99}
for x in data_set:
    print(x)

# ---------------------------------------------------------------------------------------------------------------------------------------

data_dict = {'name' : 'Metin', 'age' : 20, 'city' : 'Baku'}
for x in data_dict:
    print(x)


for key, value in data_dict.items():
    print(key, value)
    
keys = data_dict.keys()

for x in keys:
    print(x)

# ---------------------------------------------------------------------------------------------------------------------------------------

nums = []
for x in range(1000):
    data = int(input('Enter a number: '))
    if data % 2 == 0:
        nums.append(data)
    
    if len(nums) == 10:
        break
    
print(nums)


# və ya

nums = []
while True:
    data = int(input('Enter a number: '))
    if data % 2 == 0:
        nums.append(data)

    if len(nums) == 10:
        break

print(nums)

# və ya

nums = []
while len(nums) != 10:
    data = int(input('Enter a number: '))
    if data % 2 == 0:
        nums.append(data)

    if len(nums) == 10:
        break

print(nums)