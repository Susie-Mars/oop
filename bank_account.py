class BankAccount:
    
    bank_name = "Bank Dojo"

    def __init__(self, int_rate, balance): 
        self.int_rate = int_rate
        self.balance = balance

    def deposit(self, amount):
        self.balance+=(amount)
        return self
    
    def with_draw(self,amount):
        if BankAccount.can_withdraw(self.balance,amount):
            self.balance -= amount
        else:
            # self.balance-= 
            print("Insufficient Funds: Charging a $5 fee")
        return self

    @staticmethod
    def can_withdraw(balance,amount):
        if (balance - amount) < 0:
            return False
        else:
            return True

    def display_account_info(self):
        print(f"Balance: {self.balance}")
        return self
    
    def yield_interest(self):
        if self.balance> 0:
            self.balance += self.balance * self.int_rate
        return self



account_1 = BankAccount(.01,0)
account_2 = BankAccount(.01, 0)

account_1.deposit(50).deposit(100).deposit(75).with_draw(40).yield_interest().display_account_info()
account_2.deposit(40).deposit(500).with_draw(20).with_draw(30).with_draw(20).with_draw(100).yield_interest().display_account_info()