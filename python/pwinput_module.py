import pwinput

pw_1 = pwinput.pwinput('Password: ', mask='*')
pw_2 = pwinput.pwinput('Password: ', mask='.')
pw_3 = pwinput.pwinput('Password: ', mask='')

print(pw_1)
print(pw_2)
print(pw_3)