# Project Description

This expense tracker uses object-oriented programming (OOP) concepts in Python. It  implements two classes, Expense and ExpenseDatabase, to manage financial expenses.

# Key Features

## Expense Class

This represents an individual financial expense.

### Attributes of class Expense:

1. id: A unique identifier generated as a UUID string.
2. title: A string representing the title of the expense.
3. amount: A float representing the amount of the expense.
4. created_at: A timestamp indicating when the expense was created (UTC).
5. updated_at: A timestamp indicating the last time the expense was updated (UTC).

### Methods:

1. **init**: Initializes the attributes.
2. update: Allows updating the title and/or amount, updating the updated_at timestamp.
3. to_dict: Returns a dictionary representation of the expense.

## ExpenseDB class

Manages a collection of Expense objects.

### Attributes:

1. expenses: A list storing Expense instances.

### Methods:

1. **init**: Initializes the list.
2. add_expense: Adds an expense.
3. remove_expense: Removes an expense.
4. get_expense_by_id: Retrieves an expense by ID.
5. get_expense_by_title: Retrieves expenses by title.
6. to_dict: Returns a list of dictionaries representing expenses.

# Cloning Instructions

1. Copy the repository page and copy the HTTPS URL [https://github.com/omoladd/alt_school_oop_exam.git](https://github.com/omoladd/alt_school_oop_exam.git) 
2. Open your terminal or command prompt
3. Navigate to your desired directory using cd your/folder/path
4. Proceed to clone the repository in the path using `git clone [repo URL]`
5. Change the directory into the cloned repository using `cd` repo_name

# How to Run the Code

1. Navigate to the project directory
2. Run the [main.py](http://main.py/) script to test the functionality using `python [main.py](http://main.py/)`

## Contributing:

Feel free to fork this repository and make improvements!
