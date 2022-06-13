# import math

# usin = input().split(",")
# num = eval(usin[0] + "." + usin[1] + usin[2])
# decimal = num
# decimalNew = decimal * (10 ** (len(usin[1]) + 1))
# x = 10 ** len(usin[1])
# xNew = 10 ** (len(usin[1]) + 1)
# numerator = int(decimalNew - int(decimal * x))
# denominator = xNew - x

# print(decimal)
# print(decimalNew)
# print(x)
# print(xNew)

# gcd = math.gcd(numerator, denominator)
# numerator /= gcd
# denominator /= gcd

# print(f"{int(numerator)} / {int(denominator)}")

# import math

# integer, decimal, recurring = input().split(",")
# """
# Convert user input into a number
# """
# # print(integer)
# # print(decimal)
# # print(recurring)
# num = eval(integer + "." + decimal + recurring)
# print(f"{num=}")

# """
# Multiplying both sides of the equation
# i.e. x = 0.77 -> 10x = 7.7
# """
# x = 10 ** (len(decimal) + len(recurring))
# print(f"{x=}")
# num *= x
# print(f"{num=}")
# xPrevious = x / 10
# numPrevious = num / 10
# print(f"{xPrevious=}")
# print(f"{numPrevious=}")
# numerator = math.ceil(num - numPrevious)
# denominator = int(x - xPrevious)
# print(f"{numerator=}")
# print(f"{denominator=}")

# gcd = math.gcd(numerator, denominator)
# numerator /= gcd
# denominator /= gcd

# print(f"{int(numerator)} / {int(denominator)}")

import math

integer, decimal, recurring = input().split(",")
num = eval(integer + "." + decimal + recurring)
x = 10 ** (len(decimal) + len(recurring))
num *= x
xPrevious = x / 10
numPrevious = num / 10
numerator = math.ceil(num - numPrevious)
denominator = int(x - xPrevious)
gcd = math.gcd(numerator, denominator)
numerator /= gcd
denominator /= gcd
print(f"{int(numerator)} / {int(denominator)}")