from clients.private_http_builder import AuthenticationUserDict
from clients.users.public_users_client import get_public_users_client, CreateUserRequestDict
from clients.users.private_users_client import get_private_users_client
from tools.fakers import get_random_email

# Инициализируем клиент PublicUserClient
public_users_client = get_public_users_client()

# Инициализируем запрос на создание пользователя
create_user_request = CreateUserRequestDict(
    email=get_random_email(),
    password="qwert",
    lastName="Ivanov",
    firstName="Ivan",
    middleName="Ivanovich"
)
# Отправляем POST запрос на создание пользователя
create_user_response = public_users_client.create_user(create_user_request)
print("Create user data", create_user_response)

# Инициализируем пользовательские данные для аутентификации
authentication_user = AuthenticationUserDict(
    email=create_user_request['email'],
    password=create_user_request['password']
)
# Инициализируем клиент PrivateUserClient
private_users_client = get_private_users_client(authentication_user)

# Отправляем GET запрос на получение данных пользователя
get_user_response = private_users_client.get_user(create_user_response['user']['id'])
print("Get user data", get_user_response)
