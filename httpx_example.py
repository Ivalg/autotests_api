import httpx


# Метод httpx.get()
# response = httpx.get("https://jsonplaceholder.typicode.com/todos/1")
#
# print(response.status_code)
# print(response.json())

# Передача заголовков
# headers = {"Authorization": "Bearer my_secret_token"}
# response = httpx.get("https://httpbin.org/get", headers=headers)
# print(response.status_code)
# print(response.json())

# Работа с параметрами запроса
# params = {"userId": 4}
# response = httpx.get("https://jsonplaceholder.typicode.com/todos", params=params)
# print(response.url)  # https://jsonplaceholder.typicode.com/todos?userId=3
# print(response.json())  # Фильтрованный список задач


# # Метод httpx.post()
# data = {"title": "New task", "completed": False, "userId": 4}
# response = httpx.post("https://jsonplaceholder.typicode.com/todos", json=data)
# print(response.status_code)
# print(response.json)

# Отправка данных в application/x-www-form-urlencoded
# data = {"username": "test_user", "password": "123455"}
# response = httpx.post("https://httpbin.org/post", data=data)
# print(response.status_code)
# print(response.json())

# Отправка файлов
# files = {"file": ("example.txt", open("example.txt", "rb"))}
# response = httpx.post("https://httpbin.org/post", files=files)
# print(response.json())

# --------------------- Работа с сессиями (httpx.Client) -----------------------
# with httpx.Client() as client:
#     response1 = client.get("https://jsonplaceholder.typicode.com/todos/1")
#     response2 = client.get("https://jsonplaceholder.typicode.com/todos/2")
#
# print(response1.json())
# print(response2.json())

# ------------ Добавление базовых заголовков в Client --------------
# client = httpx.Client(headers={"Authorization": "Bearer my_secret_token"})
# response = client.get("https://httpbin.org/get")
# print(response.json())
# client.close() # сесию нужно закрывать (в контексном менеджере - автоматически)


## ----------------------- Работа с ошибками -------------------------------------
## Проверка статус кода ответа(raise_for_ststus)
# try:
#     response = httpx.get("https://jsonplaceholder.typicode.com/invalid-url")
#     response.raise_for_status()
# except httpx.HTTPError as e:
#     print(f"Ошибка запроса: {e}")

#  == Обработка таймаутов ==
# try:
#     response = httpx.get("https://httpbin.org/delay/5", timeout=2)
# except httpx.ReadTimeout:
#     print("Запрос превысил лимит времени")

