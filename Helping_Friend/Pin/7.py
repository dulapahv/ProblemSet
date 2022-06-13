balance = int(input("Enter the initial balance: "))

while True:
    usin = input('Transaction type and amount ("done 0" to exit): ').split()
    if usin[0] == "done":
        break
    elif usin[0] == "D" and int(usin[1]) >= 0:
        balance += int(usin[1])
        print(f"> Deposit = {usin[1]} THB, current balance = {balance} THB.")
    elif usin[0] == "W" and int(usin[1]) >= 0:
        balance -= int(usin[1])
        print(f"> Withdrawal = {usin[1]} THB, current balance = {balance} THB.")
    else:
        print("> Invalid transaction!")

print(f"> Current balance = {balance} THB.")