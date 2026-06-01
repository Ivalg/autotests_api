from clients.api_client import APIClient
from clients.files.files_client import File
from clients.users.private_users_client import User
from clients.private_http_builder import get_private_http_client, AuthenticationUserSchema
from typing import TypedDict
from httpx import Response, QueryParams


class Course(TypedDict):
    """Описание структуры курса"""
    id: str
    title: str
    maxScore: int
    minScore: int
    description: str
    previewFile: File
    estimatedTime: str
    createdByUser: User


class GetCoursesQueryDict(TypedDict):
    """Описание структуры запроса на получение списка курсов"""
    userId: str


class CreateCourseRequestDict(TypedDict):
    """Описание структуры запроса на создание курса"""
    title: str
    maxScore: int
    minScore: int
    description: str
    estimateTime: str
    previewFileId: str
    createdByUserId: str


class CreateCourseResponseDict(TypedDict):
    """Описание структуры ответа создания курса"""
    course: Course


class UpdateCourseRequestDict(TypedDict):
    """Описание структуры запроса на обновление курса"""
    title: str | None
    maxScore: int | None
    minScore: int | None
    description: str | None
    estimateTime: str | None


class CoursesClient(APIClient):
    """Клиент для работы с api/v1/courses"""

    def get_courses_api(self, query: GetCoursesQueryDict) -> Response:
        """
        Получить список курсов
        :param query: Словарь с userId
        :return: Объект httpx.Response
        """
        return self.get(f"/api/v1/courses", params=QueryParams(**query))

    def get_course_api(self, course_id: str) -> Response:
        """
        Метод получения курса по ID
        :param course_id: Идентификатор курса
        :return: Объект httpx.Response
        """
        return self.get(f"/api/v1/courses/{course_id}")

    def create_course_api(self, request: CreateCourseRequestDict) -> Response:
        """
        Создание курса
        :param request: Словарь с title, maxScore, minScore, description, estimatedTime, previewFileId, createByUserId
        :return: Объект httpx.Response
        """
        return self.post("/api/v1/courses", json=request)

    def update_course_api(self, course_id: str, request: UpdateCourseRequestDict) -> Response:
        """
        Обновление курса
        :param course_id: Идентификатор курса
        :param request: Словарь с title, maxScore, minScore, description, estimatedTime
        :return: Объект httpx.Response
        """
        return self.patch(f"/api/v1/courses/{course_id}", json=request)

    def delete_course_api(self, course_id: str) -> Response:
        """
        Удаление курса
        :param course_id: Идентификатор курса
        :return: Объект httpx.Response
        """
        return self.delete(f"/api/v1/courses/{course_id}")

    def create_course(self, request: CreateCourseRequestDict) -> CreateCourseResponseDict:
        response = self.create_course_api(request)
        return response.json()


# builder для CoursesClient
def get_courses_client(user: AuthenticationUserSchema) -> CoursesClient:
    """
    Функция создает экземпляр CoursesClient с уже настроенным HTTP клиентом

    :return: Готовый к использованию CoursesClient
    """
    return CoursesClient(client=get_private_http_client(user))
