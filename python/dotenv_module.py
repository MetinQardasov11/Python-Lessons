from dotenv import load_dotenv
import os

load_dotenv('.env')

username: str = os.getenv('USERNAME')
password: str = os.getenv('PASSWORD')
print(username)
print(password)

# ---------------------------------------------------------------------------------------------------------------------------------------

def get_api_url(url: str, *, api: str) -> str:
    return '/'.join((url, api))

url: str = os.getenv('URL')
api: str = os.getenv('API_KEY')
print(get_api_url(url=url, api=api))