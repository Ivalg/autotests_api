from clients.api_client import APIClient
from clients.private_http_builder import AuthenticationUserDict, get_private_http_client
from typing import TypedDict
from httpx import Response


class CreateFileRequestDict(TypedDict):
    """Описание структуры запроса на создание файла"""
    filename: str
    directory: str
    upload_file: str


class FilesClient(APIClient):
    """Клиент для работы api/v1/files"""

    def get_file_api(self, file_id: str) -> Response:
        """
        Метод получения файла
        :param file_id: Идентификатор файла
        :return: Объект httpx.Response
        """
        return self.get(f"/api/v1/files/{file_id}")

    def create_file_api(self, request: CreateFileRequestDict) -> Response:
        """
        Метод создания файла
        :param request: Словарь filename, directory, upload_file
        :return: Объект httpx.Response
        """
        return self.post(
            "/api/v1/files",
            data=request,
            files={"upload_file": open(request["upload_file"], "rb")}
        )

    def delete_file(self, file_id: str) -> Response:
        """
        Метод удаления файла
        :param file_id: Идентификатор файла
        :return: Объект httpx.Response
        """
        return self.delete(f"/api/v1/files/{file_id}")


# builder для FilesClient
def get_files_client(user: AuthenticationUserDict) -> FilesClient:
    """
    Функция создает экземпляр FilesClient с уже настроенным HTTP клиентом

    :return: Готовый к использованию FilesClient
    """
    return FilesClient(client=get_private_http_client(user))
