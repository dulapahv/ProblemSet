size = int(input("Enter arrow size: "))
for i in range(size - 1):
    print(" " * (size - i - 1) + "*" * (i + 1))
print("*" * (size * 2))
for i in range(size - 1):
    print(" " * (i + 1) + "*" * (size - i - 1))