import httpx

data = {"email": "user1@example.com", "password": "string"}
login_response = httpx.post("http://localhost:8000/api/v1/authentication/login", json=data)
login_response_json = login_response.json()

access_token = login_response_json["token"]["accessToken"]
response = httpx.get("http://localhost:8000/api/v1/users/me", headers={"Authorization": f"Bearer {access_token}"})
print(response.status_code)
print(response.json())

