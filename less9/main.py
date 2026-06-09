# #### Task 1: Create a Library Management System with Custom Exceptions
# 1. Create a Python program to manage a small library system. 
# 2. Define custom exceptions for specific scenarios:
#    - **`BookNotFoundException`**: Raised when trying to borrow a book that doesn’t exist in the library.
#    - **`BookAlreadyBorrowedException`**: Raised when a book is already borrowed.
#    - **`MemberLimitExceededException`**: Raised when a member tries to borrow more books than allowed.
# 3. Implement classes for:
#    - **`Book`**: Attributes include `title`, `author`, and `is_borrowed`.
#    - **`Member`**: Attributes include `name`, `borrowed_books` (limit to 3 books per member).
#    - **`Library`**: Manages books and members, including borrowing and returning books.
# 4. Test your program with the following scenarios:
#    - Adding books and members.
#    - Borrowing and returning books.
#    - Handling exceptions when rules are violated.

class BookNotFoundException(Exception):
    pass

class BookAlreadyBorrowedException(Exception):
    pass

class MemberLimitExceededException(Exception):
    pass

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_borrowed = False

class Member:
    def __init__(self, name):
        self.name = name
        self.borrowed_books = []

    def borrow_book(self, book):
        if len(self.borrowed_books) >= 3:
            raise MemberLimitExceededException(f"{self.name} cannot borrow more than 3 books.")
        if book.is_borrowed:
            raise BookAlreadyBorrowedException(f"{book.title} is already borrowed.")
        book.is_borrowed = True
        self.borrowed_books.append(book)

    def return_book(self, book):
        if book in self.borrowed_books:
            book.is_borrowed = False
            self.borrowed_books.remove(book)

class Library:
    def __init__(self):
        self.books = []
        self.members = []
    def add_book(self, title, author):
        self.books.append(Book(title, author))
    def add_member(self, name):
        self.members.append(Member(name))
    def borrow_book(self, member_name, book_title): 
        member = next((m for m in self.members if m.name == member_name), None)
        if not member:
            raise BookNotFoundException(f"Member {member_name} not found.")
        book = next((b for b in self.books if b.title == book_title), None)
        if not book:
            raise BookNotFoundException(f"Book {book_title} not found.")
        member.borrow_book(book)
    def return_book(self, member_name, book_title):
        member = next((m for m in self.members if m.name == member_name), None)
        if not member:
            raise BookNotFoundException(f"Member {member_name} not found.")
        book = next((b for b in self.books if b.title == book_title), None)
        if not book:
            raise BookNotFoundException(f"Book {book_title} not found.")
        member.return_book(book)


# ---

# #### Task 2: Student Grades Management
# 1. Create a CSV file named `grades.csv` with the following structure:
   
# csv
#    Name,Subject,Grade
#    Alice,Math,85
#    Bob,Science,78
#    Carol,Math,92
#    Dave,History,74
   


# 2. Write a Python program to:
#    - Read data from `grades.csv` and store it in an appropriate data structure (e.g., a list of dictionaries).
#    - Calculate the average grade for each subject.
#    - Write a new CSV file named `average_grades.csv` with the following structure:
     
def calculate_average_grades(input_file, output_file):
    import csv
    from collections import defaultdict

    grades = defaultdict(list)

    # Read the grades from the input CSV file
    with open(input_file, mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            subject = row['Subject']
            grade = float(row['Grade'])
            grades[subject].append(grade)

    # Calculate average grades
    average_grades = {subject: sum(grades[subject]) / len(grades[subject]) for subject in grades}

    # Write the average grades to the output CSV file
    with open(output_file, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Subject', 'Average Grade'])
        for subject, avg_grade in average_grades.items():
            writer.writerow([subject, avg_grade])
# Example usage
calculate_average_grades('grades.csv', 'average_grades.csv')


# csv
#      Subject,Average Grade
#      Math,88.5
#      Science,78
#      History,74
     


# 3. Use the `csv` module for reading and writing the CSV files.

# ---

# ### **Task 3: JSON Handling**

# #### **Load and Save Tasks (JSON)**
# 1. Create a JSON file named `tasks.json` with the following structure:
   


# json
#    [
#        {"id": 1, "task": "Do laundry", "completed": false, "priority": 3},
#        {"id": 2, "task": "Buy groceries", "completed": true, "priority": 2},
#        {"id": 3, "task": "Finish homework", "completed": false, "priority": 1}
#    ]
   


# 2. Write a Python program to:
#    - Load the tasks from `tasks.json`.
#    - Display all tasks with the following fields: ID, Task Name, Completed Status, Priority.
#    - Save any changes back to the `tasks.json` file (e.g., after modifying a task).

# #### **Calculate Task Completion Stats**
# 1. Write a Python function to calculate the following statistics:
#    - **Total tasks**: Count the total number of tasks.
#    - **Completed tasks**: Count the number of completed tasks.
#    - **Pending tasks**: Count the number of tasks that are not completed.
#    - **Average priority**: Calculate the average priority level of all tasks.
   
#    Display these statistics after loading the tasks.

# #### **Convert JSON Data to CSV**
# 1. Write a function to convert the task data in `tasks.json` to a CSV file named `tasks.csv`. The CSV should have the following columns:
#    - ID
#    - Task Name
#    - Completed Status
#    - Priority

def load_tasks(filename):
    import json
    with open(filename, 'r') as file:
        tasks = json.load(file)
    return tasks 

def display_tasks(tasks):
    print(f"{'ID':<5} {'Task Name':<20} {'Completed':<10} {'Priority':<10}")
    for task in tasks:
        print(f"{task['id']:<5} {task['task']:<20} {str(task['completed']):<10} {task['priority']:<10}")

def save_tasks(filename, tasks):
    import json
    with open(filename, 'w') as file:
        json.dump(tasks, file, indent=4)
def calculate_stats(tasks):
    total_tasks = len(tasks)
    completed_tasks = sum(1 for task in tasks if task['completed'])
    pending_tasks = total_tasks - completed_tasks
    average_priority = sum(task['priority'] for task in tasks) / total_tasks if total_tasks > 0 else 0

    print(f"Total tasks: {total_tasks}")
    print(f"Completed tasks: {completed_tasks}")
    print(f"Pending tasks: {pending_tasks}")
    print(f"Average priority: {average_priority:.2f}")

#    For example:
   

# csv
#    ID,Task,Completed,Priority
#    1,Do laundry,False,3
#    2,Buy groceries,True,2
#    3,Finish homework,False,1
def convert_json_to_csv(json_file, csv_file):
    import json
    import csv

    with open(json_file, 'r') as file:
        tasks = json.load(file)

    with open(csv_file, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['ID', 'Task Name', 'Completed', 'Priority'])
        for task in tasks:
            writer.writerow([task['id'], task['task'], task['completed'], task['priority']])
# Example usage
tasks = load_tasks('tasks.json')

