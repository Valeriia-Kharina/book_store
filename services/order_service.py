from sqlalchemy.orm import Session
from models import Book, Order, Customer, OrderItem, PreOrder
from repositories import order_repository
from .pricing_logic import calculate_final_price


def create_order(db: Session, data):
    try:
        customer = db.query(Customer).filter(Customer.id == data.customer_id).first()
        if not customer:
            raise ValueError("Клієнт не знайдений")

        total_price = 0
        order_items = []

        for item in data.items:
            book = db.query(Book).filter(Book.id == item.book_id).with_for_update().first()
            if not book:
                raise ValueError(f"Книга з ID {item.book_id} не знайдена")

            # МЕХАНІЗМ РЕЗЕРВУ: перевіряємо вільний залишок (stock - reserved_stock)
            available = book.stock - book.reserved_stock
            if available < item.quantity:
                raise ValueError(f"Недостатньо вільного товару '{book.title}' (доступно: {available})")

            # СТАВИМО В РЕЗЕРВ (HOLD)
            book.reserved_stock += item.quantity

            # Створюємо запис про резервування (передзамовлення)
            reservation = PreOrder(
                customer_id=data.customer_id,
                book_id=book.id,
                quantity=item.quantity,  # Переконайтеся, що в PreOrder є це поле, або додайте його в модель
                status="очікується"
            )
            db.add(reservation)

            item_price = book.price * item.quantity
            order_items.append(OrderItem(
                book_id=book.id,
                quantity=item.quantity,
                price=item_price
            ))
            total_price += item_price

        result = calculate_final_price(db, customer, total_price, data.items)

        order = Order(
            customer_id=data.customer_id,
            total_price=result["final_price"],
            status="Pending",
            applied_promos=", ".join(result["applied_promos"]),
            items=order_items
        )

        new_order = order_repository.create_order(db, order)
        db.commit()
        db.refresh(new_order)
        return new_order

    except Exception as e:
        db.rollback()
        raise e


# МЕХАНІЗМ ЗВІЛЬНЕННЯ РЕЗЕРВУ
def update_order_status(db: Session, order_id: int, new_status: str):
    order = order_repository.get_order(db, order_id)
    if not order:
        return None

    # Заборона на дивні переходи статусу
    if order.status in ["Cancelled", "Shipped"] and new_status == "Pending":
        raise ValueError("Неможливо повернути завершене замовлення в обробку")

    # ЛОГІКА ЗВІЛЬНЕННЯ / СПИСАННЯ
    for item in order.items:
        book = db.query(Book).filter(Book.id == item.book_id).with_for_update().first()

        # 1. СКАСУВАННЯ: Знімаємо тільки резерв
        if new_status == "Cancelled" and order.status == "Pending":
            book.reserved_stock -= item.quantity
            # Оновлюємо пов'язаний преордер
            pre = db.query(PreOrder).filter(PreOrder.book_id == book.id,
                                            PreOrder.customer_id == order.customer_id).first()
            if pre: pre.status = "скасовано"

        # 2. ВІДПРАВКА: Списуємо фізично
        elif new_status == "Shipped" and order.status == "Pending":
            book.stock -= item.quantity
            book.reserved_stock -= item.quantity
            pre = db.query(PreOrder).filter(PreOrder.book_id == book.id,
                                            PreOrder.customer_id == order.customer_id).first()
            if pre: pre.status = "доставлено"

    order.status = new_status
    db.commit()
    db.refresh(order)
    return order

def get_orders(db: Session):
    """Отримати список усіх замовлень"""
    return order_repository.get_all_orders(db)


def get_order(db: Session, order_id: int):
    """Отримати конкретне замовлення за ID"""
    return order_repository.get_order(db, order_id)


def update_order(db: Session, order_id: int, data):
    """Оновити статус або дані замовлення"""
    # Тут можна додати бізнес-логіку перевірки статусів (ORDER_STATUS) перед оновленням
    updated_order = order_repository.update_order(db, order_id, data)
    return updated_order


def delete_order(db: Session, order_id: int):
    """Видалити замовлення"""
    return order_repository.delete_order(db, order_id)