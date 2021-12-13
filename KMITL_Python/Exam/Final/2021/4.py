class SavingAccount:
    def __init__(self, bank_name, acc_name, acc_id, balance, 
                 transaction_history):
        self.bank_name = bank_name
        self.acc_name = acc_name
        self.acc_id = acc_id
        self.transaction_history = transaction_history
        self.balance = balance
    
    def deposit(self, money, person, date):
        self.balance += money
        self.transaction_history.append(f"deposit {money} by "+
            f"{person} to the account on {date}")

    def withdraw(self, money, person, date):
        if self.balance - money < 0:
            print("Saving account cannot have a negative balance!")
        else:
            self.balance -= money
            self.transaction_history.append(f"withdraw {money} by "+
                f"{person} from the account on {date}")

    def get_balance(self):
        print(self.balance)

    def print_statement(self):
        print(self.transaction_history)


class OverDrawnAccount(SavingAccount):
    def __init__(self, bank_name, acc_name, acc_id, balance, transaction_history, over_drawn_limit):
        super().__init__(bank_name, acc_name, acc_id, balance, transaction_history)

        self.over_drawn_limit = over_drawn_limit
    
    def withdraw(self, money, person, date):
        if self.balance - money < self.over_drawn_limit:
            print("Account balance cannot exceed the over drawn limit!")
        else:
            self.balance -= money
            self.transaction_history.append(f"withdraw {money} by {person} from the account on {date}")
    

test = OverDrawnAccount("SCB", "Judge", "64011388", -200, [], -200)
test.deposit(500, "Judge", "22/5/12")
test.withdraw(400, "nomiya", "22/12/12")
test.get_balance()
test.print_statement()

# test2 = SavingAccount("SCB", "Judge", "64011388", 200, [])
# test2.deposit(500, "Judge", "22/5/12")
# test2.withdraw(200, "nomiya", "22/12/12")
# test2.print_statement()


        