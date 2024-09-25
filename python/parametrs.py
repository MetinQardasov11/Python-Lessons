def greeting():
    return 'Salam, Mətin Qardaşov'

print(greeting())

# ---------------------------------------------------------------------------------------------------------------------------------------

def greeting(name):
    return f'Salam, {name}'

print(greeting('Mətin Qardaşov'))

# ---------------------------------------------------------------------------------------------------------------------------------------

def greeting(name='Mətin Qardaşov'):
    return f'Salam, {name}'

print(greeting())

# ---------------------------------------------------------------------------------------------------------------------------------------

def greeting(name, surname):
    return f'Salam, {name} {surname}'

print(greeting('Mətin', 'Qardaşov'))
print(greeting(surname='Qardaşov', name='Mətin'))

# ---------------------------------------------------------------------------------------------------------------------------------------

def greeting(company, name, surname):
    return f'Salam, {name} {surname}, "{company}" şirkəti sizi salamlayır.'

print(greeting('Apple', 'Mətin', 'Qardaşov'))

# ---------------------------------------------------------------------------------------------------------------------------------------

# Əgər dəyişən yerinə / yazırıqsa, biz onu çağıran zaman 'company=' yaza bilmərik. 41-ci sətirdə olduğu kimi yaza bilmərik.
def greeting(company, name, surname, /):
    return f'Salam, {name} {surname}, "{company}" şirkəti sizi salamlayır.'

# print(greeting('Mətin', 'Qardaşov',company='Apple'))

# ---------------------------------------------------------------------------------------------------------------------------------------

# Burda isə kod işləyəcək. Çünki biz '/' işarəsini hara qoyuruqsa, ondan əvvəl olan elementləri parametrləri ilə çağıra bilmərik. 
# Əgər '/' işarəsini name-dən sonraya qoysaq, o zaman 'surname='-də yaza bilərik.
def greeting(name, surname, /, company):
    return f'Salam, {name} {surname}, "{company}" şirkəti sizi salamlayır.'

print(greeting('Mətin', 'Qardaşov',company='Apple'))

# ---------------------------------------------------------------------------------------------------------------------------------------

# Əgər dəyişən olan yerə '*' işarəsi qoyuruqsa, ondan sonra olan elementləri parametrləri ilə çağırmalıyıq.
def greeting(*, name, surname, company):
    return f'Salam, {name} {surname}, "{company}" şirkəti sizi salamlayır.'

print(greeting(name='Mətin', surname='Qardaşov', company='Apple'))

# ---------------------------------------------------------------------------------------------------------------------------------------

# Bu kod işləyəcək. Çünki '*' işarəsindən sonra 'surname' və 'company' olduğundan, onları çağırdığım zaman dəyişənləri ilə çağırmalıyıq.
def greeting(name, *, surname, company):
    return f'Salam, {name} {surname}, "{company}" şirkəti sizi salamlayır.'

print(greeting('Mətin', surname='Qardaşov', company='Apple'))

# ---------------------------------------------------------------------------------------------------------------------------------------

def plus_num(*args):
    return sum(args)
    # return '-'.join(map(str, args))

print(plus_num(1, 2, 3, 4, 5))

# ---------------------------------------------------------------------------------------------------------------------------------------

def person(**info):
    return info

print(person(name='Mətin', surname='Qardaşov', company='Apple', age=20, salary=5000))

# ---------------------------------------------------------------------------------------------------------------------------------------

def phone(**info):
    return info

iphone = phone(brand='iPhone', model='16', color='black', price=3000)
samsung = phone(brand='Samsung', model='S24', description='new')
xiaomi = phone(brand='Xiaomi', model='Redmi Note 12', price=2000, security='yes', color='white')

print(iphone)
print(samsung)
print(xiaomi)
print(f'{iphone["brand"]} => {iphone["model"]}')
print(f'{samsung["brand"]} => {samsung["model"]}')
print(f'{xiaomi["brand"]} => {xiaomi["model"]}')

# ---------------------------------------------------------------------------------------------------------------------------------------

import random
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(random.choices(nums, k=3))

# ---------------------------------------------------------------------------------------------------------------------------------------

def add_item(element, data_list=[]):
    data_list.append(element)
    return data_list

print(add_item(5))
print(add_item(10))

# ---------------------------------------------------------------------------------------------------------------------------------------

def add_item(element, data_list=None):
    if data_list is None:
        data_list = []
    data_list.append(element)
    return data_list

print(add_item(5, [1, 2, 3, 4]))
print(add_item(10, [7, 8, 9]))