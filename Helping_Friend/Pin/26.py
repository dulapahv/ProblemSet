import math
v = input('Input v: ')

if 48 <= ord(v[0]) <= 57:
    s, n, i = 0, 0, 0
    while s <= float(v):
        s += math.sqrt(2) * i - 1
        n += 1
        i += 1
    print(f"Output: n = {n}, S = {s:.2f}")
else:
    print("Invalid input")