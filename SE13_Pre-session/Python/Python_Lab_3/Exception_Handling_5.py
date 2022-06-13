a = float(input("a: "))
b = float(input("b: "))

if b == 0:
    raise Exception("Sorry, can't divide with zero")
else:
    print("the answer of a divide by b is {}".format(a/b))
