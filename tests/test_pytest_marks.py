import pytest
import sys


@pytest.mark.skip(reason="Функционал в разработке")
def test_feature_in_development():
    pass


# ------------------------------------- mark.skipif(условие, причина) --------------------------------------------------

@pytest.mark.skipif(sys.version_info < 3.8, reason="Требуется версия 3.8 или выше")
def test_python_version():
    pass


SYSTEM_VERSION = "v1.2.0"  # Для примера укажем версию тестируемой системы


@pytest.mark.skipif(
    SYSTEM_VERSION == "v1.3.0",  # Пропустим авто-тест, если версия системы равна v1.3.0
    reason="Тест не может быть запущен на версии системы v1.3.0"
)
def test_system_version_valid():  # В текущей конфигурации этот тест запустится
    pass


@pytest.mark.skipif(
    SYSTEM_VERSION == "v1.2.0",  # Пропустим автотест, если версия системы равна v1.2.0
    reason="Тест не может быть запущен на версии системы v1.2.0"
)
def test_system_version_invalid():  # Этот авто-тест не запустится
    pass


# --------------------------------- mark.xfail() -----------------------------------------------

@pytest.mark.xfail(reason="Известная ошибка, исправление в следующем релизе")
def test_known_issue():
    pass


@pytest.mark.xfail(reason='Найден баг в приложении, из-за которого тест падает с ошибкой')
def test_with_bug():
    assert 1 == 2


@pytest.mark.xfail(reason='Баг уже исправлен, но на тест все еще висит маркировка xfail')
def test_without_bug():
    pass


@pytest.mark.xfail(reason='Внешний сервис временно недоступен')
def test_external_services_is_unavailable():
    assert 1 == 2
