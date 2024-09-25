from faker import Faker

fake_en = Faker('en_US')
fake_az = Faker('az_AZ')
fake_ru = Faker('ru_RU')
fake_ger = Faker('de_DE')


print(fake_en.name())
print(fake_en.country())
print(fake_en.city())
print(fake_en.address())
print(fake_en.phone_number())

# ---------------------------------------------------------------------------------------------------------------------------------------

print(fake_az.name())
print(fake_az.country())
print(fake_az.city())
print(fake_az.address())
print(fake_az.phone_number())

# ---------------------------------------------------------------------------------------------------------------------------------------

print(fake_ru.name())
print(fake_ru.country())
print(fake_ru.city())
print(fake_ru.address())
print(fake_ru.phone_number())

# ---------------------------------------------------------------------------------------------------------------------------------------

print(fake_ger.name())
print(fake_ger.country())
print(fake_ger.city())
print(fake_ger.address())
print(fake_ger.phone_number())

# ---------------------------------------------------------------------------------------------------------------------------------------

male_first_names = [fake_az.first_name_male() for _ in range(100)]
print(male_first_names)

# ---------------------------------------------------------------------------------------------------------------------------------------

credit_numbers = fake_en.credit_card_number()
print(credit_numbers)

# ---------------------------------------------------------------------------------------------------------------------------------------

company_email = fake_en.company_email()
print(company_email)

# ---------------------------------------------------------------------------------------------------------------------------------------

text = fake_az.text()
print(text)