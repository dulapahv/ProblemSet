class EWallet:
    def __init__(self, owner, maxMoney):
        self.owner = owner
        self.maxMoney = maxMoney
        self.balance = 0
    
    def deposit(self, amount):
        if self.balance + amount <= self.maxMoney:
            self.balance += amount
            print(f"Deposited {amount}. Current balance: {self.balance}")
        else:
            print("You have reached maximum amount of money for your account!")

    def withdraw(self, amount):
        if self.balance - amount >= 0:
            self.balance -= amount
            print(f"Withdrawn {amount}. Current balance: {self.balance}")
        else:
            print("You don't have enough money to withdraw!'")
    
    def getBalance(self):
        print(f"Current balance: {self.balance} THB")