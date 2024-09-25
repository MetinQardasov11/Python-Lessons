import bcrypt
from getpass import getpass
import pwinput as pin
from typing import Generator
import names, json

password = 'Metinq2003'

hash_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
# print(hash_password)

pw1 = b'$2b$12$X2AW8cakly8GwJqdA80Dr.XW60b4wVUhPBUi.JhBEUi7mQG9bWtFi'
pw2 = b'$2b$12$7mQv40bl.Jg9nvlQXyNa6.xCCBbJ0NOQBxyTICRf39e1b/0p2NBz6'

if bcrypt.checkpw(password.encode('utf-8'), pw1):
    print('It matches ✅✅✅')
else:
    print('It does not match ❌❌❌')

# ---------------------------------------------------------------------------------------------------------------------------------------

password = getpass('Enter password: ')
print(password)

if bcrypt.checkpw(password.encode('utf-8'), pw1):
    print('It matches ✅✅✅')
else:
    print('It does not match ❌❌❌')

# ---------------------------------------------------------------------------------------------------------------------------------------

password = pin.pwinput(prompt='Enter password: ', mask='*')
check = bcrypt.checkpw(password.encode('utf-8'), pw1)

if check:
    print('Ok ✅✅✅')
else:
    print('NO ❌❌❌')
    
# və ya

print('Ok ✅✅✅' if check else 'NO ❌❌❌')

# ---------------------------------------------------------------------------------------------------------------------------------------

def generate_hash_password(password: bytes) -> bytes:
    return bcrypt.hashpw(password, bcrypt.gensalt())

def verify_user(password: str, hash_data: str) -> bool:
    return bcrypt.checkpw(password.encode(), hash_data.encode())

def get_user(gender: str | None = None) -> Generator:
    first_name, last_name = names.get_full_name(gender=gender).split()
    password = f'{first_name[0]}{last_name[0]}2024'
    password = generate_hash_password(password.encode())
    yield {
        "First Name" : first_name,
        "Last Name" : last_name,
        "Email" : f"{first_name.lower()}.{last_name.lower()}@gmail.com",
        "Password" : password.decode()
    }

with open('json/user.json', 'r') as file:
    data = json.load(file)

print(f'Welcom {data['First Name']}')
print('Sign in... 👋👋👋')
password = pin.pwinput(prompt='Enter password: ', mask='*')

if verify_user(password, data['Password']):
    print('Successfully logged in 🎉🎉🎉')
else:
    print('Wrong password ⛔️⛔️⛔️')