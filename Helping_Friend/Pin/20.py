DNA = input("DNA: ")
if DNA.isdigit():
    print("This is not DNA String")
    exit(0)
base = input("Base: ")
if base.isdigit():
    print("This is not DNA String")
    exit(0)
count = 0
for i in range(len(DNA)):
    print(f"c: {DNA[i]}")
    if DNA[i] == base:
        print("True if test")
        count += 1
print(f"There are {count} times that the base {base} occur in this DNA.")