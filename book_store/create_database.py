from database import engine, Base
import models  # ОБОВ'ЯЗКОВО

Base.metadata.create_all(bind=engine)

print("Таблиці створені або вже існують!")