import httpx

# Проходим аутентификацию
login_payload = {
    "email": "user1@example.com",
    "password": "string"
}
login_response = httpx.post("http://localhost:8000/api/v1/authentication/login", json=login_payload)
login_response_data = login_response.json()
print("Login data:", login_response_data)

# Инициализируем клиент
client = httpx.Client(
    base_url="http://localhost:8000/",
    timeout=100,
    headers={"Authorization": f"Bearer {login_response_data['token']['accessToken']}"}
)

# Выполняем запрос с авторизацией
get_user_response = client.get("/api/v1/users/me")
get_user_response_data = get_user_response.json()
print("User data:", get_user_response_data)
