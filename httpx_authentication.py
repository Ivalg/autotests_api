import httpx

payload = {"email": "user1@example.com", "password": "string"}

# Выполняем запрос на аутентификацию
login_response = httpx.post("http://localhost:8000/api/v1/authentication/login", json=payload)
login_response_data = login_response.json()

print("Status code:", login_response.status_code)
print("Login response:", login_response_data)

# Формируем payload для обновления токена
refresh_payload = {"refreshToken": login_response_data["token"]["refreshToken"]}

# Выполняем запрос на обновление токена
refresh_response = httpx.post("http://localhost:8000/api/v1/authentication/refresh", json=refresh_payload)
refresh_response_data = refresh_response.json()

# Выводим обновленные токены
print("Status code:", refresh_response.status_code)
print("Refresh response:", refresh_response_data)
