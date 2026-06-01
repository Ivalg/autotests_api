from clients.api_client import APIClient
from clients.private_http_builder import get_private_http_client, AuthenticationUserSchema
from httpx import Response
from typing import TypedDict


class User(TypedDict):
    """Описание структуры пользователя"""
    id: str
    email: str
    lastName: str
    firstName: str
    middleName: str


class UpdateUserRequestDict(TypedDict):
    """Описание структуры запроса на обновление пользователя"""
    email: str | None
    firstName: str | None
    lastName: str | None
    middleName: str | None


class GetUserResponseDict(TypedDict):
    """Описание структуры создания пользователя"""
    user: User


class PrivateUserClient(APIClient):
    """
    Клиент для работы с /api/v1/users
    """
    def get_user_me_api(self) -> Response:
        """
        Получение текущего пользователя
        :return: Объект httpx.Response
        """
        return self.get("/api/v1/users/me")

    def get_user_api(self, user_id: str) -> Response:
        """
        Получение пользователя по идентификатору
        :param user_id: Идентификатор пользователя
        :return: Объект httpx.Response
        """
        return self.get(f"/api/v1/users/{user_id}")

    def update_user_id(self, user_id, request: UpdateUserRequestDict) -> Response:
        """
        Обновление пользователя по идентификатору
        :param user_id: Идентификатор пользователя
        :param request: Словарь с email, firstName, lastName, middleName
        :return: Объект httpx.Response
        """
        return self.patch(f"/api/v1/users/{user_id}", json=request)

    def delete_user_api(self, user_id: str) -> Response:
        """
        Удаление пользователя по идентификатору
        :param user_id: Идентификатор пользователя
        :return: Объект httpx.Response
        """
        return self.delete(f"/api/v1/users/{user_id}")

    def get_user(self, user_id: str) -> GetUserResponseDict:
        response = self.get_user_api(user_id)
        return response.json()


# builder для PrivateUserClient
def get_private_users_client(user: AuthenticationUserSchema) -> PrivateUserClient:
    """
    Функция создает экземпляр PrivateUserClient с уже настроенным HTTP клиентом
    :param user:
    :return: Готовый к использованию PrivateUserClient
    """
    return PrivateUserClient(client=get_private_http_client(user))
