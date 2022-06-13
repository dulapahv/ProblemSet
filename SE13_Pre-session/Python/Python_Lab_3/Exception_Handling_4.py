a = float(input("a: "))
b = float(input("b: "))

try:
    a/b
except ZeroDivisionError:
    print("can't divide with zero")
else:
    print("the answer of a divide by b is {}".format(a/b))
