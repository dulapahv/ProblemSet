# """
# These functions allow user to read and write data from/to a file.

# The data in the files are stored as {key}={value} pairs.


# User can change how the data in the files are stored by changing the these 2 lines.
# Assuming we want to store data in the file as {key} = {value} (with spaces between the key and value), we need to change:

# `return value.removeprefix(f"{key}=")` line in the `read_data` function to `return value.removeprefix(f"{key} = ")`
# and
# `return value.removeprefix(f"{key}=")` line in the `write_data` function to `return value.removeprefix(f"{key} = ")`
# """

# """Search and Get Value in a file"""


# def read_data(file, key):
#     try:
#         with open(file, "r") as readObj:
#             for line in readObj:
#                 if key in line:
#                     value = line.rstrip()
#         return value.removeprefix(f"{key}=")
#     except PermissionError:
#         raise PermissionError("Permission denied")
#     except FileNotFoundError:
#         raise FileNotFoundError("File not found")
#     except UnboundLocalError:
#         raise UnboundLocalError("Key not found")


# """Search and Replace Value in a file"""


# def write_data(file, key, value):
#     try:
#         with open(file, "r") as readObj:
#             fileData = readObj.read()
#             fileData = fileData.replace(
#                 f"{key} = {read_data(key)}", f"{key}={str(value)}")
#         with open(file, "w") as writeObj:
#             writeObj.write(fileData)
#     except PermissionError:
#         raise PermissionError("Permission denied")
#     except FileNotFoundError:
#         raise FileNotFoundError("File not found")
#     except UnboundLocalError:
#         raise UnboundLocalError("Key not found")

# sum = 0
# for i in range(1,5+1):
#     for j in range(1,i+1):
#         sum += j + 10

# print(sum)

# sum = 0
# for i in range(1,5+1):
#     sum += j + 10

# print(sum)

# x = [i for i in range(1,5+1)]
# print(x)

# from tcp_latency import measure_latency
# import time

# while True:
#     ping = (measure_latency(host='138.91.42.107', port=25565, timeout=2.5))
#     print(ping)
#     time.sleep(180)


# class BetterList:
#     def __init__(self, *args):
#         self.list = list(args)

#     def __add__(self, other):
#         return BetterList(self.list + other.list)

#     def __str__(self):
#         return str(self.list)

#     def __getitem__(self, index):
#         return self.list[index]

#     def __setitem__(self, index, value):
#         self.list[index] = value

#     def __len__(self):
#         return len(self.list)

#     def __delitem__(self, index):
#         del self.list[index]

#     def __iter__(self):
#         return iter(self.list)

#     def __reversed__(self):
#         return reversed(self.list)

#     def __contains__(self, item):
#         return item in self.list

#     def __eq__(self, other):
#         return self.list == other.list

#     def __ne__(self, other):
#         return self.list != other.list

#     def __gt__(self, other):
#         return self.list > other.list


# list1 = BetterList(1,2,3)
# list2 = BetterList(4,5,6)

# print(list1 + list2)
# print(list1)

# class Card:
#     def __init__ (self, value, suit):
#         self.v = value
#         self.s = suit

#     def __str__ (self):
#         return "(" + self.v + " " + self.s + ")"

#     def getScore(self):
#         pairs = {"A": 1, "2": 2, "3": 3, "4": 4,
#                  "5": 5, "6": 6, "7": 7, "8": 8,
#                  "9": 9, "10": 10}
#         if self.v in ["J", "Q", "K"]:
#             return pairs["10"]
#         return pairs[self.v]

#     def sum(self, other):
#         return (self.getScore() + other.getScore()) % 10

#     def __lt__ (self, rhs):
#         faces = {"3": 10, "4": 20, "5": 30, "6": 40,
#                  "7": 50, "8": 60, "9": 70, "10": 80,
#                  "J": 90, "Q": 100, "K" : 110, "A": 120,
#                  "2": 130}
#         suits = {"club": 1, "diamond": 2, "heart": 3,
#                  "spade": 4}
#         return (faces[self.v] + suits[self.s]) < (faces[rhs.v] + suits[rhs.s])

# n = int(input())

# cards = []

# for i in range(n):
#     value, suit = input().split()
#     cards.append(Card(value, suit))

# for i in range(n):
#     print(cards[i].getScore())

# print("-" * 10)

# for i in range(n - 1):
#     print(Card.sum(cards[i], cards[i+1]))

# print("-" * 10)


# cards.sort()

# for i in range(n):
#     print(cards[i])


# # Euler method python program

# # function to be solved
# def f(x,y):
#     return x+y

# # or
# # f = lambda x: x+y

# # Euler method
# def euler(x0,y0,xn,n):

#     # Calculating step size
#     h = (xn-x0)/n

#     print('\n-----------SOLUTION-----------')
#     print('------------------------------')
#     print('x0\ty0\tslope\tyn')
#     print('------------------------------')
#     for i in range(n):
#         slope = f(x0, y0)
#         yn = y0 + h * slope
#         print('%.4f\t%.4f\t%0.4f\t%.4f'% (x0,y0,slope,yn) )
#         print('------------------------------')
#         y0 = yn
#         x0 = x0+h

#     print('\nAt x=%.4f, y=%.4f' %(xn,yn))

# # Inputs
# print('Enter initial conditions:')
# x0 = float(input('x0 = '))
# y0 = float(input('y0 = '))

# print('Enter calculation point: ')
# xn = float(input('xn = '))

# print('Enter number of steps:')
# step = int(input('Number of steps = '))

# # Euler method call
# euler(x0,y0,xn,step)

# import math
# x = math.e ** (0.0004 ** 2)
# print(f"{x:.10f}")

# def solve(h, x=0.4):
#     x0 = x - h  # find x0
#     y0 = 1 + (x0 * (0 * (1 ** 0.5)))  # find y(x0)
#     return 1 + (h * (x0 * (y0 ** 0.5)))

# print(solve(0.0004))

# // pseudocode
#  function powmod(base b, exponent e, modulus m)
#   if m = 1 then return 0
#   var c := 1
#   for var a from 1 to e
#     c := (c * b) mod m
#   end for
#   return c

# def powmod(base, expo, modulus):
#     if modulus == 1:
#         return 0
#     c = 1
#     for i in range(1, expo + 1):
#         print(f'{c} * {base} % {modulus} = {c * base % modulus}')
#         c = (c * base) % modulus
#     return c

# print(powmod(6036982461, 21345, 23))

# height = int(input())
# for i in range(height):
#     print(' ' * (height - i - 1), end='')
#     print('*' * ((2 * i) + 1), end='')
#     print()

# data = []
# for i in range(5):
#     data.append(input())

# score = int(input())

# if score >= 90:
#     print('A')
# elif score >= 85 and score <= 89:
#     print('B+')
# elif score >= 80 and score <= 84:
#     print('B')
# elif score >= 75 and score <= 79:
#     print('C+')
# elif score >= 70 and score <= 74:
#     print('C')
# elif score >= 65 and score <= 69:
#     print('D+')
# elif score >= 60 and score <= 64:
#     print('D')
# else:
#     print('F')

# height = int(input())
# for i in range(height):
#     print(' ' * (height - i - 1), end='')
#     print('*' * ((2 * i) + 1), end='')
#     print()
# for i in range(height - 1):
#     print(' ' * (i + 1), end='')
#     print('*' * (2 * (height - i - 1) - 1), end='')
#     print()

# column = int(input())
# row = int(input())

# mat = []
# for i in range(row * column):
#     mat.append(float(input()))

# for i in range(row):
#     for j in range(column):
#         result = (mat[i * column + j] - min(mat)) / (max(mat) - min(mat))
#         print(f"{result:.4f}", end=' ')
#     print()

# string = input()

# for i in range(len(string)):
#     print(' ' * (len(string) - i - 1) + string[i], end='')
#     print()

# n = int(input())
# data = []
# for i in range(n):
#     data.append(int(input()))

# x = 1
# while True:
#     if len(data) <= (2 ** x):
#         break
#     x += 1

# print(x)

# import math
# sum = 0
# for i in range(0, 101):
#     print(i)
#     sum += math.floor(i/5)

# print(sum)

# import math
# try:
#     for i in range(1, 101):
#         for y in range(-99999, 99999):
#             if (i / y) - 1 == -1:
#                 print(f"{y = }")
#                 break
# except:
#     pass

# import math
# sum = 0
# for i in range(0, 11):
#     sum += (math.factorial(10)) / (math.factorial(i) * math.factorial(10 - i))

# print(sum)

"""
>>> factorial(5)
120

>>> [factorial(n) for n in range(6)]
[1, 1, 2, 6, 24, 120]

>>> factorial(30)
265252859812191058636308480000000

>>> factorial(-1)
Traceback (most recent call last):
    ...
ValueError: n must be >= 0

>>> factorial(30.1)
Traceback (most recent call last):
    ...
ValueError: n must be exact integer

>>> factorial(30.0)
265252859812191058636308480000000


>>> factorial(1e100)
Traceback (most recent call last):
    ...
OverflowError: n too large
"""

# def factorial(n):
#     import math
#     if not n >= 0:
#         raise ValueError("n must be >= 0")
#     if math.floor(n) != n:
#         raise ValueError("n must be exact integer")
#     if n+1 == n:  # catch a value like 1e300
#         raise OverflowError("n too large")
#     result = 1
#     factor = 2
#     while factor <= n:
#         result *= factor
#         factor += 1
#     return result

# if __name__ == "__main__":
#     import doctest
#     doctest.testmod()

# from chadchart import Policy
# policy = Policy()
# policy.show_all()
# print('All policy:',policy.all)
# print('-----')
# print('Number 1 (dictionary):', policy.number(1))
# print('Number 1 (thai):',policy.number(1)['thai'])
# print('Number 1 (english):',policy.number(1)['english'])
# print('Number 1 (tag):', policy.number(1)['tag'])
# print(policy.all_tag)
# print(policy.all_tag['เรียนดี'])
# policy.show_category()
# policy.category('ปลอดภัยดี')
# policy.credit()
# policy.developer()

# def find_avg(data):
#     try:
#         return sum(data) / len(data)
#     except ZeroDivisionError:
#         raise Exception("Cannot find average of empty data!")
#     except TypeError:
#         raise Exception("Data type not supported!")

# print(find_avg([1, 2, 3, 4, 5]))

