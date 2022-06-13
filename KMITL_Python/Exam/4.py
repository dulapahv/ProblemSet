from turtle import *

print("Hello, welcome to Turtle World!")

pd()

usin = '""'
while True:
    usin = input("turtle|>")

    if usin == '"fd"':
        arg = input("Please input its argument:")
        fd(float(arg))
    elif usin == '"back"':
        arg = input("Please input its argument:")
        back(float(arg))
    elif usin == '"lt"':
        arg = input("Please input its argument:")
        lt(float(arg))
    elif usin == '"rt"':
        arg = input("Please input its argument:")
        rt(float(arg))
    elif usin == '"pu"':
        pu()
    elif usin == '"pd"':
        pd()
    elif usin == '"reset"':
        reset() 
    elif usin == '"quit"':
        exit(0)
    else:
        print("Wrong command, please try again.")

mainloop()