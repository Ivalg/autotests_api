from httpx import Response
from clients.api_client import APIClient
from clients.private_http_builder import get_private_http_client, AuthenticationUserSchema
from clients.courses.courses_schema import (GetCoursesQuerySchema, CreateCourseRequestSchema,
                                            UpdateCourseRequestSchema, CreateCourseResponseSchema)


class CoursesClient(APIClient):
    """Клиент для работы с api/v1/courses"""

    def get_courses_api(self, query: GetCoursesQuerySchema) -> Response:
        """
        Получить список курсов
        :param query: Словарь с userId
        :return: Объект httpx.Response
        """
        return self.get(f"/api/v1/courses", params=query.model_dump(by_alias=True))  # type: ignore[arg-type]

    def get_course_api(self, course_id: str) -> Response:
        """
        Метод получения курса по ID
        :param course_id: Идентификатор курса
        :return: Объект httpx.Response
        """
        return self.get(f"/api/v1/courses/{course_id}")

    def create_course_api(self, request: CreateCourseRequestSchema) -> Response:
        """
        Создание курса
        :param request: Словарь с title, maxScore, minScore, description, estimatedTime, previewFileId, createByUserId
        :return: Объект httpx.Response
        """
        return self.post("/api/v1/courses", json=request.model_dump(by_alias=True))

    def update_course_api(self, course_id: str, request: UpdateCourseRequestSchema) -> Response:
        """
        Обновление курса
        :param course_id: Идентификатор курса
        :param request: Словарь с title, maxScore, minScore, description, estimatedTime
        :return: Объект httpx.Response
        """
        return self.patch(f"/api/v1/courses/{course_id}", json=request.model_dump(by_alias=True))

    def delete_course_api(self, course_id: str) -> Response:
        """
        Удаление курса
        :param course_id: Идентификатор курса
        :return: Объект httpx.Response
        """
        return self.delete(f"/api/v1/courses/{course_id}")

    def create_course(self, request: CreateCourseRequestSchema) -> CreateCourseResponseSchema:
        response = self.create_course_api(request)
        return CreateCourseResponseSchema.model_validate_json(response.text)


# builder для CoursesClient
def get_courses_client(user: AuthenticationUserSchema) -> CoursesClient:
    """
    Функция создает экземпляр CoursesClient с уже настроенным HTTP клиентом

    :return: Готовый к использованию CoursesClient
    """
    return CoursesClient(client=get_private_http_client(user))
