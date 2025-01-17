import requests

url = 'http://127.0.0.1:8000/auth/users/me/'

headers = {
    "Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzM3MDkzNTUzLCJpYXQiOjE3MzcwOTMyNTMsImp0aSI6IjVjZmViMDM4NGVkMDRkZDc5ZDY2YWE5M2QxZDllZjdlIiwidXNlcl9pZCI6MX0.LwRivAN9A0alLWUkFnj9Ld_ioQr7wZ8PUmZS7Izq6nY"
}

response = requests.get(url, headers=headers)

print(response.json())
