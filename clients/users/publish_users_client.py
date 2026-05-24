from typing import TypedDict
from httpx import Response
from clients.api_client import APIClient


class CreateUserRequestDict(TypedDict):
    """
    Описание структуры запроса на создание пользователя
    """
    email: str
    password: str
    firstName: str
    lastName: str
    middleName: str


class PublishUsersClient(APIClient):
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
