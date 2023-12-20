# Expense Tracker: Object-Oriented Programming in Python
 
## Project Description
 
This project serves as an exercise in applying object-oriented programming (OOP) concepts in Python, specifically focusing on modeling and managing financial expenses. By implementing two classes, Expense and ExpenseDatabase, the goal of this project is to gain practical experience with defining classes, utilizing attributes and methods, and handling time-related functionalities.

### **Key Features:**
* Tracks expenses with title, amount, and timestamps.
* Generates unique IDs for each expense.
* Allow adding, updating, removing, and retrieving expenses.
* Stores expenses in a list within an ExpenseDatabase class.
* Provides methods for searching expenses by ID and title.
* Represents expenses as dictionaries for easy serialization and exchange.

### **Classes:**

## ```Expense Class:``` Represents an individual expense with five attributes.

**id:** Unique identifier generated as a UUID string.

**title:** String representing the expense title.

**amount:** Float represents the expense amount.

**created_at:** Timestamp indicating the expense creation date and time (UTC).

**updated_at:** Timestamp indicating the last time the expense was updated (UTC).
 
## ```ExpenseDatabase Class:```  Manages a collection of Expense objects with six methods:

**__init__:** Initializes the empty expenses list.

**add_expense:** Adds a new Expense object to the expenses list.

**remove_expense:** Removes an Expense object from the expenses list based on its unique ID.

**get_expense_by_id:** Retrieves an Expense object from the expenses list based on its unique ID.

**get_expenses_by_title:** Retrieves a list of Expense objects from the expenses list that match a given title.

**to_dict:** Returns a list of dictionaries representing each Expense object in the database.

## Implementation of each method and function within the classes

## Expense Class:

**init(title, amount):**
* Initializes the object with the provided title and amount.
* Generates a unique identifier (id) using uuid.uuid4() and converts it to a string.
* Sets both created_at and updated_at timestamps to the current UTC time with datetime.utcnow().

**Unique IDs:**
* The __init__ method of the Expense class uses uuid.uuid4() to generate unique identifiers for each expense.
* This ensures there are no duplicate IDs, even if multiple expenses are created simultaneously.
  
**Timestamps:**
* Both created_at and updated_at in the Expense class utilize datetime.utcnow() to capture timestamps accurately.
* This allows you to track the exact time each expense was created and last updated.
* The update method updates the updated_at timestamp whenever any attribute is modified to reflect the latest change.



```python
# Importing libraries 
import uuid 
from datetime import datetime, timezone

# Creating the Expense class, which represents an individual financial expense.
class Expense:
    def __init__(self, title, amount):
        self.id = str(uuid.uuid4())
        self.title = title
        self.amount = amount
        self.created_at = datetime.utcnow()
        self.updated_at = self.created_at     
```

**update(title=None, amount=None):**
* Allows updating the title and/or amount of the Expense.
* Uses optional arguments for title and amount.
* Sets the updated attribute(s) only if a new value is provided.
* Updates the updated_at timestamp to the current UTC time whenever any attribute is modified.



```python
# Updates the title and/or amount of the expense.     
     def update(self, title = None, amount = None):
        if title is not None:
            self.title = title
        if amount is not None:
            self.amount = amount
        self.updated_at = datetime.utcnow()            
```


**to_dict():**
* Creates a dictionary representation of the Expense object.
* Includes all attributes (id, title, amount, created_at, and updated_at).
* Converts the timestamps (created_at and updated_at) to ISO format using isoformat() for easier reading and 
  compatibility.

```python
# Creating a dictionary representation of the Expense Class
   def to_dict(self):
        return {
        "id": self.id,
        "title": self.title,
        "amount": self.amount,
        "created_at": self.created_at.isoformat(),
        "updated_at": self.updated_at.isoformat()
        }
```

## ExpenseDatabase Class:   

**init():**
* Initializes the object with an empty list (expenses) to store Expense objects.
  
```python
# Creating an Expense Database class for managing a collection of Expense objects.       
class ExpenseDatabase:
    def __init__(self):
        self.expenses = []
```
**Add_expense(expense):**
* Adds a new Expense object to the expenses list.
* Takes the provided expense object as an argument.

```python
# Adding a new expense to the ExpenseDatabase.
    def add_expense(self, expense):
        self.expenses.append(expense)
```
  
**Remove_expense(expense_id):**
* Filters the expenses list, keeping only objects with IDs different from the provided expense_id.
* Effectively removes the Expense object with the matching ID from the database.

```python
# Removing an expense from ExpenseDatabase by unique ID    
    def remove_expense(self, expense_id):
        self.expenses = [expense for expense in self.expenses if expense.id != expense_id]
```

**get_expense_by_id(expense_id):**
* Iterates through the expenses list.Checks if any object's id matches the provided expense_id. If a match is found, returns the Expense object.
* If no match is found, returns None.

```python
# Retriving an expense by its unique ID.   
    def get_expense_by_id(self, expense_id):
        for expense in self.expenses:
            if expense.id == expense_id:
                return expense
        return None
```
  
**get_expenses_by_title(title):**
* Uses list comprehension to filter the expenses list.
* Keeps only objects where the title attribute matches the provided title argument.
* Returns a list of Expense objects with the matching title.

```python
# Retriving Expenses by title (returning a list).
    def get_expenses_by_title(self, title):
        return [expense for expense in self.expenses if expense.title == title]
```

**to_dict():**
* Uses list comprehension to apply the to_dict() method to each Expense object in the expenses list.
* Returns a list of dictionaries representing all Expense objects in the database.

```python
# Creating a to_dict method that returns a list of dictionaries representing each expense in 
# the database
    def to_dict(self):
        return [expense.to_dict() for expense in self.expenses]
```

# Cloning the Repository:
 
**The project GitHub URL:** https://github.com/cokoye55/OOP-concepts-in-Python.
1. Open a terminal or command prompt. This can be the Command Prompt on Windows, Terminal on macOS/Linux, or any Git bash terminal.
2. Use the git clone command followed by the URL. For example, if the project URL is https://github.com/cokoye55/OOP-concepts-in-Python, you would type:
3. git clone https://github.com/cokoye55/OOP-concepts-in-Python
4. Press Enter. This will download the project files to your local computer, creating a folder named OOP-concepts-in-Python.
   
# Running the Code:
* Navigate to the project directory. In your terminal, type cd OOP-concepts-in-Python.
* Install any dependencies (optional). If your code uses any additional libraries not included in the standard Python installation, you need to install them. For 
  example, the provided code utilizes the uuid library, so you can install it by running:
**pip install uuid**
**Run the code. Depending on your project structure, you can:**
* Run the main script: If your project includes a main script that executes all functionalities, simply type its name and press Enter. Look for instructions within the 
  script or code comments for details.
* Run individual methods/functions: Use your Python IDE or chosen environment to access specific methods or functions within the classes. You can test their 
  functionalities and explore how they work by providing different arguments or inputs.

**Additional Notes:**
 
* Remember to adjust the commands and instructions based on your specific project setup and chosen development environment.
* If you encounter any errors during cloning or running the code, consult the error messages and search online for possible solutions. You can also consider asking for 
  help in online communities or forums dedicated to Python and its libraries.


 
