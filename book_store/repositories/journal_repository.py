from models.journal import Journal

class JournalRepository:

    def __init__(self, db):
        self.db = db

    def create(self, journal):
        self.db.add(journal)
        self.db.commit()
        self.db.refresh(journal)
        return journal

    def get_all(self):
        return self.db.query(Journal).all()

    def get_by_id(self, journal_id):
        return self.db.query(Journal).filter(Journal.id == journal_id).first()

    def delete(self, journal):
        self.db.delete(journal)
        self.db.commit()