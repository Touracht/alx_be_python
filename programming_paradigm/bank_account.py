class BankAccount:
    def __init__(self, account_balance):
        self.account_balance = account_balance
        
    
    def deposit(self, amount):
            self.account_balance += amount

    def withdraw(self, amount):
        self.account_balance -= amount
        if self.account_balance < 0 and self.account_balance < amount:
            return False                
        else:
            return True
                
        
    def display_balance(self):
        print(f"Current Balance: ${self.account_balance:.2f}")
        return