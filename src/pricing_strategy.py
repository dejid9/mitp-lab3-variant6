"""Модуль реализации паттерна «Стратегия» (Strategy) для расчёта цены."""

from abc import ABC, abstractmethod
from typing import List, Dict, Any


class PricingStrategy(ABC):
    """Абстрактный базовый класс стратегии ценообразования."""

    @abstractmethod
    def calculate_price(self, base_price: float) -> float:
        """Рассчитывает итоговую цену на основе базовой."""
        pass

    @property
    @abstractmethod
    def name(self) -> str:
        """Наименование стратегии."""
        pass


class StandardPricingStrategy(PricingStrategy):
    """Стандартная цена без скидок."""

    @property
    def name(self) -> str:
        return "Стандартный тариф (без скидки)"

    def calculate_price(self, base_price: float) -> float:
        return round(float(base_price), 2)


class StudentDiscountStrategy(PricingStrategy):
    """Студенческая скидка (по умолчанию 20%)."""

    def __init__(self, discount_percent: float = 20.0) -> None:
        if not (0.0 <= discount_percent <= 100.0):
            raise ValueError("Процент скидки должен быть от 0 до 100")
        self._discount_percent = discount_percent

    @property
    def name(self) -> str:
        return f"Студенческая скидка ({self._discount_percent}%)"

    def calculate_price(self, base_price: float) -> float:
        factor = 1.0 - (self._discount_percent / 100.0)
        return round(base_price * factor, 2)


class VipLoyaltyStrategy(PricingStrategy):
    """VIP скидка с фиксированным бонусом кэшбэка/вычета."""

    def __init__(
        self,
        discount_percent: float = 30.0,
        cash_bonus: float = 50.0
    ) -> None:
        self._discount_percent = discount_percent
        self._cash_bonus = cash_bonus

    @property
    def name(self) -> str:
        return f"VIP-клиент ({self._discount_percent}% + бонус)"

    def calculate_price(self, base_price: float) -> float:
        discounted = base_price * (1.0 - (self._discount_percent / 100.0))
        final_price = max(0.0, discounted - self._cash_bonus)
        return round(final_price, 2)


class Order:
    """Контекст заказа, использующий стратегию ценообразования."""

    def __init__(
        self,
        order_id: str,
        items: List[Dict[str, Any]],
        strategy: PricingStrategy
    ) -> None:
        self.order_id = order_id
        self.items = items
        self.strategy = strategy

    def set_strategy(self, strategy: PricingStrategy) -> None:
        """Динамически переключает стратегию расчёта цены."""
        self.strategy = strategy

    def get_base_total(self) -> float:
        """Считает суммарную базовую стоимость позиций."""
        return sum(item["price"] * item.get("quantity", 1) for item in self.items)

    def get_final_total(self) -> float:
        """Считает итоговую стоимость с учётом активной стратегии."""
        base = self.get_base_total()
        return self.strategy.calculate_price(base)

    def get_receipt(self) -> str:
        """Формирует текстовый чек заказа."""
        base = self.get_base_total()
        final = self.get_final_total()
        discount = round(base - final, 2)
        return (
            f"Заказ #{self.order_id} | Стратегия: {self.strategy.name}\n"
            f"Базовая стоимость: {base:.2f} руб. | "
            f"Скидка: {discount:.2f} руб. | "
            f"Итого к оплате: {final:.2f} руб."
        )
