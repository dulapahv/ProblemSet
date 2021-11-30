msg = input("Enter a message: ")
print("+" + "-" * len(msg) + "+")
for i, char in enumerate(msg):
    print("|" + " " * (len(msg) - i - 1) + f"{char}", end="")
    print(" " * i + "|")
print("+" + "-" * len(msg) + "+")