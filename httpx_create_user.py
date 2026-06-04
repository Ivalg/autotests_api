import httpx
from tools.fakers import fake

user_data = {
    "email": fake.email(),
    "password": "qwerty",
    "lastName": "Ivanov",
    "firstName": "Ivan",
    "middleName": "Ivanovich"
}
response = httpx.post("http://localhost:8000/api/v1/users", json=user_data)

print(response.status_code)
print(response.json())
