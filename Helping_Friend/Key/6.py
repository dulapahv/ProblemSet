import sys

def get_Input(msg):
    usin = float(input(msg))
    if usin == 0:
        print("1st coefficient can't be zero. Program exits.")
        sys.exit()
    else:
        return usin
        

a = get_Input("Value of 1st coefficient: ")
b = get_Input("Value of 2nd coefficient: ")
c = get_Input("Value of 3rd coefficient: ")

dis = (b**2) - (4 * a * c)
if dis > 0:
    result1 = ((-1 * b) + (dis**0.5)) / (2 * a)
    result2 = ((-1 * b) - (dis**0.5)) / (2 * a)
    print(f"Two real roots: {result1:.3f} and {result2:.3f}")
elif dis == 0:
    result = (-1 * b) / (2 * a)
    print(f"There is one real root: {result:.3f}")
else:
    result1 = (-1 * b) / (2 * a)
    result2A = ((-1 * dis)**0.5) / (2 * a)
    result2B = result2A * -1
    if result2A >= 0:
        print(f"Two complex roots: {result1:.3f}+{result2A:.3f}i and {result1:.3f}{result2B:.3f}i")
    else:
        print(f"Two complex roots: {result1:.3f}+{result2B:.3f}i and {result1:.3f}{result2A:.3f}i")