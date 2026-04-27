class BankAccount:
    def __init__(self, account_number, balance=0.0):
        self.account_number = account_number
        self.balance = float(balance)

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount > self.balance:
            return -1
        self.balance -= amount
        return 0

    def __str__(self):
        return (
            f"Account Number: **{str(self.account_number)[-2:]}\n"
            f"Current Balance: {self.balance:.2f}"
        )
