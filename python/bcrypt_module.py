import bcrypt
from getpass import getpass # Şifrəni görməmək üçün istifadə olunur.

pwd = b'metin qardasov'

hashed_pwd = bcrypt.hashpw(pwd, bcrypt.gensalt())
print(hashed_pwd)


user_pass = getpass('Enter your password: ').encode()

if bcrypt.checkpw(user_pass, hashed_pwd):
    print('Correct password')
else:
    print('Wrong password')
    
