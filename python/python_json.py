import json
import names
import random



data = {
    'students' : ['Metin', 'Omer', 'Osman', 'Zubeyr'],
    'exam' : True,
    'count' : 24,
    'info' : {
        'subject' : 'Fundamentals of Computer Science',
        'date' : '2020-01-01'
    }
}

data = {
    'students' : None,
    2 : True,
    None : 24,
    'tuple' : (11, 12, 13),
    True : {
        'subject' : 'Fundamentals of Computer Science',
        'date' : '2020-01-01'
    }
}

with open('json/data.json', 'w') as file:
    json.dump(data, file, indent=4)


# ---------------------------------------------------------------------------------------------------------------------------------------


data = [{ 'name' : names.get_full_name(), 'point' : random.randint(80, 100)} for x in range(15)]
with open('json/students.json', 'w') as file:
    json.dump(data, file, indent=4)


# ---------------------------------------------------------------------------------------------------------------------------------------


with open('json/students.json') as file:
    # data = file.read()
    data = json.load(file)
    
print(data)
print(type(data))
print(data[2]['name'])
print(data[2]['point'])

for x in data:
    print(f'{x.get("name")} => {x.get("point")}')


# ---------------------------------------------------------------------------------------------------------------------------------------


data = {'Name' : 'Metin', 'age' : 22, 'email' : 'metin.qardasov2003@gmail.com'}
data_json = json.dumps(data)
print(data_json)


# ---------------------------------------------------------------------------------------------------------------------------------------


str_json = '{"Name": "Metin", "age": 22, "email": "metin.qardasov2003@gmail.com"}'
python_data = json.loads(str_json)
print(python_data)
print(python_data['Name'])