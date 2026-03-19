import pytest
from unittest.mock import MagicMock
from services.pricing_logic import calculate_final_price


# Макет клієнта
class MockCustomer:
    def __init__(self, tier):
        self.loyalty_tier = tier


def test_gold_loyalty_discount():
    """Перевірка знижки 10% для Gold клієнта"""
    # 1. Створюємо заглушку для бази даних
    db_mock = MagicMock()

    # 2. Налаштовуємо заглушку так, щоб вона повертала порожній список промо-акцій
    # Це імітує ситуацію, коли в базі немає активних часових промо
    db_mock.query.return_value.filter.return_value.all.return_value = []

    customer = MockCustomer("Gold")

    # 3. Передаємо заглушку замість None
    result = calculate_final_price(db_mock, customer, 1000, [])

    assert result["final_price"] == 900.0
    assert "Loyalty (Gold)" in result["applied_promos"]


def test_no_discount_for_new_customer():
    """Перевірка відсутності знижок для нових клієнтів"""
    db_mock = MagicMock()
    db_mock.query.return_value.filter.return_value.all.return_value = []

    customer = MockCustomer("New")
    result = calculate_final_price(db_mock, customer, 1000, [])

    assert result["final_price"] == 1000.0
    assert len(result["applied_promos"]) == 0