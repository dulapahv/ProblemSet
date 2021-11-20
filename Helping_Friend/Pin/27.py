usin = input("Input 12-digit string: ")

if len(usin) == 12 and usin.isnumeric():
    s = 0
    for i in range(12):
        if i % 2 == 0:
            s += int(usin[i]) * 1
        else:
            s += int(usin[i]) * 3
    t = 10 - (s % 10)
    if t == 10:
        c = 0
    else:
        c = t
    print(f"Output: check digit = {c}")
else:
    print("invalid input")