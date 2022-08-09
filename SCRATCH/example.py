n=int(input())
for i in range(n+1):print(f"{' '*(len(bin(n))-len(bin(i)))}{i:b}")