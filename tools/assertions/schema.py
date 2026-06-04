from typing import Any
from jsonschema import validate
from jsonschema.validators import Draft202012Validator


def validate_json_schema(instance: Any, schema: dict) -> None:
    """
    Проверяет соответствие JSON-объекта (instance) заданной JSON-схеме (schema)
    :param instance: JSON-данные, которые нужно проверить
    :param schema: Ожидаемая JSON-схема
    :return: jsonschema.exceptions.ValidationError: Если instance не соответствует schema
    """
    validate(
        schema=schema,
        instance=instance,
        format_checker=Draft202012Validator.FORMAT_CHECKER
    )
