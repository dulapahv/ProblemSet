class BankAccount:
    def __init__(self, bankName, ownerName, accountNumber, balance):
        self.bankName = bankName
        self.ownerName = ownerName
        self.accountNumber = accountNumber
        self.balance = balance
    
    def deposit(self, amountDeposit):
        self.balance += amountDeposit
        print("Amount deposit: %d" %amountDeposit)
        print("Amount deposit: %d" %self.balance)

    def withdraw(self, amountDeposit):
        if amountDeposit < self.balance:
            self.balance -= amountDeposit
            print("Amount deposit: %d" %amountDeposit)
            print("Amount deposit: %d" %self.balance)

    def currentBalance(self):
        print("Current Balance: %d" %self.balance)

