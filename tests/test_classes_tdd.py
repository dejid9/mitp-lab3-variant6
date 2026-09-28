"""TDD модульные тесты для классов лабораторной работы №3."""

import pytest
from src.student import Student
from src.math_helper import MathHelper
from src.counter import Counter
from src.pricing_strategy import (
    StandardPricingStrategy,
    StudentDiscountStrategy,
    VipLoyaltyStrategy,
    Order,
)


class TestStudentTDD:
    def test_student_creation_and_info(self):
        st = Student("Вафин Денис Наильевич", "221141", [5, 5, 5])
        assert st.full_name == "Вафин Денис Наильевич"
        assert st.group == "221141"
        assert st.average_grade() == 5.0
        assert st.is_excellent() is True
        assert "221141" in st.get_info()

    def test_student_empty_name_raises(self):
        with pytest.raises(ValueError):
            Student("   ", "221141")

    def test_student_add_grade_validation(self):
        st = Student("Иван Иванов", "221141")
        st.add_grade(4)
        st.add_grade(5)
        assert st.average_grade() == 4.5
        with pytest.raises(ValueError):
            st.add_grade(6)


class TestMathHelperTDD:
    def test_is_prime(self):
        assert MathHelper.is_prime(2) is True
        assert MathHelper.is_prime(17) is True
        assert MathHelper.is_prime(4) is False
        assert MathHelper.is_prime(1) is False
        assert MathHelper.is_prime(-7) is False

    def test_clamp(self):
        assert MathHelper.clamp(5.0, 0.0, 10.0) == 5.0
        assert MathHelper.clamp(-5.0, 0.0, 10.0) == 0.0
        assert MathHelper.clamp(15.0, 0.0, 10.0) == 10.0

    def test_validate_grade(self):
        assert MathHelper.validate_grade(5) is True
        assert MathHelper.validate_grade(1) is False


class TestCounterTDD:
    def test_counter_stepping(self):
        c = Counter(initial=0, step=3)
        assert c.value == 0
        assert c.increment() == 3
        assert c.increment() == 6
        assert c.decrement() == 3

    def test_counter_bounds(self):
        c = Counter(initial=5, step=10, min_val=0, max_val=10)
        assert c.increment() == 10
        assert c.decrement() == 0

    def test_counter_reset(self):
        c = Counter(initial=10, step=2)
        c.reset(42)
        assert c.value == 42


class TestPricingStrategyTDD:
    def test_standard_pricing(self):
        strategy = StandardPricingStrategy()
        assert strategy.calculate_price(1000.0) == 1000.0

    def test_student_discount(self):
        strategy = StudentDiscountStrategy(discount_percent=20.0)
        assert strategy.calculate_price(1000.0) == 800.0

    def test_vip_strategy(self):
        strategy = VipLoyaltyStrategy(discount_percent=30.0, cash_bonus=50.0)
        # 1000 * 0.7 = 700 - 50 = 650
        assert strategy.calculate_price(1000.0) == 650.0

    def test_order_context_strategy_swap(self):
        items = [{"title": "Товар", "price": 500.0, "quantity": 2}]
        order = Order("ORD-1", items, StandardPricingStrategy())
        assert order.get_base_total() == 1000.0
        assert order.get_final_total() == 1000.0

        order.set_strategy(StudentDiscountStrategy(20.0))
        assert order.get_final_total() == 800.0
        assert "800.00" in order.get_receipt()
