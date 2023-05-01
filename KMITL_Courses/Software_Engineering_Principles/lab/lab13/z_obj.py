import ZODB
import ZODB.FileStorage
import persistent
from abc import ABC, abstractmethod
import datetime as dt


class Customer(persistent.Persistent):
    def __init__(self, name=""):
        self.name = name
        self.accounts = persistent.list.PersistentList()

    def __str__(self):
        return "Customer Name: " + self.name

    def addAccount(self, a):
        self.accounts.append(a)
        return a

    def account(self, n):
        if 0 <= n < len(self.accounts):
            return self.accounts[n]
        return None

    def printStatus(self):
        print(self.__str__())
        for a in self.accounts:
            print("", end="    ")
            a.printStatus()


class Account(ABC):
    def __init__(self, balance=0.0, owner=None):
        self.balance = balance
        self.owner = owner
        self.bankTransaction = []

    @abstractmethod
    def __str__(self):
        raise NotImplementedError(
            "users must define __str__ to use this base class")

    @abstractmethod
    def deposit(self, amount):
        raise NotImplementedError(
            "users must define deposit to use this base class")

    @abstractmethod
    def withdraw(self, amount):
        raise NotImplementedError(
            "users must define withdraw to use this base class")

    @abstractmethod
    def transfer(self, amount, account):
        raise NotImplementedError(
            "users must define transfer to use this base class")

    @abstractmethod
    def accountDetails(self):
        raise NotImplementedError(
            "users must define accountDetails to use this base class")

    def transferIn(self, m, o):
        if issubclass(o.__class__, Account):
            self.balance += m

    def getBalance(self):
        return self.balance

    def printStatus(self):
        print(self.__str__())

    def printBankTransaction(self):
        self.printStatus()
        print()
        for t in self.bankTransaction:
            t.printDetail()
            print()


class SavingAccount(Account, persistent.Persistent):
    def __init__(self, balance=0.0, owner=None, interest=1.0):
        Account.__init__(self, balance, owner)
        self.interest = interest

    def __str__(self):
        return f"Saving Account of Customer : {self.owner.name}    Balance : {self.balance:.2f}    Interest : {self.interest:.2f}"

    def deposit(self, amount):
        transaction = BankTransaction(
            amount, self.balance, dt.datetime.now(), "Deposit")
        self.bankTransaction.append(transaction)
        self.balance += amount

    def withdraw(self, amount):
        if amount <= self.balance:
            transaction = BankTransaction(
                -amount, self.balance, dt.datetime.now(), "Withdraw")
            self.bankTransaction.append(transaction)
            self.balance -= amount

    def transfer(self, amount, account):
        if amount <= self.balance:
            account.transferIn(amount, self)
            transaction = BankTransaction(
                -amount, self.balance, dt.datetime.now(), "Transfer to " + account.__str__().split(":")[1].split(" ")[1])
            self.bankTransaction.append(transaction)
            self.balance -= amount

    def transferIn(self, m, o):
        transaction = BankTransaction(
            m, self.balance, dt.datetime.now(), "Transfer from " + o.__str__().split(":")[1].split(" ")[1])
        self.bankTransaction.append(transaction)
        return super().transferIn(m, o)

    def accountDetails(self):
        print(self.__str__())


class CurrentAccount(Account, persistent.Persistent):
    def __init__(self, balance=0.0, owner=None, limit=-5000.0):
        Account.__init__(self, balance, owner)
        self.limit = limit

    def __str__(self):
        return f"Current Account of Customer : {self.owner.name}    Balance : {self.balance:.2f}    Limit : {self.limit:.2f}"

    def deposit(self, amount):
        transaction = BankTransaction(
            amount, self.balance, dt.datetime.now(), "Deposit")
        self.bankTransaction.append(transaction)
        self.balance += amount

    def withdraw(self, amount):
        if amount <= self.balance:
            transaction = BankTransaction(
                -amount, self.balance, dt.datetime.now(), "Withdraw")
            self.bankTransaction.append(transaction)
            self.balance -= amount

    def transfer(self, amount, account):
        if amount <= self.balance:
            account.transferIn(amount, self)
            transaction = BankTransaction(
                -amount, self.balance, dt.datetime.now(), "Transfer to " + account.__str__().split(":")[1].split(" ")[1])
            self.bankTransaction.append(transaction)
            self.balance -= amount

    def transferIn(self, m, o):
        transaction = BankTransaction(
            m, self.balance, dt.datetime.now(), "Transfer from " + o.__str__().split(":")[1].split(" ")[1])
        self.bankTransaction.append(transaction)
        return super().transferIn(m, o)

    def accountDetails(self):
        print(self.__str__())


class BankTransaction(persistent.Persistent):
    def __init__(self, amount, balance, timestamp, ttype):
        self.amount = abs(amount)
        self.old_balance = balance
        self.new_balance = self.old_balance + amount
        self.timestamp = timestamp
        self.ttype = ttype

    def printDetail(self):
        print(f"{self.ttype}")
        print(f"    Amount:    {self.amount:.2f}")
        print(f"    Old Balance:    {self.old_balance:.2f}")
        print(f"    New Balance:    {self.new_balance:.2f}")
        print(f"    Time Stamp:    {str(self.timestamp)}")
