import httpx
from tools.fakers import get_random_email

# Создаем пользователя
create_user_payload = {
    "email": get_random_email(),
    "password": "qwert",
    "firstName": "Ivan",
    "lastName": "Ivanov",
    "middleName": "Ivanovich"
}
create_user_response = httpx.post("http://localhost:8000/api/v1/users", json=create_user_payload)
create_user_response_data = create_user_response.json()

# Проходим аутентификацию
login_payload = {
    "email": create_user_payload["email"],
    "password": create_user_payload["password"]
}
login_response = httpx.post("http://localhost:8000/api/v1/authentication/login", json=login_payload)
login_response_data = login_response.json()

# Выполняем загрузку файла
create_file_headers = {
    "Authorization": f"Bearer {login_response_data["token"]["accessToken"]}"
}
create_file_response = httpx.post(
    "http://localhost:8000/api/v1/files",
    data={"filename": "avatar.png", "directory": "courses"},
    files={"upload_file": open("./testdata/files/avatar.png", "rb")},
    headers=create_file_headers
)
create_file_response_data = create_file_response.json()
print("Create file data:", create_file_response_data)
