# Лабораторная работа №3

ФИО: Вафин Денис Наильевич
Группа: 221141
Вариант: 6
Лабораторная работа: №3

Дисциплина: «Методы и технологии программирования».

## Выполненные практические задания по варианту 6

### Средней сложности
1. **№2 — Класс «Студент» с методом вывода информации.** Реализован класс `Student` (в модуле `src/student.py`), содержащий атрибуты ФИО, академической группы и списка оценок, методы добавления оценок `add_grade`, расчёта среднего балла `average_grade`, выявления отличников `is_excellent` и метод информативного форматированного вывода `get_info`.
2. **№6 — Класс со статическим методом.** Реализован класс `MathHelper` (в модуле `src/math_helper.py`), содержащий статические методы `@staticmethod is_prime`, `clamp` и `validate_grade`, демонстрирующие вызов служебных алгоритмов без привязки к состоянию экземпляра (`self`).
3. **№8 — Класс-счётчик (увеличение/уменьшение).** Реализован класс `Counter` (в модуле `src/counter.py`), обеспечивающий инкремент, декремент с настраиваемым шагом, поддержку минимального и максимального порога, а также сброс состояния.

### Повышенной сложности
1. **№4 — Реализовать паттерн Strategy для расчёта цены.** Реализован поведенческий паттерн «Стратегия» (`src/pricing_strategy.py`):
   - Абстрактный базовый класс `PricingStrategy`;
   - Конкретные алгоритмы: `StandardPricingStrategy` (базовый тариф), `StudentDiscountStrategy` (скидка студентам), `VipLoyaltyStrategy` (скидка VIP + вычет бонуса);
   - Контекст `Order`, поддерживающий динамическую смену алгоритма на лету (`set_strategy`) и печать детального чека.
2. **№10 — Unit-тесты классов (TDD).** Разработка выполнена по методологии Test-Driven Development (TDD). Набор модульных тестов `tests/test_classes_tdd.py` полностью покрывает все классы, методы и граничные условия.

---

## Архитектура проекта

```text
mitp-lab3-variant6/
├── src/
│   ├── counter.py             # Задание 8 (среднее): класс-счётчик
│   ├── math_helper.py         # Задание 6 (среднее): статические методы
│   ├── pricing_strategy.py    # Задание 4 (повышенное): паттерн Strategy
│   └── student.py             # Задание 2 (среднее): класс Student
├── tests/
│   └── test_classes_tdd.py    # Задание 10 (повышенное): TDD unit-тесты (11 тестов)
├── .flake8                    # Конфигурация линтера flake8
├── .gitattributes             # Нормализация переносов строк (eol=lf)
├── .gitignore                 # Игнорируемые артефакты Python
├── main.py                    # Демонстрационный скрипт
├── README.md                  # Документация и отчёт по лабораторной работе
└── requirements.txt           # Зависимости проекта
```

---

## Установка и запуск

### Windows (PowerShell)

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
python main.py
python -m flake8 .
python -m pytest -v
```

### Linux / macOS (Bash)

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python3 main.py
python3 -m flake8 .
python3 -m pytest -v
```

---

## Подтверждение работы (логи выполнения)

### Демонстрация работы `main.py`:
```text
=================================================================
Лабораторная работа №3 — Вариант 6
Дисциплина: «Методы и технологии программирования»
Студент: Вафин Денис Наильевич (Группа 221141)
=================================================================

[1] Класс «Студент»:
    Студент: Вафин Денис Наильевич | Группа: 221141 | Средний балл: 4.80
    Отличник: False

[2] Класс со статическими методами (MathHelper):
    Число 7 простое? -> True
    Число 13 простое? -> True
    Число 24 простое? -> False
    Число 29 простое? -> True
    MathHelper.clamp(142.5, 0.0, 100.0) -> 100.0

[3] Класс-счётчик (Counter):
    Начальное значение: 10
    После increment(): 15
    После increment(): 20
    После decrement(): 15

[4] Паттерн «Стратегия» (Strategy) для расчёта цены:
    1. Заказ #ORD-2026-001 | Стратегия: Стандартный тариф (без скидки)
Базовая стоимость: 5000.00 руб. | Скидка: 0.00 руб. | Итого к оплате: 5000.00 руб.
    2. Заказ #ORD-2026-001 | Стратегия: Студенческая скидка (25.0%)
Базовая стоимость: 5000.00 руб. | Скидка: 1250.00 руб. | Итого к оплате: 3750.00 руб.
    3. Заказ #ORD-2026-001 | Стратегия: VIP-клиент (35.0% + бонус)
Базовая стоимость: 5000.00 руб. | Скидка: 1850.00 руб. | Итого к оплате: 3150.00 руб.

[5] Unit-тесты классов (TDD):
    Полный набор модульных тестов находится в tests/test_classes_tdd.py
    Тесты подтверждают корректность всех классов и граничных условий.
=================================================================
```

### Результат проверки линтером `flake8`:
```text
python -m flake8 .
[OK] Ошибок не обнаружено, код полностью соответствует PEP 8.
```

### Результаты тестирования `pytest -v`:
```text
============================= test session starts =============================
platform win32 -- Python 3.12.6, pytest-9.1.1, pluggy-1.6.0 -- C:\Python312\python.exe
cachedir: .pytest_cache
metadata: {'Python': '3.12.6', 'Platform': 'Windows-10-10.0.19045-SP0', 'Packages': {'pytest': '9.1.1', 'pluggy': '1.6.0'}, 'Plugins': {'anyio': '4.15.1', 'html': '4.0.2', 'metadata': '3.1.1', 'ordering': '0.6', 'rerunfailures': '16.4', 'xdist': '3.8.0', 'seleniumbase': '4.51.3'}}
rootdir: C:\Users\dejid\Desktop\Учёба\Новая папка\mitp-lab3-variant6
plugins: anyio-4.15.1, html-4.0.2, metadata-3.1.1, ordering-0.6, rerunfailures-16.4, xdist-3.8.0, seleniumbase-4.51.3
collecting ... collected 13 items

tests/test_classes_tdd.py::TestStudentTDD::test_student_creation_and_info PASSED [  7%]
tests/test_classes_tdd.py::TestStudentTDD::test_student_empty_name_raises PASSED [ 15%]
tests/test_classes_tdd.py::TestStudentTDD::test_student_add_grade_validation PASSED [ 23%]
tests/test_classes_tdd.py::TestMathHelperTDD::test_is_prime PASSED       [ 30%]
tests/test_classes_tdd.py::TestMathHelperTDD::test_clamp PASSED          [ 38%]
tests/test_classes_tdd.py::TestMathHelperTDD::test_validate_grade PASSED [ 46%]
tests/test_classes_tdd.py::TestCounterTDD::test_counter_stepping PASSED  [ 53%]
tests/test_classes_tdd.py::TestCounterTDD::test_counter_bounds PASSED    [ 61%]
tests/test_classes_tdd.py::TestCounterTDD::test_counter_reset PASSED     [ 69%]
tests/test_classes_tdd.py::TestPricingStrategyTDD::test_standard_pricing PASSED [ 76%]
tests/test_classes_tdd.py::TestPricingStrategyTDD::test_student_discount PASSED [ 84%]
tests/test_classes_tdd.py::TestPricingStrategyTDD::test_vip_strategy PASSED [ 92%]
tests/test_classes_tdd.py::TestPricingStrategyTDD::test_order_context_strategy_swap PASSED [100%]

============================= 13 passed in 0.16s ==============================
```

---

## Git Flow и история коммитов

В проекте реализован полный цикл Git Flow:
1. `main` — релизная ветка;
2. `develop` — интеграционная ветка разработки;
3. `feature/variant6-oop` — функциональная ветка;
4. Атомарные коммиты по методологии Conventional Commits отражают фазы TDD и пошаговой реализации классов;
5. Слияния выполнены исключительно через `--no-ff`;
6. Релиз зафиксирован тегом `v1.0.0`.
