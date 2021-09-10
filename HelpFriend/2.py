def conv_input(chk):
    if chk == "A":
        return 10
    elif chk == "B":
        return 11
    elif chk == "C":
        return 12
    elif chk == "D":
        return 13
    elif chk == "E":
        return 14
    elif chk == "F":
        return 15
    return int(chk)

w, x, y, z = input("Input: ").split(":")
n = ((16**3) * conv_input(w)) + ((16**2) * conv_input(x)) + (16 * conv_input(y)) + conv_input(z)
print(f"Output = {n}")