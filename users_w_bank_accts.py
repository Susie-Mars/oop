class BankAccount:
    
    bank_name = "Bank Dojo"

    def __init__(self, int_rate, balance): 
        self.int_rate = int_rate
        self.balance = balance
    
    def deposit(self, amount):
        self.balance+=(amount)
        return self
    
    def with_draw(self,amount):
        self.balance-=(amount)
        return self

class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account = BankAccount(int_rate=0.02, balance=0)
    
    def make_deposit(self, amount):
        self.account.deposit(amount)
        print(self.account.balance)
        return self
    
    def make_withdrawal(self, amount):
        self.account.with_draw(amount)
        print(self.account.balance)
        return self

    def display_user_balance(self):
        print(f"User:{self.name} Balance :{self.account.balance}")
        return self



account_1 = User("Johnny Max", "jmax@mail.com")

account_1.make_deposit(200).make_withdrawal(25).display_user_balance()
