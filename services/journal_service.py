from models.journal import Journal
from repositories.journal_repository import JournalRepository

class JournalService:

    def __init__(self, db):
        self.repository = JournalRepository(db)

    def create_journal(self, data):
        if data.price <= 0:
            raise ValueError("Ціна повинна бути додатня")

        journal = Journal(**data.model_dump())
        return self.repository.create(journal)

    def get_all(self):
        return self.repository.get_all()

    def delete(self, journal_id):
        journal = self.repository.get_by_id(journal_id)
        if not journal:
            raise ValueError("Журнал не знайдено ")
        self.repository.delete(journal)

    def update(self, journal_id, data):

        journal = self.repository.get_by_id(journal_id)

        if not journal:
            raise ValueError("Журнал не знайдено")

        if data.price <= 0:
            raise ValueError("Ціна повинна бути додатня")

        for key, value in data.model_dump().items():
            setattr(journal, key, value)

        return self.repository.update(journal)