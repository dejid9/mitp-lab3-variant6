"""Главный модуль демонстрации объектно-ориентированных решений (Лабораторная №3)."""

from src.student import Student
from src.math_helper import MathHelper
from src.counter import Counter
from src.pricing_strategy import (
    StandardPricingStrategy,
    StudentDiscountStrategy,
    VipLoyaltyStrategy,
    Order,
)


def main() -> None:
    print("=" * 65)
    print("Лабораторная работа №3 — Вариант 6")
    print("Дисциплина: «Методы и технологии программирования»")
    print("Студент: Вафин Денис Наильевич (Группа 221141)")
    print("=" * 65)

    # 1. Задание 2 (среднее): Класс Student
    student = Student("Вафин Денис Наильевич", "221141", [5, 5, 4, 5, 5])
    print("\n[1] Класс «Студент»:")
    print("   ", student.get_info())
    print("    Отличник:", student.is_excellent())

    # 2. Задание 6 (среднее): Класс со статическим методом MathHelper
    print("\n[2] Класс со статическими методами (MathHelper):")
    samples = [7, 13, 24, 29]
    for num in samples:
        print(f"    Число {num} простое? -> {MathHelper.is_prime(num)}")
    clamped = MathHelper.clamp(142.5, 0.0, 100.0)
    print(f"    MathHelper.clamp(142.5, 0.0, 100.0) -> {clamped}")

    # 3. Задание 8 (среднее): Класс-счётчик Counter
    counter = Counter(initial=10, step=5, min_val=0, max_val=30)
    print("\n[3] Класс-счётчик (Counter):")
    print("    Начальное значение:", counter.value)
    print("    После increment():", counter.increment())
    print("    После increment():", counter.increment())
    print("    После decrement():", counter.decrement())

    # 4. Задание 4 (повышенное): Паттерн Strategy для расчёта цены
    items = [
        {"title": "Учебник по Python", "price": 1200.0, "quantity": 1},
        {"title": "Курс «Методы программирования»", "price": 3800.0, "quantity": 1},
    ]
    order = Order("ORD-2026-001", items, StandardPricingStrategy())
    print("\n[4] Паттерн «Стратегия» (Strategy) для расчёта цены:")
    print("    1.", order.get_receipt())

    order.set_strategy(StudentDiscountStrategy(discount_percent=25.0))
    print("    2.", order.get_receipt())

    order.set_strategy(VipLoyaltyStrategy(discount_percent=35.0, cash_bonus=100.0))
    print("    3.", order.get_receipt())

    # 5. Задание 10 (повышенное): Unit-тесты классов (TDD)
    print("\n[5] Unit-тесты классов (TDD):")
    print("    Полный набор модульных тестов находится в tests/test_classes_tdd.py")
    print("    Тесты подтверждают корректность всех классов и граничных условий.")
    print("=" * 65)


if __name__ == "__main__":
    main()
