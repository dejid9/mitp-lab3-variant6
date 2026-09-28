"""Модуль, реализующий класс-счётчик."""


class Counter:
    """Класс-счётчик с поддержкой инкремента, декремента и шага."""

    def __init__(
        self,
        initial: int = 0,
        step: int = 1,
        min_val: int | None = None,
        max_val: int | None = None
    ) -> None:
        """Инициализирует счётчик.

        Параметры:
            initial (int): Начальное значение.
            step (int): Шаг изменения (по умолчанию 1).
            min_val (int | None): Нижний порог значения.
            max_val (int | None): Верхний порог значения.
        """
        if step <= 0:
            raise ValueError("Шаг счётчика должен быть положительным числом")
        if min_val is not None and max_val is not None and min_val > max_val:
            raise ValueError("min_val не может превышать max_val")

        self._min_val = min_val
        self._max_val = max_val
        self._step = step
        self._value = initial

        self._apply_bounds()

    def _apply_bounds(self) -> None:
        if self._min_val is not None and self._value < self._min_val:
            self._value = self._min_val
        if self._max_val is not None and self._value > self._max_val:
            self._value = self._max_val

    @property
    def value(self) -> int:
        """Текущее значение счётчика."""
        return self._value

    @property
    def step(self) -> int:
        """Шаг изменения счётчика."""
        return self._step

    def increment(self) -> int:
        """Увеличивает счётчик на шаг."""
        new_val = self._value + self._step
        if self._max_val is not None and new_val > self._max_val:
            self._value = self._max_val
        else:
            self._value = new_val
        return self._value

    def decrement(self) -> int:
        """Уменьшает счётчик на шаг."""
        new_val = self._value - self._step
        if self._min_val is not None and new_val < self._min_val:
            self._value = self._min_val
        else:
            self._value = new_val
        return self._value

    def reset(self, new_value: int = 0) -> int:
        """Сбрасывает значение счётчика."""
        self._value = new_value
        self._apply_bounds()
        return self._value

    def __repr__(self) -> str:
        return f"Counter(value={self._value}, step={self._step})"

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Counter):
            return NotImplemented
        return self._value == other._value
