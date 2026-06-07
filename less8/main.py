# ## Model a Farm

# In this assignment, you’ll create a simplified model of a farm. As you work through this assignment, keep in mind that there are a number of correct answers.

# The focus of this assignment is less about the Python class syntax and more about software design in general, which is highly subjective. This assignment is intentionally left open-ended to encourage you to think about how you would organize your code into classes.

# Before you write any code, grab a pen and paper and sketch out a model of your farm, identifying classes, attributes, and methods. Think about inheritance. How can you prevent code duplication? Take the time to work through as many iterations as you feel are
# necessary.

# The actual requirements are open to interpretation, but try to adhere to these guidelines:

# 1. You should have at least four classes: the parent `Animal` class, and then at least three child animal classes that inherit from Animal.
# 2. Each class should have a few attributes and at least one method that models some behavior appropriate for a specific animal or all animals—such as walking, running, eating, sleeping, and so on.
# 3. Keep it simple. Utilize inheritance. Make sure you output details about the animals and their behaviors.

# ---

# ## Build a Bank Application

# #### **Objective:**
# Develop a command-line banking application that allows users to perform basic banking operations like creating an account, depositing money, and withdrawing money. This will help you practice using object-oriented programming (OOP), file handling, and error handling in Python.


# ### **Tasks:**

# #### **Step 1: Define the Classes**
# 1. Create a class `Account` with attributes:
#    - `account_number`
#    - `name`
#    - `balance`

# 2. Create a class `Bank` to manage all accounts. It should have:
#    - A dictionary to store accounts (`accounts`).
#    - Methods for each operation:
#      - `create_account(name, initial_deposit)`
#      - `view_account(account_number)`
#      - `deposit(account_number, amount)`
#      - `withdraw(account_number, amount)`
#      - `save_to_file()` and `load_from_file()` (for file handling).

class Account:
    def __init__(self, account_number, name, balance):
        self.account_number = account_number
        self.name = name
        self.balance = balance

class Bank:
    def __init__(self):
        self.accounts = {}
    
    def create_account(self, name, initial_deposit):
        account_number = len(self.accounts) + 1  # Simple unique account number generation
        account = Account(account_number, name, initial_deposit)
        self.accounts[account_number] = account
        self.save_to_file()
        print(f"Account created successfully! Your account number is {account_number}.")
    
    def view_account(self, account_number):
        account = self.accounts.get(account_number)
        if account:
            print(f"Account Number: {account.account_number}")
            print(f"Name: {account.name}")
            print(f"Balance: ${account.balance:.2f}")
        else:
            print("Account not found.")
    
    def deposit(self, account_number, amount):
        account = self.accounts.get(account_number)
        if account:
            if amount > 0:
                account.balance += amount
                self.save_to_file()
                print(f"Deposited ${amount:.2f} successfully! New balance: ${account.balance:.2f}")
            else:
                print("Deposit amount must be positive.")
        else:
            print("Account not found.")
    
    def withdraw(self, account_number, amount):
        account = self.accounts.get(account_number)
        if account:
            if 0 < amount <= account.balance:
                account.balance -= amount
                self.save_to_file()
                print(f"Withdrew ${amount:.2f} successfully! New balance: ${account.balance:.2f}")
            else:
                print("Invalid withdrawal amount. Check your balance.")
        else:
            print("Account not found.")
    
    def save_to_file(self):
        with open('accounts.txt', 'w') as file:
            for account in self.accounts.values():
                file.write(f"{account.account_number},{account.name},{account.balance}\n")
    
    def load_from_file(self):
        try:
            with open('accounts.txt', 'r') as file:
                for line in file:
                    account_number, name, balance = line.strip().split(',')
                    self.accounts[int(account_number)] = Account(int(account_number), name, float(balance))
        except FileNotFoundError:
            pass  # No accounts to load

class BankApp:
    def __init__(self):
        self.bank = Bank()
        self.bank.load_from_file()
    
    def run(self):
        while True:
            print("\nWelcome to the Bank App!")
            print("1. Create Account")
            print("2. View Account Details")
            print("3. Deposit Money")
            print("4. Withdraw Money")
            print("5. Exit")
            choice = input("Please select an option: ")
            
            if choice == '1':
                name = input("Enter your name: ")
                initial_deposit = float(input("Enter initial deposit amount: "))
                self.bank.create_account(name, initial_deposit)
            elif choice == '2':
                account_number = int(input("Enter your account number: "))
                self.bank.view_account(account_number)
            elif choice == '3':
                account_number = int(input("Enter your account number: "))
                amount = float(input("Enter deposit amount: "))
                self.bank.deposit(account_number, amount)
            elif choice == '4':
                account_number = int(input("Enter your account number: "))
                amount = float(input("Enter withdrawal amount: "))
                self.bank.withdraw(account_number, amount)
            elif choice == '5':
                print("Thank you for using the Bank App. Goodbye!")
                break
            else:
                print("Invalid option. Please try again.")

if __name__ == "__main__":
    app = BankApp()
    app.run()


# #### **Step 2: Implement the Methods**
# 1. **Account Creation**
#    - Generate a unique `account_number`.
#    - Create an `Account` object and store it in the dictionary.
#    - Save account details to a file.

# 2. **View Account Details**
#    - Prompt the user to input their account number.
#    - Retrieve and display the account details if found; otherwise, show an error.

# 3. **Deposit Money**
#    - Prompt the user for their account number and deposit amount.
#    - Validate the amount and update the account balance.

# 4. **Withdraw Money**
#    - Prompt the user for their account number and withdrawal amount.
#    - Validate that the amount is less than or equal to the balance and update the account balance.

# 5. **File Handling**
#    - Use `save_to_file` to write account details to `accounts.txt`.
#    - Use `load_from_file` to load account details when the program starts.

# ---