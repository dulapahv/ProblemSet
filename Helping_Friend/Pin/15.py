import math

t = float(input("Input t: "))
N0 = float(input("Input N0: "))
Nt = float(input("Input Nt: "))

if Nt == N0:
    print("invalid input")
else:
     T = (-693 * t) / math.log(N0 / Nt)
     print(f"Output = {T:.4f}")