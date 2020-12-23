# For this challenge, create a bank account class that has two attributes:
#
# owner
# balance
# and two methods:
#
# deposit
# withdraw
# As an added requirement, withdrawals may not exceed the available balance.
#
# Instantiate your class, make several deposits and withdrawals, and test to make sure the account can't be overdrawn.
class Account:

    def __init__(self, owner, balance):
        self. owner = owner
        self.balance = balance

    def __str__(self):
        return f'Account owner: {self.owner}\nHas Account balance: {self.balance}'

    def deposit(self, amount):
        print("Deposit Accepted")
        self.balance = self.balance + amount

    def withdraw(self, amount):
        if self.balance > amount:
            self.balance = self.balance - amount
            print("Withdrawal Accepted")
        else:
            print("Funds Unavailable!")
