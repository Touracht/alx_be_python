class BankAccount:
    def __init__(self, account_balance, initial_balance = 0.0):
        self.account_balance = account_balance
        self.current_balance = initial_balance
    
    def deposit(self, amount):
            self.current_balance += amount
            return (self.current_balance)

    def withdraw(self, amount):
        self.current_balance -= amount
        if amount > self.current_balance:
            return True
        else:
            return False
        
    def display_balance(self):
        print(f"Your current balance is {self.current_balance}")