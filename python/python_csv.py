import csv
import names
import random
import string

with open('csv/sample_data.csv') as file:
    csv_reader = csv.reader(file, delimiter=',')
    header = next(csv_reader)
    for x in csv_reader:
        print(x[0])
        
# ---------------------------------------------------------------------------------------------------------------------------------------

def parse_csv(filename, delimiter=',', show_header=True):
    data = []
    
    with open(filename) as file:
        csv_reader = csv.DictReader(file, delimiter=delimiter)
        
        if not show_header:
            header = next(csv_reader)

        for row in csv_reader:
            data.append(row)
    
    return data

print(parse_csv('csv/sample_data.csv', show_header=False))

# ---------------------------------------------------------------------------------------------------------------------------------------

def person_info():
    while True:
        first_name, last_name = names.get_full_name().split(' ')
        code = ''.join(random.choices(string.ascii_letters, k=7))
        
        yield {
            "firstname": first_name,
            "lastname": last_name,
            "email": f'{first_name.lower()}.{last_name.lower()}@gmail.com',
            "age": random.randint(18, 60),
            "code": code
        }

data_person = person_info()

with open('csv/person_data.csv', 'w') as file:
    field_name_list = ['firstname', 'lastname', 'email', 'age', 'code']
    csv_writer = csv.DictWriter(file, fieldnames=field_name_list)
    csv_writer.writeheader()
    # csv_writer.writerows([next(data_person) for _ in range(100)])
    
    for x in range(1000):
        print(x)
        csv_writer.writerow(next(data_person))

print('DONE!')