def UserInput():
    global A, B, C
    A, B, C = input('Input the numbers of products A, B, and C (3 numbers with space): ').split(" ")
    if type(eval(A)) == "int" and type(eval(B)) == "int" and type(eval(C)) == "int":
        ShowPrice()
    else:
        print("Wrong Input!")

def ComputePrice():
  a = 20*A
  b = 50*B
  c = 100*C
  TotalPrice = a+b+c

def ShowPrice():
  a = 20*A
  b = 50*B
  c = 100*C
  MyPrice = a+b+c

  print('The total price is %d'%MyPrice)

UserInput()
