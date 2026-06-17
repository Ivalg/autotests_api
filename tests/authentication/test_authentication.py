from http import HTTPStatus
import pytest
from clients.authentication.authentication_client import AuthenticationClient, get_authentication_client
from clients.users.public_users_client import get_public_users_client, PublicUsersClient
from clients.users.users_schema import CreateUserRequestSchema
from clients.authentication.authentication_schema import LoginResponseSchema, LoginRequestSchema
from fixtures.users import UserFixture
from tools.assertions.authentication import assert_login_response
from tools.assertions.base import assert_status_code
from tools.assertions.schema import validate_json_schema


# ============================================ до фикстуры function_user =============================

# @pytest.mark.regression
# @pytest.mark.authentication
# def test_login(public_users_client: PublicUsersClient, authentication_client: AuthenticationClient):
#
#     create_user_request = CreateUserRequestSchema()
#     public_users_client.create_user(create_user_request)
#
#     login_request = LoginRequestSchema(
#         email=create_user_request.email,
#         password=create_user_request.password
#     )
#     login_response = authentication_client.login_api(login_request)
#     login_response_data = LoginResponseSchema.model_validate_json(login_response.text)
#
#     # Проверяем статус-код
#     assert_status_code(login_response.status_code, HTTPStatus.OK)
#     # Проверяем данные в ответе
#     assert_login_response(login_response_data)
#     # Проверяем структуру JSON ответа
#     validate_json_schema(login_response.json(), login_response_data.model_json_schema())


@pytest.mark.regression
@pytest.mark.authentication
class TestAuthentication:
    def test_login(self, function_user: UserFixture, authentication_client: AuthenticationClient):
        request = LoginRequestSchema(email=function_user.email, password=function_user.password)
        response = authentication_client.login_api(request)
        response_data = LoginResponseSchema.model_validate_json(response.text)

        assert_status_code(response.status_code, HTTPStatus.OK)
        assert_login_response(response_data)
        validate_json_schema(response.json(), response_data.model_json_schema())
