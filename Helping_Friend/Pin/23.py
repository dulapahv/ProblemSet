def MySumSquare(n):
    sum=0
    for i in range (1, n+1):
        sum+=i**2
    return sum

n = eval(input('Input an integer number: '))
if 1<n<100 and type(n) == int:
    summa = MySumSquare(n)
    print('The summation of squares is %d'%summa)
else:
    print('Error')