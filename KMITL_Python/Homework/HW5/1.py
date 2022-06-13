n = float(input("Enter a number: "))
guess = n / 2
temp = 0
for i in range(3):
    for j in range(5 + i):
        temp = n / guess
        guess = (guess + temp) / 2
    print(f"{5 + i} times: {guess:.3f}")