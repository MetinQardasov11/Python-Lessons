
# Daxil edilən ədədlərin armstrong sayı olub-olmamasını yoxlayan proqram
def is_armstrong_number(number):
    number = str(number)
    sum_num = 0
    for i in number:
        sum_num += int(i) ** len(number)
        
    if sum_num == int(number):
        return True
    return False

print(is_armstrong_number(153))
print(is_armstrong_number(8208))
print(is_armstrong_number(3223))

# ---------------------------------------------------------------------------------------------------------------------------------------

# və ya

def is_armstrong_number(number):
    number = str(number)
    arm = sum(int(x)**len(number) for x in number)
    if arm == int(number):
        return True
    return False

print(is_armstrong_number(153))
print(is_armstrong_number(8208))
print(is_armstrong_number(3223))

# ---------------------------------------------------------------------------------------------------------------------------------------

# və ya

def is_armstrong_number(number):
    return True if int(number) == sum(int(x)**len(str(number)) for x in str(number)) else False

print(is_armstrong_number(153))
print(is_armstrong_number(8208))
print(is_armstrong_number(3223))

# ---------------------------------------------------------------------------------------------------------------------------------------

# Klaviaturadan daxil edilən n rəqəmli ədədlərdən armstrong sayı olan ədədləri ekrana çap edən proqram
def armstrong_num(n):
    nums = []
    
    for x in range(10**(n-1), 10**n):
        arm = 0
        
        for i in str(x):
            arm += int(i) ** n
            
        if arm == int(x):
            nums.append(arm)
    
    return nums

print(armstrong_num(3))
print(armstrong_num(4))

# ---------------------------------------------------------------------------------------------------------------------------------------

# və ya

def armstrong_num(n):
    nums = []
    
    for x in range(10**(n-1), 10**n):
        arm = sum(int(i)**n for i in str(x))
                
        if arm == int(x):
            nums.append(arm)
    
    return nums

print(armstrong_num(3))
print(armstrong_num(4))

# ---------------------------------------------------------------------------------------------------------------------------------------

# və ya

def armstrong_num(n):
    nums = []
    
    for x in range(10**(n-1), 10**n):
        arm = sum(int(i)**n for i in str(x))
                
        if arm == int(x):
            nums.append(arm)
    
    return nums