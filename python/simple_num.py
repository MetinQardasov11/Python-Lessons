start = int(input("Start: "))
finish = int(input("Finish: "))

print(f'Simple numbers between {start} and {finish} are: ')

for num in range(start, finish+1):
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                break
        else:
            print(num)