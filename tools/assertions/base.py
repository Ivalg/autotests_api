from typing import Any


def assert_status_code(actual: int, expected: int):
    """
    Проверка, что фактический статус-код соответствует ожидаемому

    :param actual: Фактический статус-код
    :param expected: Ожидаемый статус-код
    :return AssertionError: Если статус-коды не совпадают - ошибка
    """
    assert actual == expected, (
        f"Incorrect response status code. "
        f"Expected status code: {expected}. "
        f"Actual status code: {actual}"
    )


def assert_equal(actual: Any, expected: Any, name: str):
    """
    Проверяет, что фактическое значение равно ожидаемому

    :param actual: Фактическое значение
    :param expected: Ожидаемое значение
    :param name: Название проверяемого значения
    :return: AssertionError - если фактическое значение не равно ожидаемому
    """
    assert actual == expected, (
        f'Incorrect value: "{name}". '
        f'Expected value: {expected}. '
        f'Actual value: {actual}'
    )


def assert_is_true(actual: Any, name: str):
    """
    Проверяет, что фактическое значение является истинным

    :param actual: Фактическое значение
    :param name: Имя проверяемого значения
    :return: AssertionError - если фактическое значение ложно
    """
    assert actual, (
        f'Incorrect value: {name}. '
        f'Expected true value but got: {actual}'
    )
