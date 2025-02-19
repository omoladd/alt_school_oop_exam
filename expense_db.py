class ExpenseDB:
    def __init__(self):
        self.expenses=[]  

    
    def add_expense(self, expense):
        self.expenses.append(expense)

    
    def remove_expense(self, expense_id):
        self.expenses = [exp for exp in self.expenses if exp.id != expense_id]

    
    def get_expense_by_id(self, expense_id):
        for expense in self.expenses:
            if expense.id == expense_id:
                return expense
        return None
    
  
    def get_expenses_by_title(self, title):
        return[exp for exp in self.expenses if exp.title.lower() == title.lower()]
     
    
    def to_dict(self):
        return[expense.to_dict() for expense in self.expenses]



