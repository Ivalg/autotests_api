from clients.api_client import APIClient
from typing import TypedDict
from httpx import Response, QueryParams


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
    createByUserId: str


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
