"""Модуль, содержащий класс Student с представлением информации о студенте."""

from typing import List


class Student:
    """Класс для представления сведений о студенте."""

    def __init__(
        self,
        full_name: str,
        group: str,
        grades: List[int] | None = None
    ) -> None:
        """Инициализирует объект студента.

        Параметры:
            full_name (str): Фамилия, имя и отчество студента.
            group (str): Академическая группа.
            grades (List[int] | None): Список оценок (по умолчанию пустой).
        """
        if not full_name.strip():
            raise ValueError("ФИО студента не может быть пустой строкой")
        if not group.strip():
            raise ValueError("Группа не может быть пустой строкой")

        self.full_name = full_name.strip()
        self.group = group.strip()
        self.grades: List[int] = list(grades) if grades is not None else []

    def add_grade(self, grade: int) -> None:
        """Добавляет оценку от 2 до 5."""
        if not (2 <= grade <= 5):
            raise ValueError(
                f"Оценка должна быть в диапазоне от 2 до 5, получено: {grade}"
            )
        self.grades.append(grade)

    def average_grade(self) -> float:
        """Вычисляет средний академический балл."""
        if not self.grades:
            return 0.0
        return round(sum(self.grades) / len(self.grades), 2)

    def is_excellent(self) -> bool:
        """Проверяет, является ли студент отличником."""
        return bool(self.grades) and all(grade == 5 for grade in self.grades)

    def get_info(self) -> str:
        """Возвращает форматированную строку с информацией о студенте."""
        avg = self.average_grade()
        status = " (отличник)" if self.is_excellent() else ""
        return (
            f"Студент: {self.full_name} | "
            f"Группа: {self.group} | "
            f"Средний балл: {avg:.2f}{status}"
        )

    def __repr__(self) -> str:
        return f"Student(name={self.full_name!r}, group={self.group!r})"
