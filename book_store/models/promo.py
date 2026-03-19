from sqlalchemy import Column, Integer, String, Float, DateTime
from database import Base


class Promo(Base):
    __tablename__ = "promo"

    id = Column(Integer, primary_key=True, index=True)

    name = Column(String)

    discount = Column(Float)  # 0.10 = 10%

    category = Column(String, nullable=True)

    active_from = Column(DateTime)
    active_to = Column(DateTime)