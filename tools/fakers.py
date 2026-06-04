from faker import Faker


class Fake:
    """Класс для генерации случайных текстовых данных с использованием библиотеки Faker"""

    def __init__(self, faker: Faker):
        """
        :param faker: Экземпляр класса Faker, который будет использоваться для генерации данных
        """
        self.faker = faker

    def text(self) -> str:
        """Генерирует случайный текст"""
        return self.faker.text()

    def uuid4(self) -> str:
        """Генерирует случайный UUID4"""
        return self.faker.uuid4()

    def email(self) -> str:
        """Генерирует случайный email"""
        return self.faker.email()

    def sentence(self) -> str:
        """Генерирует случайное предложение"""
        return self.faker.sentence()

    def password(self) -> str:
        """Генерирует случайный пароль"""
        return self.faker.password()

    def last_name(self) -> str:
        """Генерирует случайную фамилию"""
        return self.faker.last_name()

    def first_name(self) -> str:
        """Генерирует случайное имя"""
        return self.faker.first_name()

    def middle_name(self) -> str:
        """Генерирует случайное отчество для RU локали, и first_name если нет"""
        try:
            return self.faker.middle_name()
        except AttributeError:
            return self.faker.first_name()

    def integer(self, start: int = 1, end: int = 100) -> int:
        """Генерирует случайное целое число в заданном диапазоне"""
        return self.faker.random_int(start, end)

    def estimated_time(self) -> str:
        """Генерирует строку с предполагаемым временем (2 weeks)"""
        return f"{self.integer(1, 10)} weeks"

    def max_score(self) -> int:
        """Генерирует случайный максимальный балл в диапазоне 50 - 100"""
        return self.integer(50, 100)

    def min_score(self) -> int:
        """Генерирует случайный минимальный балл в диапазоне 1 - 30"""
        return self.integer(1, 30)


# Создаем экземпляр класса Fake с использованием Faker
fake = Fake(faker=Faker())
