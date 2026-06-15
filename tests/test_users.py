from http import HTTPStatus
import pytest
from clients.users.public_users_client import get_public_users_client, PublicUsersClient
from clients.users.private_users_client import PrivateUsersClient
from clients.users.users_schema import CreateUserRequestSchema, CreateUserResponseSchema, GetUserResponseSchema
from fixtures.users import UserFixture
from tools.assertions.base import assert_status_code
from tools.assertions.schema import validate_json_schema
from tools.assertions.users import assert_create_user_response, assert_get_user_response


# def test_create_user():
#     # Получаем экземпляр API-клиента для работы с API
#     public_users_client = get_public_users_client()
#
#     # Создаем объект запроса, используя Pydantic-схему
#     request = CreateUserRequestSchema()
#     # Вызываем метод API-клиента для отправки POST-запроса
#     response = public_users_client.create_user_api(request)
#
#     # Проверяем, что сервер вернул статус-код - 200 OK.
#     assert response.status_code == HTTPStatus.OK, "Некорректный статус код ответа"


# def test_create_user():
#     # Получаем экземпляр API-клиента для работы с API
#     public_users_client = get_public_users_client()
#
#     # Создаем объект запроса, используя Pydantic-схему
#     request = CreateUserRequestSchema()
#     # Вызываем метод API-клиента для отправки POST-запроса
#     response = public_users_client.create_user_api(request)
#
#     # Инициализируем модель ответа на основе полученного JSON в ответе
#     # Также благодаря встроенной валидации в Pydantic дополнительно убеждаемся, что ответ корректный
#     response_data = CreateUserResponseSchema.model_validate_json(response.text)
#
#     # Проверяем, что сервер вернул статус-код - 200 OK.
#     assert response.status_code == HTTPStatus.OK, "Некорректный статус код ответа"
#
#     assert response_data.user.email == request.email, 'Некорректный email пользователя'
#     assert response_data.user.last_name == request.last_name, 'Некорректный last_name пользователя'
#     assert response_data.user.first_name == request.first_name, 'Некорректный first_name пользователя'
#     assert response_data.user.middle_name == request.middle_name, 'Некорректный middle_name пользователя'


# =================================== до использования фикстур ======================================


# @pytest.mark.users
# @pytest.mark.regression
# def test_create_user():
#     public_users_client = get_public_users_client()
#
#     request = CreateUserRequestSchema()
#     response = public_users_client.create_user_api(request)
#     response_data = CreateUserResponseSchema.model_validate_json(response.text)
#
#     # Используем отдельную функцию для поверки статус-кода
#     assert_status_code(response.status_code, HTTPStatus.OK)
#
#     # Используем отдельную функцию для проверки ответа создания пользователя
#     assert_create_user_response(request, response_data)
#
#     # Проверяем, что тело ответа соответствует ожидаемой JSON-схеме
#     validate_json_schema(response.json(), response_data.model_json_schema())


@pytest.mark.users
@pytest.mark.regression
def test_create_user(public_users_client: PublicUsersClient):  # Используем фикстуру

    request = CreateUserRequestSchema()
    response = public_users_client.create_user_api(request)
    response_data = CreateUserResponseSchema.model_validate_json(response.text)

    assert_status_code(response.status_code, HTTPStatus.OK)
    assert_create_user_response(request, response_data)

    validate_json_schema(response.json(), response_data.model_json_schema())


@pytest.mark.users
@pytest.mark.regression
def test_get_user_me(private_users_client: PrivateUsersClient, function_user: UserFixture):

    response = private_users_client.get_user_me_api()
    response_data = GetUserResponseSchema.model_validate_json(response.text)

    assert_status_code(response.status_code, HTTPStatus.OK)
    assert_get_user_response(response_data, function_user.response)

    validate_json_schema(response.json(), response_data.model_json_schema())
