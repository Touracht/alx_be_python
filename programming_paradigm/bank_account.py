class BankAccount:
    def __init__(self,initial_balance = 0.0):
        self.account_balance = initial_balance
        
    
    def deposit(self, amount):
            self.account_balance += amount
            return self.account_balance

    def withdraw(self, amount):
        self.account_balance -= amount
        if self.account_balance - amount > 0:
            return True
        else:
            print()
            return False
        
    def display_balance(self):
        print(f"Current Balance: ${self.account_balance}")
        return