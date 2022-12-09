n = 0
while n < 1:
    n = int(input("Input: "))
    chk = n
for i in range(n):
    for j in range(n): 
        for k in range(j + 1):
            print("*", end = "")
        print()
    for j in range(n):
        for k in range((n - j) - 1):
            if (n - j) - 1 != 1:
                print("*", end = "")
        if j < n - 2:
            print()
    n -= 1
if chk != 1:
    print("*")