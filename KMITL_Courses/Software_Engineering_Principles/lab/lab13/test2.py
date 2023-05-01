import ZODB
import ZODB.FileStorage
import persistent
from abc import ABC, abstractmethod
import BTrees.OOBTree
import transaction
import z_obj

storage = ZODB.FileStorage.FileStorage('mydata.fs')
db = ZODB.DB(storage)
connection = db.open()
root = connection.root

if __name__ == "__main__":
    root.customers = BTrees.OOBTree.BTree()
    root.customers["Jone"] = z_obj.Customer("Jone")
    root.customers["Mary"] = z_obj.Customer("Mary")
    j = root.customers["Jone"]
    m = root.customers["Mary"]
    j.printStatus()

    a = j.addAccount(z_obj.SavingAccount(100, j))
    b = j.addAccount(z_obj.CurrentAccount(200, j))
    c = m.addAccount(z_obj.SavingAccount(1000, m))

    c.transfer(100, a)

    a.transfer(150, b)

    b.deposit(500)

    b.withdraw(50)

    b.transfer(200, c)

    c.withdraw(250)

    print()
    print("Account C")
    print()
    c.printBankTransaction()

    transaction.commit()
