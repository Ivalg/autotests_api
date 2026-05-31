from typing import TypedDict
from httpx import Response
from clients.api_client import APIClient
from clients.public_http_builder import get_public_http_client


class User(TypedDict):
    """Описание структуры пользователя"""
    id: str
    email: str
    lastName: str
    firstName: str
    middleName: str


class CreateUserRequestDict(TypedDict):
    """
    Описание структуры запроса на создание пользователя
    """
    email: str
    password: str
    firstName: str
    lastName: str
    middleName: str


class CreateUserResponseDict(TypedDict):
    """Описание структуры создания пользователя"""
    user: User


class PublicUsersClient(APIClient):
    """
    Клиент для /api/v1/users
    """
    def create_user_api(self, request: CreateUserRequestDict) -> Response:
        """
        Создание пользователя

        :param request: Словарь с данными пользователя
        :return: Объект httpx.Response
        """
        return self.post("/api/v1/users", json=request)

    def create_user(self, request: CreateUserRequestDict) -> CreateUserResponseDict:
        response = self.create_user_api(request)
        return response.json()


# builder для PublicUsersClient
def get_public_users_client() -> PublicUsersClient:
    """
    Функция создает экземпляр PublicUsersClient с уже настроенным HTTP клиентом
    :return: Готовый к использованию PublicUsersClient
    """
    return PublicUsersClient(client=get_public_http_client())
