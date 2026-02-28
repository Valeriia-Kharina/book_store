from sqlalchemy.orm import Session
from models import PreOrder


def create_preorder(db: Session, preorder: PreOrder):

    db.add(preorder)
    db.commit()
    db.refresh(preorder)

    return preorder


def get_all_preorders(db: Session):

    return db.query(PreOrder).all()

def update(self, preorder_id, book_id, customer_id, quantity):
    self.cursor.execute(
        "UPDATE preorder SET book_id=?, customer_id=?, quantity=? WHERE id=?",
        (book_id, customer_id, quantity, preorder_id)
    )
    self.connection.commit()
    return self.cursor.rowcount


def delete(self, preorder_id):
    self.cursor.execute(
        "DELETE FROM preorderі WHERE id=?",
        (preorder_id,)
    )
    self.connection.commit()
    return self.cursor.rowcount