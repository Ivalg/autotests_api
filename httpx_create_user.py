import httpx
from tools.fakers import get_random_email

user_data = {
    "email": get_random_email(),
    "password": "qwerty",
    "lastName": "Ivanov",
    "firstName": "Ivan",
    "middleName": "Ivanovich"
}
response = httpx.post("http://localhost:8000/api/v1/users", json=user_data)

print(response.status_code)
print(response.json())