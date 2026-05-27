from httpx import Client
from typing import TypedDict
from clients.authentication.authentication_client import get_authentication_client, LoginRequestDict


class AuthenticationUserDict(TypedDict):
    """Структура данных пользователя для авторизации"""
    email: str
    password: str


# private builder
def get_private_http_client(user: AuthenticationUserDict) -> Client:
    """
    Функция создает экземпляр httpx.Client с аутентификацией пользователя
    :param user: Объект AuthenticationUserSchema с email и паролем пользователя
    :return: Готовый к использованию объект httpx.Client c установленным заголовком Authorization
    """
    authentication_client = get_authentication_client()

    login_request = LoginRequestDict(email=user['email'], password=user['password'])
    login_response = authentication_client.login(login_request)  # запрос на аутентификацию

    return Client(
        timeout=100,
        base_url="http://localhost:8000",
        headers={"Authorization": f"Bearer {login_response['token']['accessToken']}"}
    )
