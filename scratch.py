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

import math
x = math.e ** (0.0004 ** 2)
print(f"{x:.10f}")