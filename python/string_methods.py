
# lower, upper, capitalize, title, swapcase, zfill, index, find, count, replace, strip, encode

text = 'Python and PostgreSql'
print(text.lower())
print(text.upper())
print(text.capitalize())
print(text.title())
print(text.swapcase())
print(text.zfill(30))
print(text.index('n'))
print(text.find('and'))
print(text.count('P'))
print(text.replace('Sql', 'SQL'))

# ---------------------------------------------------------------------------------------------------------------------------------------

text = '...I love Python and PostgreSql'
print(len(text))
print(text.strip('...'))
print(len(text.strip('...')))

# ---------------------------------------------------------------------------------------------------------------------------------------


text = 'Mənim adım Mətindir'
print(text.encode())

# ---------------------------------------------------------------------------------------------------------------------------------------

decoded = b'M\xc9\x99nim ad\xc4\xb1m M\xc9\x99tindir'
print(decoded.decode())

# ---------------------------------------------------------------------------------------------------------------------------------------

# startswith, endswith, isalpha, isalnum, isdigit, isdecimal, islower, isupper, istitle
text = 'Python'

print('Yes' if text.startswith('P') else 'No')
print('Yes' if text.endswith('n') else 'No')
print('Yes' if text.isalpha() else 'No')
print('Yes' if text.isalnum() else 'No')
print('Yes' if '\u0033'.isalnum() else 'No')
print('Yes' if text.isdigit() else 'No')
print('Yes' if '\u0033'.isdigit() else 'No')
print('Yes' if text.isdecimal() else 'No')
print('Yes' if '\u0033'.isdecimal() else 'No')
print('Yes' if text.islower() else 'No')
print('Yes' if text.isupper() else 'No')
print('Yes' if text.istitle() else 'No')