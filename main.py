from expense import Expense
from expense_db import ExpenseDB
import pandas as pd


db = ExpenseDB() #Initializing the database


expense1 = Expense("Rent", 600000)
expense2 = Expense("Transport", 50000)
expense3 = Expense("Groceries", 180000)
expense4 = Expense("Utilities", 70000)
expense5 = Expense("Transport", 60000)


db.add_expense(expense1)
db.add_expense(expense2)
db.add_expense(expense3)
db.add_expense(expense4)

print("All Expenses:", db.to_dict())

# Convert expenses to DataFrame for easy readability
df = pd.DataFrame(db.to_dict())
print("All Expenses:\n", df)



found_expense = db.get_expense_by_id(expense1.id)
print("ID Found:", found_expense.to_dict() if found_expense else "Not Found")



rent_expenses = db.get_expenses_by_title("Rent")
print("Expenses titled 'Rent':", [exp.to_dict() for exp in rent_expenses])


expense1.update(amount=800000)
print("Expense Updated Successfully:", expense1.to_dict())



db.remove_expense(expense5.id)
print("Expense removed successfully:", db.to_dict())

