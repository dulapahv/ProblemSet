n = int(input("Enter number: "))
l = []
for i in range(2,n):
    if n%i == 0:
        l.append(i)
print(l)