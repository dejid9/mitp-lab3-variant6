"""Модуль со статическими вспомогательными методами."""


class MathHelper:
    """Класс математических и валидационных утилит со статическими методами."""

    @staticmethod
    def is_prime(number: int) -> bool:
        """Проверяет, является ли целое число простым.

        Параметры:
            number (int): Проверяемое целое число.

        Возвращает:
            bool: True, если число простое, иначе False.
        """
        if not isinstance(number, int):
            raise TypeError("Ожидалось целое число")
        if number < 2:
            return False
        for i in range(2, int(number ** 0.5) + 1):
            if number % i == 0:
                return False
        return True

    @staticmethod
    def clamp(value: float, min_val: float, max_val: float) -> float:
        """Ограничивает значение заданным диапазоном [min_val, max_val]."""
        if min_val > max_val:
            raise ValueError("min_val не может быть больше max_val")
        return max(min_val, min(value, max_val))

    @staticmethod
    def validate_grade(grade: int) -> bool:
        """Проверяет корректность академической оценки (2-5)."""
        return isinstance(grade, int) and (2 <= grade <= 5)
