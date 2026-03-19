from repositories.promo_repository import get_active_promos


def calculate_final_price(db, customer, base_total, items):
    """
    Основна функція розрахунку ціни.
    Повертає фінальну ціну + інформацію про застосовані знижки.
    """

    price = base_total
    applied_promos = []

    # 1. Tier-based знижки (Loyalty)
    loyalty_discounts = {
        "Gold": 0.10,   # 10%
        "Silver": 0.05, # 5%
        "Bronze": 0.01  # 1%
    }

    tier_discount = loyalty_discounts.get(customer.loyalty_tier, 0)

    if tier_discount > 0:
        price *= (1 - tier_discount)
        applied_promos.append(f"Loyalty ({customer.loyalty_tier})")

    # 2. Bulk знижки (оптові)
    total_quantity = sum(item.quantity for item in items)

    if total_quantity >= 5:
        price *= 0.95
        applied_promos.append("Bulk discount (5% за кількість)")

    if base_total > 1000:
        price -= 100
        applied_promos.append("Fixed discount (-100 за суму > 1000)")

    # 3. Промо-акції
    price, promo_names = apply_promos(db, items, price)

    applied_promos.extend(promo_names)

    return {
        "final_price": max(round(price, 2), 0),
        "applied_promos": applied_promos
    }


def apply_promos(db, items, price):
    from models import Book # Уникаємо циклічного імпорту
    promos = get_active_promos(db)
    applied = []

    for promo in promos:
        if promo.category:
            # Перевіряємо, чи є в замовленні книги потрібної категорії
            for item in items:
                book = db.query(Book).filter(Book.id == item.book_id).first()
                if book and book.category == promo.category:
                    price *= (1 - promo.discount)
                    applied.append(f"{promo.name} (Категорія: {promo.category})")
                    break # Знижка за категорію нараховується один раз
        else:
            # Часова акція на все замовлення
            price *= (1 - promo.discount)
            applied.append(promo.name)

    return price, applied