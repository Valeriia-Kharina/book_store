import pytest
from services import order_service
from unittest.mock import MagicMock


def test_forbidden_status_transition():
    """Перевірка заборони переходу з Shipped назад у Pending"""
    db = MagicMock()
    # Імітуємо замовлення, яке вже відправлене
    mock_order = MagicMock()
    mock_order.status = "Shipped"

    # Підміняємо репозиторій, щоб він повернув наше "відправлене" замовлення
    order_service.order_repository.get_order = MagicMock(return_value=mock_order)

    # Очікуємо, що код видасть помилку ValueError
    with pytest.raises(ValueError) as excinfo:
        order_service.update_order_status(db, 1, "Pending")

    assert "Неможливо повернути" in str(excinfo.value)


def test_allowed_status_transition():
    """Перевірка дозволеного скасування замовлення"""
    db = MagicMock()
    mock_order = MagicMock()
    mock_order.status = "Pending"
    mock_order.items = []  # Порожні товари для простоти

    order_service.order_repository.get_order = MagicMock(return_value=mock_order)

    # Має спрацювати без помилок
    result = order_service.update_order_status(db, 1, "Cancelled")
    assert result is not None