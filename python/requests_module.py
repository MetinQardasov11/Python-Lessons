import requests, string, random

url = 'https://www.azernews.az/nation/218058.html'
r = requests.get(url)

# print(r.text)
# print(r.status_code)
# print(r.headers)

# --------------------------------------------------------------------------------------------------------------------------------------------------

url = 'https://www.azernews.az/media/2023/11/27/fotoramdrio.jpg'
r = requests.get(url)

# print(r.headers)
# print(r.content)

# --------------------------------------------------------------------------------------------------------------------------------------------------

data_jpg = r.content

# with open('img/shahdag.jpg', 'wb') as file:
#     file.write(data_jpg)
    
# print('DONE')

# --------------------------------------------------------------------------------------------------------------------------------------------------

url = 'https://jsonplaceholder.typicode.com/posts'
r = requests.get(url)

data = r.json()
# print(data)

# for x in data:
#     print(x['id'], x['title'])
    
# --------------------------------------------------------------------------------------------------------------------------------------------------

url = 'https://jsonplaceholder.typicode.com/posts/29'
r = requests.get(url)

data = r.json()

# print(data['id'], data['title'])

# --------------------------------------------------------------------------------------------------------------------------------------------------

# url ='http://httpbin.org/delay/1'
# r = requests.post(url)

# print(r)
# print(r.text)

# --------------------------------------------------------------------------------------------------------------------------------------------------

url = 'http://httpbin.org/basic-auth/metinqardasov/11112003Mm'
my_login = 'metinqardasov'
my_password = '11112003Mm'
r = requests.get(url, auth=(my_login, my_password))
# print(r.text)

# --------------------------------------------------------------------------------------------------------------------------------------------------

# url = 'https://xalqqazeti.az/az/iqtisadiyyat'
my_params = {'page': 1, 'per_page': '10'}
r = requests.get(url, params=my_params)
# print(r.status_code)
# print(r.url)

# --------------------------------------------------------------------------------------------------------------------------------------------------

url = 'http://httpbin.org/post'

my_info = {
    'username' : 'metinqardasov',
    'password' : '11112003Mm'
}

r = requests.post(url, data=my_info)
print(r.text)

data = r.json()['form']
# username, password = data['username'], data['password']
# print(f'username: {username} => password: {password}')

# --------------------------------------------------------------------------------------------------------------------------------------------------

url = 'https://picsum.photos/seed/'

def rand_url(width: int=200, height: int=200,length: int=15):
    rand_str = ''.join(random.sample(string.ascii_letters, k=length))
    return f'https://picsum.photos/seed/{rand_str}/{width}/{height}'

def get_image_url(data_url):
    r = requests.get(data_url)
    if r.ok:
        return r.url, r.content
    return False


for x in range(20):
    image_url, image_data = get_image_url(rand_url(400, 600))
    with open(f'img/picsum/photo_{x}.jpg', 'wb') as file:
        file.write(image_data)