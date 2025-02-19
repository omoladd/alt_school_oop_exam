import uuid
from datetime import datetime, timezone

class Expense:
    def __init__(self, title, amount):
        self.id = str(uuid.uuid4())
        self.title = title
        self.amount = amount
        self.created_at = datetime.now(timezone.utc)
        self.updated_at= self.created_at

    def update(self, title: str = None, amount: float = None):
        if title:
            self.title = title
        if amount:
            self.amount = amount
        self.updated_at = datetime.now(timezone.utc)

    
    def to_dict(self):
        return{
            "id": self.id,
            "title": self.title,
            "amount": self.amount,
            "created_at": self.created_at,
            "updated_at": self.updated_at,
        }
    

