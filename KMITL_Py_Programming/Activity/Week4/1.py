name = input("Enter employee’s name: ")
hour = float(input("Enter number of hours worked in a week: "))
rate = float(input("Enter hourly pay rate: "))
fedTax = float(input("Enter federal tax withholding rate: "))
staTax = float(input("Enter state tax withholding rate: "))

gross = rate * hour
fedHold = gross * fedTax
staHold = gross * staTax
totalHold = fedHold + staHold
print(f"\nEmployee Name: {name}")
print(f"Hours Worked: {hour}")
print(f"Pay Rate: {rate}")
print(f"Gross Pay: {gross}")
print("Deductions:\n   ",
        f"Federal Withholding ({fedTax * 100}%) : ${fedHold}\n   ",
        f"State Withholding ({staTax * 100}%) : ${staHold}\n   ",
        f"Total Deduction: ${totalHold}\n" +
    f"Net Pay: ${(gross - totalHold)}")
