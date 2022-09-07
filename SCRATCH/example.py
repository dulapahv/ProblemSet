# n=int(input())
# for i in range(n+1):print(f"{' '*(len(bin(n))-len(bin(i)))}{i:b}")

# # get 2 binary number and output sum in binary, hex, a decimal
# n,m=map(int,input().split())
# print(f"{n+m:b}")
# print(f"{n+m:x}")
# print(f"{n+m}")

# write a code to convert decimal number to 30 bit binary
number = int(input("Enter a number: "))

if number < 0:
   print("Invalid input")
else:
   print(bin(number)[2:].zfill(30))