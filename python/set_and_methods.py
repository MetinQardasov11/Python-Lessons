# Set data tipi iterable, unordered, mutable

my_set = {1, 2, 3, 4, 5}
print(my_set)
print(type(my_set))

# ---------------------------------------------------------------------------------------------------------------------------------------

my_set = {'Orxan', 'Hikmet'}
my_set.add('Metin')
print(my_set)

# ---------------------------------------------------------------------------------------------------------------------------------------

my_set = {'Orxan', 'Hikmet', 'Osman', 'Ali'}
my_set.remove('Hikmet')
print(my_set)

# ---------------------------------------------------------------------------------------------------------------------------------------

# set data tipi unikal və imumtable olmalıdır. Yəni, əgər içində 2 ədəd eyni dəyişən yazsaq, birini qəbul edəcək və içində list, dict, set yaza bilmərik.
my_set = {'Orxan', 'Hikmet', 'Osman', 'Orxan', 'Ali'}
print(my_set)

for x in my_set:
    print(x)


# set data tipi həmçinin ordered-dir. Çünki daxilindəki ədədlər sıralanmır.
my_nums = {9, 1, 5, 2}
for x in my_nums:
    print(x)

# ---------------------------------------------------------------------------------------------------------------------------------------

# pop metodu
my_set = {'Orxan', 'Hikmet', 'Osman', 'Ali'}
deleted_value = my_set.pop()
print(deleted_value)

# ---------------------------------------------------------------------------------------------------------------------------------------

# copy metodu
my_set = {'Orxan', 'Hikmet', 'Osman', 'Ali'}
new_set = my_set.copy()
my_set.add('Metin')
print(my_set)
print(new_set)

# ---------------------------------------------------------------------------------------------------------------------------------------

# clear metodu
my_set = {'Orxan', 'Hikmet', 'Osman', 'Ali'}
my_set.clear()
print(my_set)

# ---------------------------------------------------------------------------------------------------------------------------------------

# discard metodu
my_set = {'Orxan', 'Hikmet', 'Osman', 'Ali'}
my_set.discard('Hikmet')
my_set.discard('Anar')
print(my_set)

# ---------------------------------------------------------------------------------------------------------------------------------------

my_class = ['Metin', 'Abdullah', 'Orxan', 'Hikmet', 'Abdullah', 'Osman', 'Ali', 'Abdullah']
my_set = set(my_class)
print(my_set)

my_word = 'test'
my_set = set(my_word)
print(my_set)

my_dict = {'one' : 'bir', 'two' : 'iki', 'three' : 'üç', 'four' : 'dörd', 'deux' : 'iki'}
my_set = set(my_dict)
new_set = set(my_dict.values())
print(my_set)
print(new_set)

# ---------------------------------------------------------------------------------------------------------------------------------------

nums1 = {1, 2, 3, 4, 5}
nums2 = {4, 5, 6, 7, 8}

# iki çoxluğun birləşməsi
print(nums1 | nums2)
print(nums1.union(nums2))

# iki çoxluğun kəsişməsi
print(nums1 & nums2)
print(nums1.intersection(nums2))

# simmetrik fərqlilik
print(nums1 ^ nums2)
print(nums1.symmetric_difference(nums2))

# birində işlənən digərində işlənməyən elementlər
print(nums1 - nums2)
print(nums1.difference(nums2))
print(nums2 - nums1)
print(nums2.difference(nums1))

# ---------------------------------------------------------------------------------------------------------------------------------------

set_1 = {1, 4, 5}
set_2 = {5, 1, 4}
print(set_1 == set_2)

# ---------------------------------------------------------------------------------------------------------------------------------------

set_1 = {1, 2, 3, 4, 5, 6, 7, 8, 9}
set_2 = {3, 5, 7}
print(set_2.issubset(set_1))

# ---------------------------------------------------------------------------------------------------------------------------------------

set_1 = {1, 2, 3}
set_2 = {4, 5, 6}
set_3 = {7, 8, 9}
set_1.update(set_2, set_3)
print(set_1)