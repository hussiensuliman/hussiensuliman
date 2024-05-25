class BankAccount:
    def __init__(self, account_number, account_holder,balance=0.0):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = balance
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited ${amount:.2f}. New balance: ${self.balance:.2f}")
        else:
            print("Deposit amount must be positive.")
    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew ${amount:.2f}. New balance: ${self.balance:.2f}")
        else:
            print("Insufficient balance or invalid withdrawal amount.")
    def get_balance(self):
        return str(self.balance) 
class SavingsAccount(BankAccount):
    def __init__(self, account_number, account_holder, interest_rate):
        super().__init__(account_number, account_holder)
        self.interest_rate = interest_rate
    def apply_interest(self):
        interest = self.balance * self.interest_rate / 100
        self.balance += interest
        print(f"Applied interest: ${interest:.2f}. New balance: ${self.balance:.2f}")
    def get_balance(self):
        return f"Account holder: {self.account_holder}, Balance: ${self.balance:.2f}, Interest rate: {self.interest_rate}%"
account = BankAccount("123456789", "John Doe")
account.deposit(1000)
account.withdraw(500)
print("balance:",end ='')
print(account.get_balance())
savings_account = SavingsAccount("987654321", "Jane Doe", 2.5)
savings_account.deposit(1000)
savings_account.apply_interest()
print(savings_account.get_balance())
