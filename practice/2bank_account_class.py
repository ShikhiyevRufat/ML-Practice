class BankAccount:
    def __init__(self, account_holder, balance = 0.0):
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"{self.account_holder} your balance increase to {amount}.Your total balance is {self.balance}")

    def withdraw(self, amount):
        if self.balance > amount:
            self.balance -= amount
            print(f"Now your balance is {self.balance}")
        else:
            print(f"You have not enough balance!")

    def display_balance(self):
        print(f"Final balance {self.balance}")



result = BankAccount("Rufat Shikhiyev", 1000)
result.deposit(500)
result.withdraw(900)
result.display_balance()




# class SavingsAccount(BankAccount):
#     def __init__(self, interest_rate):
#         self.interest_rate = interest_rate

#     def apply_interest():
#         pass