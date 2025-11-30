print("***************************************************************************************************************")

print("Write a Python class named BankAccount with attributes like account_number, balance, and customer_name, and methods like deposit, withdraw, and check_balance.")

class BankAccount:
    def __init__(self, account_number, customer_name, current_balance = 0):
        self.account_number = account_number
        self.customer_name = customer_name
        self.current_balance = current_balance

    def deposit(self, amount):
        if amount > 0:
            self.current_balance += amount
            print(f"Account credited with  ${amount}. Current balance is :: ${self.current_balance}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount > 0:
            if amount <= self.current_balance:
                self.current_balance -= amount
                print(f"Account debited with ${amount}. Current balance is :: ${self.current_balance}")
            else:
                print("Insufficient balance!")
        else:
            print("Amount must be positive.")

    def check_balance(self):
        print(f"Current balance :: ${self.current_balance}")


account = BankAccount("12973752", "Kiran", 10000)

account.check_balance()
account.deposit(2000)
account.withdraw(5000)
account.withdraw(15000)

print("***************************************************************************************************************")
