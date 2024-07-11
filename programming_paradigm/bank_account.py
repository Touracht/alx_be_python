class BankAccount:
    def __init__(self, account_balance, initial_balance = f"{0:.2f}"):
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
        print(f"Current Balance: ${self.current_balance}")
        return