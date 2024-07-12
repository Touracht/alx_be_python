class BankAccount:
    def __init__(self,initial_balance = 0.00):
        self.account_balance = initial_balance
        
    
    def deposit(self, amount):
            self.account_balance += amount
            return self.account_balance

    def withdraw(self, amount):
        self.account_balance -= amount
        if self.account_balance - amount > 0.00:
            return True
        else:
            print("Insufficient funds.")
            return False
                
        
    def display_balance(self):
        print(f"Current Balance: ${self.account_balance:.2f}")
        return