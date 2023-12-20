# Importing libraries 
import uuid 
from datetime import datetime, timezone

# creating the Expense class
class Expense:
    def __init__(self, title, amount):
        self.id = str(uuid.uuid4())
        self.title = title
        self.amount = amount
        self.created_at = datetime.utcnow()
        self.updated_at = self.created_at
        
        
    def update(self, title = None, amount = None):
        if title is not None:
            self.title = title
        if amount is not None:
            self.amount = amount
        self.updated_at = datetime.utcnow()
            

# Creating a dictionary representation of the Expense Class
    def to_dict(self):
        return {
        "id": self.id,
        "title": self.title,
        "amount": self.amount,
        "created_at": self.created_at.isoformat(),
        "updated_at": self.updated_at.isoformat()
        }
        
        

# Creating Expense Database class        
class ExpenseDatabase:
    def __init__(self):
        self.expenses = []

# Adding an Expense 
def add_expense(self, expense):
    self.expenses.append(expense)
    

# Removing an expense from ExpenseDatabase    
def remove_expense(self, expense_id):
    self.expenses = [expense for expense in self.expenses if expense.id != expense_id]
    
# Getting an expense by ID.    

def get_expense_by_id(self, expense_id):
    for expense in self.expenses:
        if expense.id == expense_id:
            return expense
        return None
    
# Get expenses by title (returning a list).

def get_expenses_by_title(self, title):
    return [expense for expense in self.expenses if expense.title == title]

# Createing a to_dict method that returns a list of dictionaries representing each expense in 
# #the database.

def to_dict(self):
    return [expense.to_dict() for expense in self.expenses]
