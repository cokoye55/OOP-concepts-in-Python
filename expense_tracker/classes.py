# Importing libraries 
import uuid 
from datetime import datetime, timezone

# Creating the Expense class which represents an individual financial expense.
class Expense:
    def __init__(self, title, amount):
        self.id = str(uuid.uuid4())
        self.title = title
        self.amount = amount
        self.created_at = datetime.utcnow()
        self.updated_at = self.created_at
        
# Updates the title and/or amount of the expense.       
    def update(self, title = None, amount = None):
        if title is not None:
            self.title = title
        if amount is not None:
            self.amount = amount
        self.updated_at = datetime.utcnow()
            
# Creating a dictionary representation of the Expense Class.
    def to_dict(self):
        return {
        "id": self.id,
        "title": self.title,
        "amount": self.amount,
        "created_at": self.created_at.isoformat(),
        "updated_at": self.updated_at.isoformat()
        }
        
# Creating an Expense Database class for managing a collection of Expense objects.       
class ExpenseDatabase:
    def __init__(self):
        self.expenses = []

# Adding a new expense to the ExpenseDatabase. 
    def add_expense(self, expense):
        self.expenses.append(expense)
    
# Removing an expense from ExpenseDatabase by a unique ID     
    def remove_expense(self, expense_id):
        self.expenses = [expense for expense in self.expenses if expense.id != expense_id]
    
# Retriving an expense by its unique ID.    
    def get_expense_by_id(self, expense_id):
        for expense in self.expenses:
            if expense.id == expense_id:
                return expense
        return None
    
# Retriving Expenses by title (returning a list).
    def get_expenses_by_title(self, title):
        return [expense for expense in self.expenses if expense.title == title]

# Creating a to_dict method that returns a list of dictionaries representing each expense in 
# the database
    def to_dict(self):
        return [expense.to_dict() for expense in self.expenses]
