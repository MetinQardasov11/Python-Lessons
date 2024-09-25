
# Ədədin öz rəqəmlərə bölünməsini yoxlamaq
def is_divisable(num):
    if '0' in num:
        return False
    
    for i in num:
        if int(num) % int(i) != 0:
            return False
    return True
        
a = input('Enter the num: ')
print(is_divisable(a))

# ---------------------------------------------------------------------------------------------------------------------------------------

# Öz rəqəmlərinə bölünən ədədləri tapmaq

def get_divisables(n):
    nums = []
    
    for i in range(10**(n-1), (10**n)):
        if '0' in str(i):
            continue
        for j in str(i):
            if i % int(j) != 0:
                break    
        else:
            nums.append(i)
            
    return nums
            
print(get_divisables(2))

# ---------------------------------------------------------------------------------------------------------------------------------------

# və ya

def get_divisables(n):
    nums = []
    
    for i in range(10**(n-1), (10**n)):
        if '0' in str(i) or len(set(str(i))) < n:
            continue
        if all(i % int(j) == 0 for j in str(i)):
            nums.append(i)
            
    return nums

print(get_divisables(2))