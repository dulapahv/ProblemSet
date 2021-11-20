even, odd = 0, 0
for i in range(5):
    num = int(input("enter a number "))
    if num % 2 == 0:
        even += 1
    else:
        odd += 1
print(f"there were {even} even numbers")
print(f"there were {odd} odd numbers")