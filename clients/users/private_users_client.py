from httpx import Response
from clients.api_client import APIClient
from clients.private_http_builder import get_private_http_client, AuthenticationUserSchema
from clients.users.users_schema import UpdateUserRequestSchema, GetUserResponseSchema


class PrivateUsersClient(APIClient):
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

    def update_user_id(self, user_id, request: UpdateUserRequestSchema) -> Response:
        """
        Обновление пользователя по идентификатору
        :param user_id: Идентификатор пользователя
        :param request: Словарь с email, firstName, lastName, middleName
        :return: Объект httpx.Response
        """
        return self.patch(f"/api/v1/users/{user_id}", json=request.model_dump(by_alias=True))

    def delete_user_api(self, user_id: str) -> Response:
        """
        Удаление пользователя по идентификатору
        :param user_id: Идентификатор пользователя
        :return: Объект httpx.Response
        """
        return self.delete(f"/api/v1/users/{user_id}")

    def get_user(self, user_id: str) -> GetUserResponseSchema:
        response = self.get_user_api(user_id)
        return GetUserResponseSchema.model_validate_json(response.text)


# builder для PrivateUsersClient
def get_private_users_client(user: AuthenticationUserSchema) -> PrivateUsersClient:
    """
    Функция создает экземпляр PrivateUsersClient с уже настроенным HTTP клиентом
    :return: Готовый к использованию PrivateUsersClient
    """
    return PrivateUsersClient(client=get_private_http_client(user))
