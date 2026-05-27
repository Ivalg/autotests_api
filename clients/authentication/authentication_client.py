from clients.api_client import APIClient
from httpx import Response
from typing import TypedDict
from clients.public_http_builder import get_public_http_client  # Импортируем builder


class Token(TypedDict):
    """Описание структуры аутентификационных токенов"""
    tokenType: str
    accessToken: str
    refreshToken: str


class LoginRequestDict(TypedDict):
    """
    Описание структуры запроса на аутентификацию
    """
    email: str
    password: str


class LoginResponseDict(TypedDict):
    """Описание структуры ответа аутентификации"""
    token: str


class RefreshRequestDict(TypedDict):
    """
    Описание структуры запроса для обновления токена
    """
    refreshToken: str


class AuthenticationClient(APIClient):
    """
    Клиент для работы с /api/v1/authentication
    """

    def login_api(self, request: LoginRequestDict) -> Response:
        """
        Метод выполняет аутентификацию пользователя
        :param request: Словарь с email / password
        :return: Ответ от сервера. Объект httpx.Response
        """
        return self.post("/api/v1/authentication/login", json=request)

    def refresh_api(self, request: RefreshRequestDict) -> Response:
        """
        Метод обновляет токен авторизации

        :param request: Словарь refreshToken
        :return: Ответ от сервера. Объект httpx.Response
        """
        return self.post("/api/v1/authentication/refresh", json=request)

    def login(self, request: LoginRequestDict) -> LoginResponseDict:
        response = self.login_api(request)  # отправляем запрос на аутентификацию
        return response.json()  # возвращаем JSON
    

# builder для AuthenticationClient
def get_authentication_client() -> AuthenticationClient:
    """
    Функция создает экземпляр AuthenticationClient с уже настроенным HTTP клиентом
    :return: Готовый к использованию AuthenticationClient
    """
    return AuthenticationClient(client=get_public_http_client())
